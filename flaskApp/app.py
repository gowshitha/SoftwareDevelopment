# from flask import Flask, render_template, url_for, request

# app = Flask(__name__)

 

# @app.route('/')
# @app.route('/home')
# def home():
#     return render_template("index.html")



# @app.route('/result',methods=['POST', 'GET'])
# def result():
#     output = request.form.to_dict()
#     print(output)
#     name = output["name"]


#     return render_template('index.html', name = name)
    




# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# Download necessary resources
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('wordnet')
# nltk.download('wordnet')
nltk.download('omw-1.4')




def get_wordnet_pos(tag):
    """
    Map POS tag to first character used by WordNetLemmatizer
    """
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def paraphrase(text):
    """
    Paraphrase text by replacing words with their synonyms
    """
    # Tokenize text into words
    words = word_tokenize(text)
    
    # Get the part of speech for each word
    tagged_words = nltk.pos_tag(words)
    
    # Create a new list of words with synonyms substituted for some of them
    new_words = []
    for word, tag in tagged_words:
        # Map the part of speech to a WordNet POS tag
        wn_tag = get_wordnet_pos(tag)
        
        # Find synonyms for the word using WordNet
        synonyms = set()
        for syn in wordnet.synsets(word, pos=wn_tag):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())
        
        # If there are synonyms available, choose one at random to replace the word
        if synonyms:
            new_word = synonyms.pop()
            new_words.append(new_word)
        else:
            new_words.append(word)
    
    # Combine the new words into a new sentence
    new_sentence = " ".join(new_words)
    return new_sentence

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/paraphrase', methods=['POST'])
def paraphrase_text():
    text = request.form['text']
    paraphrased_text = paraphrase(text)
    return render_template('index.html', text=text, paraphrased_text=paraphrased_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

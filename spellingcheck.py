# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mmi2ncnsfXxSLRYZx0pjitKNWSuVAPJJ
"""

import language_tool_python

def check_text(text):
    tool = language_tool_python.LanguageTool('en-US')
    return tool.correct(text)

print("Enter the text you want to check or Type 'quit' to exit.")
while True:
    text = input("Enter your text here: ")
    if text.lower() == "quit":
        break
    if len(text) < 5:
        print("Input must be at least 5 characters long")
    else:
        print("Checking your text...")
        corrected_text = check_text(text)
        print(f"Corrected text: {corrected_text}")
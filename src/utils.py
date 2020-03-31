"""================================================

    * Author: Arya Nguyen
    * Description: Utility functions

================================================"""
import nltk


def tokenize(string):
    string = string.lower()
    string = nltk.word_tokenize(string)
    return string

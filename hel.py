import os
import json

from difflib import get_close_matches



with open('data.json') as f:
    data = json.load(f)

#convert list to string
def listToString(s):
    str1 = " "

    return (str1.join(s))


def find(word):
    if word in  data:
        print("the word is :" + word)
        print("the definition is " + listToString(data[word]))


def closeMatches(patterns, word):
    print(get_close_matches(word, patterns))


def closeUpper(patterns, word):
   # print(get_close_matches(word, patterns))
    print(get_close_matches(word.upper(), patterns))


def closeSmall(patterns, word):
   # print(get_close_matches(word, patterns))
    print(get_close_matches(word.small(), patterns))


word = input("Enter your word:")
find(word)



#print(data)
#    patterns = ['ape', 'apple', 'peach', 'puppy']
closeMatches(data, word)
closeUpper(data,word)

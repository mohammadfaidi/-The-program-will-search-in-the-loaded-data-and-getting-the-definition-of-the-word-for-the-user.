Write a program that:
- Reads JSON data from a file (data.json) as attached.
- Asks the user to enter a word.
- The program will search in the loaded data and getting the definition of the word for the user.
- Enhance your code with string methods and difflib (Like if the user write in Capital, Small ...etc.).






Python | Find all close matches of input string from a list
We are given a list of pattern strings and a single input string. We need to find all possible close good enough matches of input string into list of pattern strings.

Examples:

Input : patterns = ['ape', 'apple', 
                  'peach', 'puppy'], 
          input = 'appel'
Output : ['apple', 'ape']
Recommended: Please try your approach on {IDE} first, before moving on to the solution.
We can solve this problem in python quickly using in built function difflib.get_close_matches().

How does difflib.get_close_matches() function work in Python ?
difflib.get_close_matches(word, possibilities, n, cutoff) accepts four parameters in which n, cutoff are optional. word is a sequence for which close matches are desired, possibilities is a list of sequences against which to match word. Optional argument n (default 3) is the maximum number of close matches to return, n must be greater than 0. Optional argument cutoff (default 0.6) is a float in the range [0, 1]. Possibilities that don’t score at least that similar to word are ignored.
The best (no more than n) matches among the possibilities are returned in a list, sorted by similarity score, most similar first.

filter_none
edit
play_arrow

brightness_4
# Function to find all close matches of  
# input string in given list of possible strings 
from difflib import get_close_matches 
  
def closeMatches(patterns, word): 
     print(get_close_matches(word, patterns)) 
  
# Driver program 
if __name__ == "__main__": 
    word = 'appel'
    patterns = ['ape', 'apple', 'peach', 'puppy'] 
    closeMatches(patterns, word) 
References : https://docs.python.org/2/library/difflib.html

Output:

['apple', 'ape']





#!/usr/bin/env python3

# Import json module
import json

# Define json data
customerData ="""{
    "id": "3425678",
    "name": "John Micheal",
    "email": "john@gmail.com",
    "type": "regular",
    "address": "4258 Poplar Chase Lane, Boise, Idaho."
}"""

# Input the key value that you want to search
keyVal = input("Enter a key value: \n")

# load the json data
customer = json.loads(customerData)
# Search the key value using 'in' operator
if keyVal in customer:
    # Print the success message and the value of the key
    print("%s is found in JSON data" %keyVal)
    print("The value of", keyVal,"is", customer[keyVal])
else:
    # Print the message if the value does not exist
    print("%s is not found in JSON data" %keyVal)
    
    
    
    
    
    Ask Question
Asked 8 years ago
Active 6 months ago
Viewed 4k times

8


1
How can I tell difflib.get_close_matches() to ignore case? I have a dictionary which has a defined format which includes capitalisation. However, the test string might have full capitalisation or no capitalisation, and these should be equivalent. The results need to be properly capitalised, however, so I can't use a modified dictionary.

import difflib

names = ['Acacia koa A.Gray var. latifolia (Benth.) H.St.John',
    'Acacia koa A.Gray var. waianaeensis H.St.John',
    'Acacia koaia Hillebr.',
    'Acacia kochii W.Fitzg. ex Ewart & Jean White',
    'Acacia kochii W.Fitzg.']
s = 'Acacia kochi W.Fitzg.'

# base case: proper capitalisation
print(difflib.get_close_matches(s,names,1,0.9))

# this should be equivalent from the perspective of my program
print(difflib.get_close_matches(s.upper(),names,1,0.9))

# this won't work because of the dictionary formatting
print(difflib.get_close_matches(s.upper().capitalize(),names,1,0.9))
Output:

['Acacia kochii W.Fitzg.']
[]
[]
Working code:

Based on Hugh Bothwell's answer, I have modified the code as follows to get a working solution (which should also work when more than one result is returned):

import difflib

names = ['Acacia koa A.Gray var. latifolia (Benth.) H.St.John',
    'Acacia koa A.Gray var. waianaeensis H.St.John',
    'Acacia koaia Hillebr.',
    'Acacia kochii W.Fitzg. ex Ewart & Jean White',
    'Acacia kochii W.Fitzg.']
test = {n.lower():n for n in names}    
s1 = 'Acacia kochi W.Fitzg.'   # base case
s2 = 'ACACIA KOCHI W.FITZG.'   # test case

results = [test[r] for r in difflib.get_close_matches(s1.lower(),test,1,0.9)]
results += [test[r] for r in difflib.get_close_matches(s2.lower(),test,1,0.9)]
print results
Output:

['Acacia kochii W.Fitzg.', 'Acacia kochii W.Fitzg.']
python difflib
share  improve this question  follow 
edited Jul 8 '12 at 18:04
asked Jul 8 '12 at 16:24

rudivonstaden
5,74544 gold badges2020 silver badges3333 bronze badges
Sorry to reboot an old post, but I found this interesting. For the final search product, I'm reading the code and it seems like you would not need the s1 and first results list. Is that correct? It seems the algorithm would produce the result you wanted without those lines. – Tyler Russell Dec 22 '17 at 0:59
@TylerRussell that's correct. The purpose was to verify that the capitalisation of the search term did not influence the result. The fact that searching with s1 and searching with s2 produced the same result showed that the algorithm worked. Generally you would only use one search term. – rudivonstaden Jan 9 '18 at 7:51
add a comment
3 Answers
Active
Oldest
Votes

9


I don't see any quick way to make difflib do case-insensitive comparison.

The quick-and-dirty solution seems to be

make a function that converts the string to some canonical form (for example: upper case, single spaced, no punctuation)

use that function to make a dict of {canonical string: original string} and a list of [canonical string]

run .get_close_matches against the canonical-string list, then plug the results through the dict to get the original strings back

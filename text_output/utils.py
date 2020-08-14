'''
That file contains functions for deleting the purity of words in the text
1. The conver function takes text arguments and returns a word dictionary and the number of repetitions of each word.
2. The function stat takes the dictionary of the frequency function conver and divides the list of words into three groups:
words whose frequency is repeated less than 2 times, more than or equal to 2 and less than exactly 5, and the third words that are repeated more than 6 times
'''
import re

def convert(text):
    frequency = {}
    pattern = re.findall(r'\b[A-a-Z-z]{2,20}\b', text)
    for word in pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1
    return frequency
def stat(frequency):
    fr1 = {}
    fr2 = {}
    fr3 = {}
    for word, value in frequency.items():
        if value < 2:
            fr1[word] = value
        if value >= 2 and value <= 5:
            fr2[word] = value
        if value > 6:
            fr3[word] = value
    return [fr1, fr2, fr3]

# Write a function called score_unigrams that takes three arguments:
#   - a path to a folder of training data 
#   - a path to a test file that has a sentence on each line
#   - a path to an output CSV file
#
# Your function should do the following:
#   - train a single unigram model on the combined contents of every .txt file
#     in the training folder
#   - for each sentence (line) in the test file, calculate the log unigram 
#     probability ysing the trained model (see the lab handout for details on log 
#     probabilities)
#   - write a single CSV file to the output path. The CSV file should have two
#     columns with headers, called "sentence" and "unigram_prob" respectively.
#     "sentence" should contain the original sentence and "unigram_prob" should
#     contain its unigram probabilities.
#
# Additional details:
#   - there is training data in the training_data folder consisting of the contents 
#     of three novels by Jane Austen: Emma, Sense and Sensibility, and Pride and Prejudice
#   - there is test data you can use in the test_data folder
#   - be sure that your code works properly for words that are not in the 
#     training data. One of the test sentences contains the words 'color' (American spelling)
#     and 'television', neither of which are in the Austen novels. You should record a log
#     probability of -inf (corresponding to probability 0) for this sentence.
#   - your code should be insensitive to case, both in the training and testing data
#   - both the training and testing files have already been tokenized. This means that
#     punctuation marks have been split off of words. All you need to do to use the
#     data is to split it on spaces, and you will have your list of unigram tokens.
#   - you should treat punctuation marks as though they are words.
#   - it's fine to reuse parts of your unigram implementation from HW3.

# You will need to use log and -inf here. 
# You can add any additional import statements you need here.
from math import log, inf
import os
import csv
from array import array

def score_unigrams(training="training_data/", test="test_data/test_sentences.txt", output="output.csv"):
    content = []
    for filename in os.listdir(training):
        f = os.path.join(training, filename)
        with open(f, 'r') as file:
            content += file.read().split()
    content = [x.lower() for x in content]
    d = {}
    total = len(content)
    for word in set(content):
        d[word] = log(content.count(word) / total)
    unigram_prob = []
    sent = []
    with open(test, 'r') as file_data:
        for line in file_data: 
            words = line.strip().split()
            words = [x.lower() for x in words]
            prob_list = []
            for word in words:
                prob_list.append(d.get(word, -inf))
            sent.append(line.strip()) 
            unigram_prob.append(sum(prob_list))
    tab = [{"sentence": s, "unigram_prob": p} for s, p in zip(sent, unigram_prob)]
    with open(output, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["sentence", "unigram_prob"])
        writer.writeheader()
        writer.writerows(tab) 

# Do not modify the following line
if __name__ == "__main__":
    # You can write code to test your function here
      score_unigrams()

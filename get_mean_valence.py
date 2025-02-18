# The file valence_data/winter_2016_senses_valence.csv contains data from an 
# experiment that asked people to provide valence ratings for words associated
# with each of the five senses (touch, taste, smell, sight, sound). The file has
# three columns: Word, Modality, and Val. Word contains the word, Modality the
# sensory modality, and Val contains the mean valence rating for that word,
# where higher valence corresponds to more positive emotional states.

# The question we'll try to answer is whether certain sensory modalities have 
# higher or lower mean valences than others.
# 
#  Write a function called get_mean_valence that takes a Path to a CSV file
#  as input. You can assume the file will be formatted as described above.
#  Your function should return a dictionary with keys corresponding to each
#  of the five modalities. The value for each key should be its mean valence
#  score across all of the words in the CSV file.

# The data are from the paper 
#
# Winter, B. (2016). Taste and smell words form an affectively loaded and emotionally
# flexible part of the English lexicon. Language, Cognition and Neuroscience, 31(8), 
# 975-988.
import csv

def get_mean_valence(file="valence_data/winter_2016_senses_valence.csv"):
    def mean(l1):
        avg = sum(l1)/len(l1)
        return avg
    data = []
    with open(file, "r") as f:
        data = [line.strip().split(",") for line in f]
    m_touch = []  #sorry for the hard coding
    m_taste = []
    m_smell = []
    m_sight = []
    m_sound = []
    for row in data:
        if row[1] == "Touch": m_touch.append(float(row[2]))
        elif row[1] == "Taste": m_taste.append(float(row[2]))
        elif row[1] == "Smell": m_smell.append(float(row[2]))
        elif row[1] == "Sight": m_sight.append(float(row[2]))
        elif row[1] == "Sound": m_sound.append(float(row[2]))
        else: continue 
    a = ['Touch', 'Taste', 'Smell', 'Sight', 'Sound']
    b = [mean(m_touch), mean(m_taste), mean(m_smell), mean(m_sight), mean(m_sound)]
    d = dict(zip(a, b))
    print(d)
    return d

# Do not modify the following line
if __name__ == "__main__":
    # You can write code to test your function here
    pass 

from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet as wn

#the user gives two phrases
phrase1 = raw_input("Write first phrase:")
phrase2 = raw_input("Write second phrase:")

#list to append every verb,noun and adjective
#phrase1
phrase1_words = []
str(phrase1_words)

#phrase2
phrase2_words = []
str(phrase2_words)

#Separate words and keep verbs,nous and adjectives
#phrase1
for word, pos in pos_tag(word_tokenize(phrase1)):
    if ((pos == "VB") or (pos == "VBD") or (pos == "VBG") or (pos == "VBN") or
    (pos == "VBP") or (pos == "VBP") or (pos == "VBP") or (pos == "VBZ") or
    (pos == "NN") or (pos == "NNS") or (pos == "NNP") or (pos == "NNPS") or
    (pos == "JJ") or (pos == "JJR") or (pos == "JJS")):
        phrase1_words.append(word)

#phrase2
for word, pos in pos_tag(word_tokenize(phrase2)):
    if ((pos == "VB") or (pos == "VBD") or (pos == "VBG") or (pos == "VBN") or
    (pos == "VBP") or (pos == "VBP") or (pos == "VBP") or (pos == "VBZ") or
    (pos == "NN") or (pos == "NNS") or (pos == "NNP") or (pos == "NNPS") or
    (pos == "JJ") or (pos == "JJR") or (pos == "JJS")):
        phrase2_words.append(word)

#compare each word of phrase1 with words from phrase2
similarity_sum = 0
for i in range(len(phrase1_words)):
    for j in range (len(phrase2_words)):
        verb1 = wn.synsets(phrase1_words[i])
        verb2 = wn.synsets(phrase2_words[j])
        s = verb1[0].wup_similarity(verb2[0])
        if s :
            similarity_sum += s

#average similarity of the two phrases is printed
average_sim = similarity_sum / (len(phrase1_words) + len(phrase2_words))
print "Average similarity of the two phrases is:", average_sim

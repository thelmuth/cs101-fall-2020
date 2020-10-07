import nltk
import random

NOUNS = ["dog", "person", "octopus", "platypus", "monkey", "computer", "chair",
         "cat", "juice", "book", "TV", "bacon", "egg", "Abraham Lincoln", "bagel"]

movie = "I like the movie Mr. & Mrs. Smith! Brad Pitt, Angelina Jolie, etc. are in it."

buses = "I will book the bus ticket while I bus the table and read a book."

def main():

    ### Get the parts of speach of a list of words
#     words2 = nltk.word_tokenize(movie)
#     pos = nltk.pos_tag(words2)
    
#     print(words2)
    
#     for word, word_pos in pos:
#         print(word, "-", word_pos)
    
    ### We can look up a specific tag
#     nltk.help.upenn_tagset("CC")

#     nltk.help.upenn_tagset()

    ### Let's make a function call to replace_nouns
#     result_sent = replace_nouns(buses, NOUNS)
#     print(result_sent)
#     
#     sent2 = replace_nouns(movie, ["apple", "banana", "cherry", "kiwi", "orange"])
#     print(sent2)

    ### Read each line of a file:
    filename = "PrideAndPrejudice.txt"
    f = open(filename, "r")
    
#     for line in f:
#         print(line + "====")

    pap = f.read()
    
#     print(pap[:10000])

#     output_repeated_words("I went to to the school for a lunch lunch meeting.")
    output_repeated_words(pap)

def output_repeated_words(text):
    """Prints any words in text that are repeated."""
    
    words = nltk.word_tokenize(text)
    
    for index in range(len(words) - 1):
        if words[index] == words[index + 1]:
            print(index, words[index])
        


def replace_nouns(text, nouns):
    """For each noun in text, replace it with a random noun from the list nouns."""
    
    words = nltk.word_tokenize(text)
    words_pos = nltk.pos_tag(words)
    
    new_sentence_list = []
    
    for word, pos in words_pos:
        
        if pos == "NN":
            new_word = random.choice(nouns)
            new_sentence_list.append(new_word)
        else:
            new_sentence_list.append(word)
            
#     print(new_sentence_list)
    
    ### This allows us to take a list of tokens and turn it back into a string
    twd = nltk.tokenize.treebank.TreebankWordDetokenizer()
    new_sentence = twd.detokenize(new_sentence_list)
            
    return new_sentence


if __name__ == "__main__":
    main()

import nltk

NOUNS = ["dog", "person", "octopus", "platypus", "monkey", "computer", "chair",
         "cat", "juice", "book", "TV", "bacon", "egg", "Abraham Lincoln", "bagel"]

movie = "I like the movie Mr. & Mrs. Smith! Brad Pitt, Angelina Jolie, etc. are in it."

buses = "I will book the bus ticket while I bus the table and read a book."

def main():

#     sents = naive_sentence_tokenizer(movie)
#     for sent in sents:
#         print(sent)

    ### NLTK's version of sentence tokenizing
#     sents = nltk.sent_tokenize(movie)
#     for sent in sents:
#         print(sent)

    ### NLTK's version of words tokenizing
#     words = nltk.word_tokenize(movie)
#     print(words)
    
    ### Get the parts of speach of a list of words
    words2 = nltk.word_tokenize(buses)
    pos = nltk.pos_tag(words2)
    
    for word, word_pos in pos:
        print("The part of speech for", word, "is", word_pos)


    ### We can display all of the parts of speech abreviations using this
    # nltk.help.upenn_tagset()
    
    ### We can look up a specific tag
#     nltk.help.upenn_tagset("DT")


def naive_sentence_tokenizer(text):
    """This will return the sentences in text as a list."""
    
    sentences = []
    current_sentence = ""
    
    for char in text:
        current_sentence += char
        
        if char in ".?!":
            sentences.append(current_sentence)
            current_sentence = ""
    
    return sentences





if __name__ == "__main__":
    main()

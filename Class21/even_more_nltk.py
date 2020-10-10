import nltk
import matplotlib.pyplot as plt

def main():

    ### Read each line of a file:
    filename = "PrideAndPrejudice.txt"
    f = open(filename, "r")

    pap = f.read()

#     output_repeated_words(pap)

    ### This finds all proper nouns
#     proper = find_proper_nouns(pap)
    
    ### The hard way of finding frequencies
#     proper_no_dups = remove_duplicates(proper)
#     proper_counts = get_counts(proper)
#     
#     print(proper_no_dups)
#     print(proper_counts)
#     
#     plt.bar(proper_no_dups, proper_counts)
#     plt.show()
    
    ### This way is easier to work with, and we can look at
    ### the most common things in our list of proper nouns.

#     fd = nltk.FreqDist(proper)
#     
#     ### Find the 20 most common words and their frequencies
#     common = fd.most_common(20)
#     print(common)
#     
#     ### We can use the FreqDist built-in plotting to see
#     ### the most common words plotted
#     fd.plot(20)

    
    ### We want to find sentences with 2 given characters in them
#     elizabeth_and_darcy = sentences_containing_both_targets(pap, "Elizabeth", "Darcy")
#     for sent in elizabeth_and_darcy:
#         print(sent)
    
#     jane_and_bingley = sentences_containing_both_targets(pap, "Jane", "Bingley")
#     for sent in jane_and_bingley:
#         print(sent)

#     cows = sentences_containing_both_targets(pap, "cow", "the")
#     for sent in cows:
#         print(sent)

    ### Want to show off scatter plots
    ### Write a function that finds the first letter and the length of every word
    ### Just look at first 10000 characters to make a more readable plot
    text = pap[:10000]

    (first_letters, lengths) = get_first_letters_and_lengths(text)
    
    ## Plot them!
    plt.scatter(first_letters, lengths)
    plt.show()
    

def get_first_letters_and_lengths(text):
    """Returns a list containing the first letter of each word and
    a list containing the length of each word."""
    
    words = nltk.word_tokenize(text)
    
    lengths = []
    first_letters = []
    for word in words:
        first_letter = word[0].lower()
        first_letters.append(first_letter)
        lengths.append(len(word))
        
    return (first_letters, lengths)
    
    
    
def sentences_containing_both_targets(text, target1, target2):
    """Returns a list of sentences that contain words target1 and target2"""
    
    sentences = nltk.sent_tokenize(text)
    found_sentences = []
    
    for sent in sentences:
        if (target1 in sent) and (target2 in sent):
            found_sentences.append(sent)
    
        ### Bad:
#         if target1 and target2 in sent:
    
    return found_sentences
    
    
def find_proper_nouns(text):
    """Find and return a list of all proper nouns in text."""
    
    words = nltk.word_tokenize(text)
    words_pos = nltk.pos_tag(words)
    
    all_proper_nouns = []
    
    for word, pos in words_pos:
        if pos == "NNP":
            all_proper_nouns.append(word)
            
    return all_proper_nouns




def output_repeated_words(text):
    """Prints any words in text that are repeated."""
    
    words = nltk.word_tokenize(text)
    
    for index in range(len(words) - 1):
        if words[index] == words[index + 1]:
            print(index, words[index])
        




#######################
## The following two functions students coded in lab, so we're just using them

def remove_duplicates(list_with_dupes):
    """ Returns the given list with all duplicates removed. """
    
    clean_list = []
    
    for entry in list_with_dupes:
        if entry not in clean_list:
            clean_list.append(entry)
            
    return clean_list


def get_counts(list_to_count):
    """ Returns a frequency list corresponding to the given list. """
    
    freq_list = []
    clean_list = remove_duplicates(list_to_count)
    
    for entry_a in clean_list:
        count = 0
        for entry_b in list_to_count:
            if entry_b == entry_a:
                count += 1
        freq_list.append(count)
    
    return freq_list


if __name__ == "__main__":
    main()

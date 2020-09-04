
def main():

    tweet = "Computer Science #rules #python #comptuerscience"    
    index = tweet.find("#")
    space_index = tweet.find(" ", index)
    hashtag = tweet[index : space_index]
    print(hashtag)

# These two lines of code should appear at the bottom in all your programs
if __name__ == "__main__":
    main()

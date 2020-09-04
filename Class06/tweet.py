
def main():

    tweet = "this tweet ends in a #hashtag"
    index = tweet.find("#")
    print("index = ", index)
    space_index = tweet.find(" ", index)
    print("space_index = ", space_index)
    hashtag = tweet[index : space_index]
    print(hashtag)

# These two lines of code should appear at the bottom in all your programs
if __name__ == "__main__":
    main()


# input | output
# "Computer Science #rules #python #comptuerscience" | "#rules"
# "#animals #cat #dog #emu" | "#animals"
# "this tweet has no hashtag" | ""
# "this tweet ends in a #hashtag" | "#hashtag"
# "this is weird # yes it is" | "#"
# "" | ""


# 1
# Take names from a list and produce one, comma-separated string
# names = ["Elsa", "Anna", "Olaf", "Kristoff", "Sven"]
# frozen = ""
# for name in names:
#     frozen = frozen + name + ", "
#     
# print(frozen)

# 2
# Same thing, but no comma after Sven
# names = ["Elsa", "Anna", "Olaf", "Kristoff", "Sven", "Harry", "Ron"]
# frozen = ""
# for name in names[:-1]:
#     frozen = frozen + name + ", "
# 
# frozen = frozen + names[-1]
# print(frozen)

# 3
# Nested loops
# for ch in "hello":
#     for x in range(5):
#         print(ch, x)


# 4
# If statements
# divisor = float(input("Enter a number to divide 1 by: "))
# if divisor == 0.0:
#     print("You can't divide by zero!!!")
# else:
#     print("1 divided by", divisor, "is", 1 / divisor)
    
## Same thing, but with not equals
# divisor = float(input("Enter a number to divide 1 by: "))
# if divisor != 0.0:
#     print("1 divided by", divisor, "is", 1 / divisor)
# else:
#     print("You can't divide by zero!!!")


# 5
# Turn a word into Pig Latin
# word = input("Enter a word: ")
# ### if word[0] == "a" or word[0] == "e" .....
# if word[0] in "aeiouAEIOU":
#     pig_latin = word + "ay"
# else:
#     pig_latin = word[1:] + word[0] + "ay"
# print(word, "in Pig Latin is", pig_latin)

# 6
# Use if statements to do something in a loop some of the time
# for number in range(10):
#     if number % 2 == 0:
#         print(number, "is even!")

# 7
## User enters name. We want to print only the vowels in their name
# name = input("Enter your name: ")
# for ch in name:
#     if ch in "aeiouAEIOU":
#         print(ch)

# vowels = ""
# name = input("Enter your name: ")
# for ch in name:
#     if ch in "aeiouAEIOU":
#         vowels += ch    # equivalent to vowels = vowels + ch
# 
# print(vowels)

# consonants = ""
# name = input("Enter your name: ")
# for ch in name:
#     if not ch in "aeiouAEIOU":
#         consonants += ch    # equivalent to vowels = vowels + ch
# 
# print(consonants)

consonants = ""
name = input("Enter your name: ")
for ch in name:
    if ch in "aeiouAEIOU":
        #consonants += ch
        pass
    else:
        consonants += ch

print(consonants)




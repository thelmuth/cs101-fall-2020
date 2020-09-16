### We want to change every period in a user's input into an exclamation point!

# text = input("Enter some sentences: ")
# new_text = ""
# for char in text:
#     if char == ".":
#         new_text += "!"
#     else:
#         new_text += char
# 
# print(new_text)


### We want to get only the digits out of a user's entered SSN
# input_ssn = input("Enter your SSN: ")
# ssn = ""
# for char in input_ssn:
#     if char in "0123456789":
#         ssn += char
# 
# print("The cleaned SSN is:", ssn)


    


### We want to find the longest string in the list
# names = ["Charlie", "Caroline", "Charlotte", "Cathy", "Cody", "Carol", "Chad", "Cat"]
# longest = ""
# for name in names:
#     if name > longest:
#         longest = name
#     
# print(longest)


### elif allows you to have more than 2 conditions


grade = 78

if grade >= 90:
    print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")





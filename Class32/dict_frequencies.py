"""
Simple example of using a dictionary to count frequencies of characters
in a string.
"""

def main():
    
#     student = {"first_name": "Kendra",
#                "last_name": "Alonzo",
#                "year": 2018,
#                "major": "history"
#                }
#     
#     ### We need to know that the order of this list is
#     ### first_name, last_name, year, major
#     student_list = ["Kendra", "Alonzo", 2018, "history"]
#     
#     print(student)
#     
#     print("the value associated with year is", student.pop("year"))
#     
#     print(student)
#     
#     print("the value associated with major is", student["major"])
#     
#     print(student)
#     print()
#     
#     ### Looping over dictionary:
#     for key in student:
#         print(key, "=>", student[key])
    
    text = input("Enter some text: ")
    
    ### Use a dictionary to store how frequently each character appears.
    ### Keys: characters
    ### Values: each character's frequency
    frequencies = {}
    
    for char in text:
        ### This checks if char is a _key_ in frequencies
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
            
    for char in frequencies:
        print(char, "=>", frequencies[char])
    
    

if __name__ == "__main__":
    main()
    
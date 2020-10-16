"""
CSVs allow us to store a spreadsheet in a way that is readable by Python.
The csv module allows us to work with CSV files.

Imagine we have a CSV full of quiz and exam scores.
Average quiz grade is worth 40% of the grade for the class.
Average exam grade is worth 60% of the grade for the class.

We want to calculate the final grade for each student, print them,
and find the highest grade in the class.
"""

import csv

def main():
    
    file = open("cs010grades.csv", "r")
    reader = csv.reader(file)
    
    ### This is how you iterate over the rows in a CSV file:
#     for row in reader:
#         print(row)

    ### To read and skip the header row:
    header = next(reader, None)
    
    name_best = ""
    grade_best = 0
    
    for row in reader:
        
        name = row[0]
        quizzes = row[1:11] ## Note: we need indices 1-10 inclusive, so go to 11
        ## quizzes is a list of __strings__
        exams = row[11:]
    
        average_quiz_grade = average_list_of_strings(quizzes)
        average_exam_grade = average_list_of_strings(exams)
        
        final_grade = 0.4 * average_quiz_grade + 0.6 * average_exam_grade
        
        print(name, "has a final grade of", round(final_grade, 2))
        
        if final_grade > grade_best:
            name_best = name
            grade_best = final_grade
            
    print()
    print("The student with the highest grade is", name_best)
    print("They achieved a grade of", grade_best)
        
    

def average_list_of_strings(number_strings):
    """Takes a list of strings representing numbers, converts them to integers,
    and finds their average."""
    
    total = 0
    for num_string in number_strings:
        total += int(num_string)

    return total / len(number_strings)

if __name__ == "__main__":
    main()
    
# Ana Robles
# CIS129
# Module 11 Lab Exercises 9.1, 9.2, and 9.3
# 4/15/2024
# This program is for inputting grades, calculating the average and recording the data.

import csv

def main():
    # Part 1: Writing grades to a text file
    print('Enter any number of grades (-1 to quit)') 
    file = open("grades.txt",'w') 
    while True: 
        grade = int(input()) 
        if grade == -1: 
            break 
        else: 
            file.writelines(f'{grade}\n') 
    file.close()

    # Part 2: Reading grades from the text file
    grades = None  
    with open('grades.txt', 'r') as file:
        grades = file.readlines()

    total = 0  
    for grade in grades:
        grade = int(grade.strip())
        print(grade)
        total += int(grade)

    print(f"Total: {total}")
    print(f"Count: {len(grades)}")
    print(f"Average: {total / len(grades) : .2f}")

    # Part 3: Storing student data in a CSV file
    n = int(input("Enter the number of students: "))
    rows = [["First Name", "Last Name", "Exam 1 Grade", "Exam 2 Grade", "Exam 3 Grade"]]
    for i in range(n):
        first = input("\nEnter First Name of Student " + str(i + 1) + ": ")
        last = input("Enter Last Name of Student " + str(i + 1) + ": ")
        ex1 = int(input("Enter Exam 1 Grade of Student " + str(i + 1) + ": "))
        ex2 = int(input("Enter Exam 2 Grade of Student " + str(i + 1) + ": "))
        ex3 = int(input("Enter Exam 3 Grade of Student " + str(i + 1) + ": "))
        rows.append([first, last, ex1, ex2, ex3])

    with open("grades.csv", 'w', newline='') as _file:
        file = csv.writer(_file)
        for i in rows:
            file.writerow(i)
        print("\nWriting Done.\n")

    with open("grades.csv", 'r') as _file:
        file = csv.reader(_file)
        header = next(file)
        for i in file:
            i[2] = int(i[2])
            i[3] = int(i[3])
            i[4] = int(i[4])
            print(i)

# Call the main function to execute all parts of the code
main()
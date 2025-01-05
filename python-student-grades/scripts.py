# import csv module to read grades.csv
import csv 
# import built-in statistics module to do calculations
import statistics
# import nan from math module
from math import nan

# initialize empty lists to hold subject scores
math_scores = []
science_scores = []
english_scores = []

# Calculate the average grade for each subject across all students.
  # function called subject_average that will take a file as a parameter and use the data to calculate the average scores for each subject
def subject_average(filename):
# opens file in read mode
  with open(filename, 'r') as subjects:
    # reader object will read/iterate over the file
    data = csv.reader(subjects)
    # skips the first line of the file - header row
    heading = next(data)

    for row in data:
      # append the scores to the respective lists
      # try/except block for error handling; if a value cannot be converted to an integer, it will be set to NaN to represent missing/invalid data
      try:
        math_scores.append(nan)
      except ValueError:
        math_scores.append(float(nan))
      try:
        science_scores.append(int(row[2]))
      except ValueError:
        science_scores.append(float(nan))
      try:
        english_scores.append(int(row[3]))
      except ValueError:
        english_scores.append(float(nan))

    # calculate the average scores for each subject
    print('Average math grade is: {}'.format(statistics.mean(math_scores))) # returns 84
    print(f"Average science grade is: {statistics.mean(science_scores)}") # returns 0 bc of invalid data
    print(f"Average english grade is: {statistics.mean(english_scores)}") # returns 91.2 

# call the function with the file name
subject_average('grades.csv')

# Find the student(s) with the highest overall grade (average of all three subjects).
def highest_overall_grade(filename):
    with open(filename, 'r') as students:
      data = csv.reader(students)
      heading = next(data)

# initialize an empty dictionary to store student names and their average grades
      student_grades = {}
      # iterate over the data

      for row in data:
          # calculate the average grade for each student
        try:
          # converts each grade to an integer and calulates the average using statistics module
          student_grades[row[0]] = statistics.mean((int(row[1])) + (int(row[2])) + (int(row[3])))
          # if any error occurs, the average is set to 0
        except ValueError:
          student_grades[row[0]] = 0

      # find the student with the highest average grade
      # max function will return the key with the highest value
      highest_grade = max(student_grades, key=student_grades.get) 
      print(f"The student with the highest overall grade is: {highest_grade}")

# call the function with the file name
highest_overall_grade('grades.csv')

# Determine which subject has the highest average grade overall.

# Create a simple report that summarizes these findings.
# Use Python's string formatting capabilities to present the results in a readable format.


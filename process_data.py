import csv
from utils import calculate_average, assign_grade

def process_grades():
    students = []
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            name, history, geography, spanish = row
            average = calculate_average([int(history), int(geography), int(spanish)])
            grade = assign_grade(average)
            students.append([name, average, grade])

    with open('student_results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Average', 'Grade'])
        writer.writerows(students)
    print('Results saved to student_results.csv')

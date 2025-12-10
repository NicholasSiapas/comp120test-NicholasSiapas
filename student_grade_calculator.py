#!/usr/bin/env python3
"""
Student Grade Calculator
A simple program demonstrating fundamental programming concepts
including functions, data structures, loops, and conditional logic.

Author: Nicholas Siapas
Course: COMP120 - Final Test
"""


def calculate_average(grades):
    """
    Calculate the average of a list of grades.
    
    Args:
        grades (list): List of numerical grades
    
    Returns:
        float: Average grade, or 0 if list is empty
    """
    if not grades:
        return 0
    return sum(grades) / len(grades)


def get_letter_grade(average):
    """
    Convert numerical average to letter grade.
    
    Args:
        average (float): Numerical grade average
    
    Returns:
        str: Letter grade (A, B, C, D, or F)
    """
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'


def display_student_report(name, grades):
    """
    Display a formatted report for a student.
    
    Args:
        name (str): Student name
        grades (list): List of grades
    """
    print(f"\n{'=' * 50}")
    print(f"Student Report for: {name}")
    print(f"{'=' * 50}")
    
    if not grades:
        print("No grades recorded.")
        return
    
    print(f"Grades: {', '.join(map(str, grades))}")
    print(f"Number of assignments: {len(grades)}")
    
    average = calculate_average(grades)
    letter_grade = get_letter_grade(average)
    
    print(f"Average: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"{'=' * 50}\n")


def main():
    """
    Main function to demonstrate the student grade calculator.
    """
    print("=" * 50)
    print("Student Grade Calculator - COMP120 Final Test")
    print("=" * 50)
    
    # Sample student data
    students = {
        "Alice Johnson": [85, 92, 88, 90, 87],
        "Bob Smith": [78, 82, 75, 80, 79],
        "Carol Davis": [95, 98, 96, 94, 97],
        "David Lee": [65, 70, 68, 72, 69],
        "Eve Martinez": [55, 58, 52, 60, 56]
    }
    
    # Process and display reports for each student
    for student_name, student_grades in students.items():
        display_student_report(student_name, student_grades)
    
    # Calculate class statistics
    all_grades = []
    for grades in students.values():
        all_grades.extend(grades)
    
    class_average = calculate_average(all_grades)
    
    print(f"{'=' * 50}")
    print(f"Class Statistics")
    print(f"{'=' * 50}")
    print(f"Total students: {len(students)}")
    print(f"Total assignments graded: {len(all_grades)}")
    print(f"Class average: {class_average:.2f}")
    print(f"Overall letter grade: {get_letter_grade(class_average)}")
    print(f"{'=' * 50}")


if __name__ == "__main__":
    main()

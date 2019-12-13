"""
Utilities to calculate SPI, CPI, display the grades,
and convert CPI to GPA.
"""


import json
import argparse
from globals import *


def calculate_spi(grades, semester_id, gpm=GRADE_POINT_MAPPING):
    """Caluculates S.P.I for semester_id

    Arguments:
        grades (dict):
            Dictionary containing grades
        semester_id (int):
            ID of semester to calculate S.P.I for
        gpm (dict):
            Maps grades to points 0-10

    Returns:
        spi (double):
            S.P.I for the semester corresponding to semester_id
    """
    grades = grades[semester_id]
    credits = 0
    grade_points = 0

    for course, course_info in grades.items():
        if course not in CR2_COURSES:
            credits += course_info["credits"]
            grade_points += course_info["credits"] * gpm[course_info["grade"]]

    spi = grade_points / credits
    return spi


def calculate_cpi(grades, gpm=GRADE_POINT_MAPPING):
    """Calculates the C.P.I

    Arguments:
        grades (dict):
            Dictionary containing grades
        gpm (dict):
            Maps grades to points 0-10

    Returns:
        cpi (double):
            C.P.I across semesters
    """
    grade_points = 0
    credits = 0
    for semester in grades:
        for course, course_info in grades[semester].items():
            if course not in CR2_COURSES:
                credits += course_info["credits"]
                grade_points += course_info["credits"] * gpm[course_info["grade"]]

    cpi = grade_points / credits
    return cpi


def display(grades, metadata):
    """Displays per semester grades

    Arguments:
        grades (dict):
            Dictionary containing grades
        metadata (dict):
            Dictionary containing metadata mapping course codes
            to course names
    """
    print('Displaying transcript:')
    print('')
    for semester, courses in metadata.items():
        semester_grades = grades[semester]
        print(semester)
        for course_id, course_info in semester_grades.items():
            course_name = courses[course_id]
            course_credits = course_info["credits"]
            course_grade = course_info["grade"]
            gap = ' ' * (50 - len(course_name))
            print(f'{course_name}{gap}{course_credits}\t{course_grade}')
        print('')


def convert_to_gpa(grades, glm=GRADE_LETTER_MAPPING, lpm=LETTER_POINT_MAPPING):
    """Converts C.P.I (scale of 10) to G.P.A (scake of 4)

    Arguments:
        grades (dict):
            Dictionary containing grades
        glm (dict):
            Maps grades to grade labels
        lpm (dict):
            Maps grade letters to points 2-4
    """
    grade_points = 0
    credits = 0
    for semester in grades:
        for course, course_info in grades[semester].items():
            if course not in CR2_COURSES:
                credits += course_info["credits"]
                grade_points += course_info["credits"] * lpm[glm[course_info["grade"]]]

    gpa = grade_points / credits
    return gpa



if __name__ == "__main__":
    with open('assets/grades.json') as jgrades:
        grades = json.load(jgrades)

    with open('assets/metadata.json') as jmeta:
        metadata = json.load(jmeta)

    parser = argparse.ArgumentParser(
                'Grade Conversion Utilities')

    parser.add_argument('-d', dest='display', type=bool,
                        help='Display transcript')
    parser.add_argument('--spi', dest='spi', type=bool,
                        help='Calculate SPI')
    parser.add_argument('--cpi', dest='cpi', type=bool,
                        help='Calculate CPI')
    parser.add_argument('--id', dest='_id', type=int,
                        help="Semester ID to calculate SPI.\
                        Required with -s argument")
    parser.add_argument('-c', dest='convert', type=bool,
                        help='Convert CPI to GPA')

    args = parser.parse_args()

    if args.display:
        display(grades, metadata)

    if args.spi:
        if args._id:
            spi = calculate_spi(grades, int(args._id))
            print(f'S.P.I for Semester {args._id} is: {spi}')
        else:
            print('--id argument is required.')

    if args.cpi:
        cpi = calculate_cpi(grades)
        print(f'C.P.I is: {cpi}')

    if args.convert:
        gpa = convert_to_gpa(grades)
        print(f'Corresponding GPA is: {gpa}')

"""
Contains global variables which are used in different scripts
in the repository.

Grades given at Indian Institute of Information Technology Vadodara
correspond to percentages as a multiple of 10, i.e, 
                AA corresponds to 100%,
                AB corresponds to 90%,
                BB corresponds to 80%,
                BC corresponds to 70%,
                CC corresponds to 60%,
                CD corresponds to 50%,
                DD corresponds to 40%.

According to WES Evaluation Agency, Gradung Scale in India is equivalent
to the U.S Grade in the following way:

        ---------------------------------------------
        |       SCALE   |   U.S. GRADE EQUIVALENT   |
        ---------------------------------------------
        |   70 - 100    |           A               |
        |   50 - 69     |           B               |
        |   35* - 49    |           C               |
        |   0 - 32      |           F               |
        ---------------------------------------------

Link: https://applications.wes.org/country-resources/resources.asp
"""


GRADE_POINT_MAPPING = {
    "AA": 10,
    "AB": 9,
    "BB": 8,
    "BC": 7,
    "CC": 6,
    "CD": 5,
    "DD": 4,
}

GRADE_LETTER_MAPPING = {
    "AA": "A",
    "AB": "A",
    "BB": "A",
    "BC": "B",
    "CC": "B",
    "CD": "C",
    "DD": "C",
}

LETTER_POINT_MAPPING = {
    'A': 4,
    'B': 3,
    'C': 2,
}

CR2_COURSES = [
    'HM101',
    'PC301',
    'HM401',
    'PC303',
]

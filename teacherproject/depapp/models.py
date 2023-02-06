
from django.db import models

# Create your models here.

SCIENCE = ' Science'
COMMERCE = ' Commerce'
ECONOMICS ='Economics'
PSYCOLOGY ='Psycology'
BIOCHEMISTRY = 'Biochemistry'




S_1 = 'Mathematics'
S_2 = 'Data Science'
S_3 = 'Software Engineering'
S_4 = 'Physics'
S_5 = 'Database Management'
C_1 = 'Accountant'
C_2 = 'Financial Analyst'
C_3 = 'Bachelor Of Commerce'
C_4 = 'BBA'
C_5 = 'Chartered Accountancy'
E_1 = 'Micro Economics'
E_2 = 'Macro Economics'
E_3 = 'Statistics'
E_4 = 'Econometrics'
E_5 = 'International Trade'
P_1 ='Modern Applied Psycology'
P_2 = 'Forensic Psycology'
P_3 = 'Child Psycology'
B_1 = 'Environmental Studies'
B_2 = 'Biomolecules'
B_3 = 'Human Physiology'





SUBJECT_CHOICES = [
    (SCIENCE, SCIENCE),
    (COMMERCE, COMMERCE),
    (ECONOMICS,ECONOMICS),
    (PSYCOLOGY,PSYCOLOGY),
    (BIOCHEMISTRY,BIOCHEMISTRY),
]

JOB_CHOICES = [
    (S_1, S_1),
    (S_2, S_2),
    (S_3, S_3),
    (S_4, S_4),
    (S_5, S_5),
    (C_1, C_1),
    (C_2, C_2),
    (C_3, C_3),
    (C_4, C_4),
    (C_5, C_5),
    (E_1,E_1),
    (E_2,E_2),
    (E_3,E_3),
    (E_4,E_4),
    (E_5,E_5),
    (P_1,P_1),
    (P_2,P_2),
    (P_3,P_3),
    (B_1,B_1),
    (B_2,B_2),
    (B_3,B_3),
]

def get_s_strings():
    s_strings = [
        S_1,
        S_2,
        S_3,
        S_4,
        S_5,
    ]

    return s_strings


def get_c_strings():
    c_strings = [
        C_1,
        C_2,
        C_3,
        C_4,
        C_5,
    ]

    return c_strings

def get_e_strings():
    e_strings = [
        E_1,
        E_2,
        E_3,
        E_4,
        E_5,
    ]

    return e_strings
def get_p_strings():
    p_strings = [
        P_1,
        P_2,
        P_3,
    ]

    return p_strings
def get_b_strings():
    b_strings = [
        B_1,
        B_2,
        B_3,
    ]

    return b_strings



class Person(models.Model):
    # id_name
    # name = models.CharField(max_length=50)
    # id_department
    department = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    # id_courses
    courses = models.CharField(max_length=50, choices=JOB_CHOICES)
from django.db import models

# Create your models here.

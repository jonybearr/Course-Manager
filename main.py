from testRequirements import *


#data loading
import csv


with open("userInputs/courses.csv",newline='') as userInput:
    reader=csv.reader(userInput,delimiter=',')
    rawUserCoursesTable=list(reader)
with open('requirements/mech_requirements.csv', newline='') as requirements:
    reader = csv.reader(requirements, delimiter=',')
    requirementsTable=list(reader)


output=testRequirement(rawUserCoursesTable,requirementsTable)
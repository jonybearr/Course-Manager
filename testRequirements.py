
#data loading
import csv

with open('mech_requirements.csv', newline='') as requirements:
    with open("courses.csv",newline='') as userInput:

        requirementsTable = csv.reader(requirements, delimiter=',')
        userCourses=csv.reader(userInput,delimiter=',')

        for row in requirementsTable:

            print(row)
        for row in userCourses:
            print(row)

        #loop through requirementsTable
            #check if required courses exist within userTable
                #if exist, 

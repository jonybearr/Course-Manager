
#data loading
import csv


with open("userInputs/courses.csv",newline='') as userInput:
    reader=csv.reader(userInput,delimiter=',')
    rawUserCoursesTable=list(reader)
with open('requirements/mech_requirements.csv', newline='') as requirements:
    reader = csv.reader(requirements, delimiter=',')
    requirementsTable=list(reader)


#process rawusercourses to get a list only of taken courses
takenCourses=[]
for row in rawUserCoursesTable:
        takenCourses.append(row[1])
print('taken Courses')
print(takenCourses)


#create output list with length requirementsTable
output=[]

#loop through requirementsTable
for row in requirementsTable:
    #check if required courses exist within userTable
        requiredClasses=row[2:]
        print('requiredClasses')
        print(requiredClasses)
        requirementDetails=[]
        for course in requiredClasses:
            #if the course is a row number, add the output list value of the row number
            if(course.isnumeric()):
                 requirementDetails.append(output[int(course)])
            
            #else process normally
            else:
                #if it exists in user's courses, add 1 to requirementDetails list
                if(course in takenCourses):
                        requirementDetails.append(1)
                else:
                        requirementDetails.append(0)
        print('requirement details')
        print(requirementDetails)
    #if requirements met, update output list value with 1, else output list value 0
    
    #process and or logic
        if row[0]=="OR":
            if(1 in requirementDetails):
                output.append(1)
            else:
                output.append(0)
        elif row[0]=="AND":
            if(0 in requirementDetails):
                output.append(0)
            else:
                output.append(1)
                
        
#loop through output list and set values that have hide in requirementsTable to -1
#calculate requirements and report missing requirements
print('output results: criterium met')
print(output)

print('hi')
for i in range(len(requirementsTable)):
     print(requirementsTable[i][1])
     if(requirementsTable[i][1]=='HIDE'):
          output[i]=-1

print('updated output')
print(output)

for i in range(len(output)):
     if(output[i]==0):
          print('missing requirements')
          print(requirementsTable[i])
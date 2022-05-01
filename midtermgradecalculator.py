'''
==========================================================================================

Title:    Midterm Grade Calculator
Author:   Angelica Kusik
Date:     November 03, 2021
Description:
  A simple Python application that will prompt the user to enter a student's grades
  for a number of assignments and the program will calculate the average grade for each 
  category of assignment as well as the student's midterm weighted grade.

===========================================================================================
'''
########### IMPORTS ############
import numpy as np

######## CONSTANTS DECLARATION ##########
#Constants that will hold the number of assignments in the Class Exercises, Pre-Class Exercises
# and Labs categories:
CLASS_EXERCISES_UPPERBOUND = 6
PRE_CLASS_ASSIGNMENTS_UPPERBOUND = 4
LABS_UPPERBOUND = 2

#Constants that will hold the total weight of Class Exercises, Pre-Class Exercises,
# Labs categories and Academic Integrity Workshop:
CLASS_EXERCISES_WORTH = 0.15
PRE_CLASS_ASSIGNMENTS_WORTH = 0.12
LABS_WORTH = 0.16
ACADEMIC_INTEGRITY_WORKSHOP_WORTH = 0.01

#Constants that will hold the minimum and maximum grades for each assignment:
MIN_VALUE = 0
MAX_VALUE = 100 

########### VARIABLES DECLARATION ############

#For this application most variables are being declared inside the while loop that
#allows the user to enter grades for multiples student's.
# The variables were declare inside the loop because they need to be zeroed before 
#in order to produce accurate results after each run.

#Variable to indicate whether the user wants to continue or not
continue_processing = True

# The loop will run for as long as the user wants to continue using the program
while continue_processing:

    #Arrays that will hold the grade inputs for all Class Exercises, Pre-Class Exercises
    # and Labs categories:
    class_exercises_array = list()
    pre_class_assignment_array = list()
    labs_array = list()

    #Array that will hold the average grades from all categories
    average_grades_array = list()

    #Array that will hold the weight from all categories
    grades_weight_array = list()

    #Variables that will hold the grade average for the Class Exercises, Pre-Class Exercises
    # and Labs categories: :
    average_class_exercises= 0.0
    average_pre_class_assignment = 0.0
    average_labs = 0.0

    #Variable that will hold the academic integrity workshop grade:
    academic_integrity_grade = 0.0

    #Variable that will hold the final value of the student's midterm grade:
    midterm_grade = 0.0

    #Variables that will hold the name of each assignment category
    first_assignment_category = 'Class Exercise'
    second_assignment_category = 'Pre-Class Assignment'
    third_assignment_category = 'Lab'
    fourth_assignment_category = 'Academic Integrity Workshop'

    ########### INPUT ############
    
    #Print program title
    print('\n=====================================================================')
    print('\n                   MIDTERM GRADE CALCULATOR                          ')
    print('\n=====================================================================')

    #Iteration loop that will run up to the tota number of Class Exercises ollect the grades for all 
    #assignments in this category
    for count in range(CLASS_EXERCISES_UPPERBOUND):

        #The input_validated flag will determine when the while loop in the sequence will end.
        input_validated = False
        #We store the messages to be prompt to the user in a variable, so we can adjust the message latter on as needed.
        input_message = '\nPlease enter grade of ' + first_assignment_category + ' ' + str(count+1) + ' : '

        #We create a boolean expression that will run until a valid user input is entered by the user.
        while not input_validated:

            #We will validate the user input to ensure it is a float. If the user input cannot be stored
            #as a float we will display an error message and ask user for a valid input.
            try:
                user_input = float(input(input_message))

                #If user input can be stored as a float, we will check if it is in the required range.
                #If input is in the range, store input in the Class Exercise array
                if MIN_VALUE <= user_input <= MAX_VALUE:
                    class_exercises_array.append(user_input)
                    
                    #If all validations succeed, we set input_validated to True to end this loop and carry on.
                    input_validated = True
                
                #If input is not in the range we display not-in-the-range error message and ask user for new input.
                else:
                    input_message = 'Grade must be in the range of ' + str(MIN_VALUE) + ' and ' + str(MAX_VALUE) + '. Please try again: '
            #If float validation fail display not-numeric-value error message and prompt user for new input.
            except:
                input_message = '\nGrade must be a numeric value. Please try again: '
    #Iteration loop will run up to the total number of Pre-Class Assignments to collect grade
    #input from the user for all assignments in this category.
    for count in range(PRE_CLASS_ASSIGNMENTS_UPPERBOUND):
        #Here again we use a flag to determine when the loop must end
        input_validated = False
        input_message = '\nPlease enter grade of ' + second_assignment_category + ' ' + str(count+1) + ' : '
        #We validate the user input to ensure that program only proceed to processing when a valid input is entered.
        while not input_validated:
            #Validate input to ensure it is a float
            try:
                user_input = float(input(input_message))
                #If float validation succeed, check if input is in the required range
                if MIN_VALUE <= user_input <= MAX_VALUE:
                    pre_class_assignment_array.append(user_input)
                    #If input is in the range we stored the value in the pre class array and set input validated flag to tru to 
                    #end the loop.
                    input_validated = True
                #If range validation fail, display not-in-the-range error message and prompt user for new input
                else:
                    input_message = 'Grade must be in the range of ' + str(MIN_VALUE) + ' and ' + str(MAX_VALUE) + '. Please try again: '
            #If float validation fail, display invalid-data-type error message and prompt user for new input.
            except:
                input_message = '\nGrade must be a numeric value. Please try again: '
    #Iteration loop will run up to the total number of Labs to collect grade
    #input from the user for all assignments in this category.
    for count in range(LABS_UPPERBOUND):
        #Here again we use a flag to determine when the loop must end
        input_validated = False
        input_message = '\nPlease enter grade of ' + third_assignment_category + ' ' + str(count+1) + ' : '
        #We validate the user input to ensure that program only proceed to processing when a valid input is entered.
        while not input_validated:
            #Validate input to ensure it is a float
            try:
                user_input = float(input(input_message))
                #If float validation succeed, check if input is in the required range
                if MIN_VALUE <= user_input <= MAX_VALUE:
                    labs_array.append(user_input)
                    #If input is in the range we stored the value in the lab array and set input validated flag to tru to 
                    #end the loop.
                    input_validated = True
                #If range validation fail, display not-in-the-range error message and prompt user for new input
                else:
                    input_message = 'Grade must be in the range of ' + str(MIN_VALUE) + ' and ' + str(MAX_VALUE) + '. Please try again: '
            #If float validation fail, display invalid-data-type error message and prompt user for new input.
            except:
                input_message = '\nGrade must be a numeric value. Please try again: '
    #Create a flag to determine the end of the while loop in the sequence and set it to False
    input_validated = False
    #Here again we store the input message in a variable
    input_message = '\nDid the student submit the ' + fourth_assignment_category + ' ? (yes/no):  '
    #Validate user input
    while not input_validated:
        #Prompt user for yes or no answer
        user_input = str(input(input_message)).lower()
        #If input == yes, set academic integrity grade variable to MAX VALUE and flag to True to end loop
        if user_input == 'yes':
            academic_integrity_grade = MAX_VALUE
            input_validated = True
        #If input == no set academic integrity grade variable to MIN VALUE and set flag to True to end loop
        else:
            if user_input == 'no':
                academic_integrity_grade = MIN_VALUE
                input_validated = True
            #If input is not == to yes or no, display invalid-answer error message and prompt user for new input.
            else:
                input_message = 'Answer must be yes or no. Please try again: '

    ########### PROCESS ############

    # Calculate the Class Exercises average grade and insert the value in the average grades array
    average_class_exercises = sum(class_exercises_array) / len(class_exercises_array)
    average_grades_array.append(average_class_exercises)

    # Calculate the Pre-Class Assignments average grade and insert the value in the average grades array
    average_pre_class_assignment = sum(pre_class_assignment_array) / len(pre_class_assignment_array)
    average_grades_array.append(average_pre_class_assignment)

    # Calculate the Labs average grade and insert the value in the average grades array
    average_labs = sum(labs_array) / len(labs_array)
    average_grades_array.append(average_labs)

    # We don't have to calculate the average grade for the Academic Integrity Workshop because
    #we only have one assignment in this category, which the grade will be either 0 or 100, so
    # we just add the variable academic integrity grade to the average grades array.
    average_grades_array.append(academic_integrity_grade)

    # Insert the weight for each assignment category in a array following the same order in which
    #the average grades were inserted in the average grades array.

    grades_weight_array.append(CLASS_EXERCISES_WORTH)
    grades_weight_array.append(PRE_CLASS_ASSIGNMENTS_WORTH)
    grades_weight_array.append(LABS_WORTH)
    grades_weight_array.append(ACADEMIC_INTEGRITY_WORKSHOP_WORTH)

    # Calculate the weighted midterm grade

    # Using numpy calculate de weighted midterm grade and store in the variable midterm grade
    midterm_grade = np.average(average_grades_array, weights=grades_weight_array)

    ########### OUTPUT ############

    # Print the title as follows 
    print('\n=====================================================================')
    print('\n                           YOUR GRADES ARE:                          ')
    print('\n=====================================================================')

    # Print student's average grades per category of assignment
    print('\n             Midterm Grade Average per Category                ')
    print('\n  ' + first_assignment_category + '  ' + second_assignment_category + '    ' + third_assignment_category + '    ' + fourth_assignment_category)
    print('\n       {:.2f}            {:.2f}          {:.2f}             {:.2f}       '.format(average_class_exercises, average_pre_class_assignment, average_labs, average_academic_integrity_workshop))
                
    # Print student's midterm grade
    print('\n\nThe student’s midterm grade for the Intro to Programming course is ' + ' {:.2f}.'.format(midterm_grade,))

    #Prompt user to enter grades for another student or end application
    #Set new value to input message variable
    input_message = '\nWould you like to enter grades for another student? (yes/no) '
    #Create a flag that will determine when the while loop in the sequence must end and set it to False.
    continue_program = False
    #Create a loop that will run until a validade input is entered.
    while not continue_program:
        #Prompt user for yes or no input
        new_user_input = input(input_message).lower()
        #If input == yes set continue program flag to True to end this loop and continue processing to 
        #True to restart program
        if new_user_input == 'yes':
            continue_processing = True
            continue_program = True
        #If input == no set continue program flag to True to end this loop and continue processing flag
        #to False to end program
        else:
            if new_user_input == 'no':
                continue_processing = False
                continue_program = True
            #If input is not == to yes or no set continue program flag to False to repeat this loop and prompt
            #user to enter a valid answer. Set continue processing flag to true to restar program if user enter
            #select yes in the new input.
            else:
                continue_program = False
                continue_processing = True



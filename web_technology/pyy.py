# student grade checker 

#student grade checker
# accept the input from the user for name and roll number.

# use list to store multiple student detail
# use three subject and accept the grade
# print all the student with their grade
#     Note: >=80%=1st divistion
#     >=60%&<80%=2nd division


def grade_check():
    # first take input as name from user
    name = input("enter your name : ")
    roll_number = int(input("enter your rollnumber : "))
    student_details = ( name, roll_number)

    sub = ["math","science"]
    
    d = {}
    for subject in sub :
        marks = int(input(f"enter your marks in {subject} : "))
        d[subject] = marks
    
    value = sum(d.values())
    percentage = value / len(sub)
    
    if percentage > 80 :
        print(" you got 1st division")
    else :
        print(" you got 2nd division")


    print(f"the is the value of dic{d}")
    print(f"His name is {name}, and his roll number is {roll_number}.")
   
    
grade_check()


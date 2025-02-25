gpa = 0
credit = 0

def calc(letter):
    if letter[0] == 'A':
        grade = 4
    elif letter[0] == 'B':
        grade = 3
    elif letter[0] == 'C':
        grade = 2
    elif letter[0] == 'D':
        grade = 1
    else:
        grade = 0 
    
    if len(letter) > 1 and letter[1] == '+': 
        grade += 0.5
    
    return grade

total_grade_points = 0  
for _ in range(20):  
    course = input().split(" ")
    if course[2] != "P": 
        course_credit = float(course[1])  
        grade = calc(course[2])  
        credit += course_credit  
        total_grade_points += grade * course_credit  

if credit == 0:
    print("0.00")
else:
    print(f"{total_grade_points / credit:.6f}")

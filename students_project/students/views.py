import random
from django.shortcuts import render
def make_dict(request):
    random_names = ['James Ramirez', 'Aiden Peterson', 'Noah White', 'Daniel Allen', 'Elijah Rodriguez',               
    'Ava Lee', 'Benjamin Mitchell', 'Ethan Martin', 'Benjamin Adams', 'Oliver Adams', 
    'Scarlett Phillips', 'Aiden Carter', 'Isabella Morris', 'Robert Jackson', 'Michael Anderson', 
    'Samuel Baker', 'Benjamin Rodriguez', 'Samuel Flores', 'Lucas White', 'James Allen', 
    'Ella Roberts', 'Logan Lee', 'Matthew Young', 'Noah Collins', 'David Young', 
    'Logan Anderson', 'Jackson Smith', 'Ella Smith', 'Michael Young', 'Alexander Stewart', 
    'Emily Nguyen', 'Penelope Carter', 'Penelope Green', 'Chris Edwards', 'Chloe Harris', 
    'Elijah Taylor', 'Isabella Mitchell', 'Sophia Nelson', 'Evelyn Green', 'Mason Carter', 
    'Oliver Flores', 'Madison Campbell', 'Sophia Brown', 'Chris Thompson', 'Robert Green', 
    'Lily Thomas', 'Harper Collins', 'John Baker', 'Anna Murphy', 'Isabella Parker', 
    'Alexander Hall', 'Robert Rogers', 'Daniel Campbell', 'Oliver Parker', 'Daniel Evans', 
    'John Taylor', 'Ava Flores', 'Charlotte Mitchell', 'Scarlett Morris', 'Benjamin Taylor', 
    'John Wright', 'Sarah Taylor', 'David Jackson', 'David Evans', 'Emily Baker', 
    'Jacob Phillips', 'Chris Nelson', 'Samuel Lee', 'Jane Robinson', 'Abigail Thomas', 
    'Matthew Scott', 'Aria Johnson', 'Chris Adams', 'Chris Ramirez', 'Luna Cook', 
    'Liam Parker', 'Noah Scott', 'Jane Rodriguez', 'Benjamin White', 'Emily Phillips', 
    'Olivia Campbell', 'Penelope Stewart', 'Noah Johnson', 'Mason Brown', 'Isabella Baker', 
    'Benjamin Stewart', 'Logan Rogers', 'John Jackson', 'Harper Morris', 'Charlotte Green', 
    'Sophia Martin', 'Robert Taylor', 'Ava Campbell', 'Sophia Rogers', 'Amelia Edwards', 
    'Abigail Evans', 'Luna Young', 'Chris Garcia', 'Sophia Campbell', 'Abigail Evans']
    students_dict = {}
    incount = 0
    while incount <= 100:
        incount += 1
        random_name = random.choice(random_names)
        students_dict.update({random_name : {}})
    return render(request, 'students_page.html', {'students_dict' : students_dict})




def student_profiles(random_names):
    students_dict = make_dict(random_names)
    for student_name in students_dict.keys():
        splitted_name = student_name.split()
        random_gpa = random.randint(1, 4)
        courselist = ['python', 'java', 'lua', 'c++']
        random_course = random.choice(courselist)
        firstname = splitted_name[0]
        lastname = splitted_name[1]
        students_dict[student_name].update({'name': firstname, 'last_name': lastname, 'gpa': random_gpa, 'course': random_course})
    return students_dict

def get_random_student(request):
    random_names = ['James Ramirez', 'Aiden Peterson', 'Noah White', 'Daniel Allen', 'Elijah Rodriguez',               
    'Ava Lee', 'Benjamin Mitchell', 'Ethan Martin', 'Benjamin Adams', 'Oliver Adams', 
    'Scarlett Phillips', 'Aiden Carter', 'Isabella Morris', 'Robert Jackson', 'Michael Anderson', 
    'Samuel Baker', 'Benjamin Rodriguez', 'Samuel Flores', 'Lucas White', 'James Allen', 
    'Ella Roberts', 'Logan Lee', 'Matthew Young', 'Noah Collins', 'David Young', 
    'Logan Anderson', 'Jackson Smith', 'Ella Smith', 'Michael Young', 'Alexander Stewart', 
    'Emily Nguyen', 'Penelope Carter', 'Penelope Green', 'Chris Edwards', 'Chloe Harris', 
    'Elijah Taylor', 'Isabella Mitchell', 'Sophia Nelson', 'Evelyn Green', 'Mason Carter', 
    'Oliver Flores', 'Madison Campbell', 'Sophia Brown', 'Chris Thompson', 'Robert Green', 
    'Lily Thomas', 'Harper Collins', 'John Baker', 'Anna Murphy', 'Isabella Parker', 
    'Alexander Hall', 'Robert Rogers', 'Daniel Campbell', 'Oliver Parker', 'Daniel Evans', 
    'John Taylor', 'Ava Flores', 'Charlotte Mitchell', 'Scarlett Morris', 'Benjamin Taylor', 
    'John Wright', 'Sarah Taylor', 'David Jackson', 'David Evans', 'Emily Baker', 
    'Jacob Phillips', 'Chris Nelson', 'Samuel Lee', 'Jane Robinson', 'Abigail Thomas', 
    'Matthew Scott', 'Aria Johnson', 'Chris Adams', 'Chris Ramirez', 'Luna Cook', 
    'Liam Parker', 'Noah Scott', 'Jane Rodriguez', 'Benjamin White', 'Emily Phillips', 
    'Olivia Campbell', 'Penelope Stewart', 'Noah Johnson', 'Mason Brown', 'Isabella Baker', 
    'Benjamin Stewart', 'Logan Rogers', 'John Jackson', 'Harper Morris', 'Charlotte Green', 
    'Sophia Martin', 'Robert Taylor', 'Ava Campbell', 'Sophia Rogers', 'Amelia Edwards', 
    'Abigail Evans', 'Luna Young', 'Chris Garcia', 'Sophia Campbell', 'Abigail Evans']
    student_dict = student_profiles(random_names)
    students = student_dict.keys()
    student_list = []
    for student in students:
        student_list.append(student)
    random_student = random.choice(student_list)
    gpa = student_dict[random_student]['gpa']
    course = student_dict[random_student]['course']
    random_student_profile = {
        'student' : random_student,
        'gpa' : gpa,
        'course' : course,
    }
    return render(request, 'main_page.html', {'random_student_profile': random_student_profile})


def students(request):
    random_names = ['James Ramirez', 'Aiden Peterson', 'Noah White', 'Daniel Allen', 'Elijah Rodriguez',               
    'Ava Lee', 'Benjamin Mitchell', 'Ethan Martin', 'Benjamin Adams', 'Oliver Adams', 
    'Scarlett Phillips', 'Aiden Carter', 'Isabella Morris', 'Robert Jackson', 'Michael Anderson', 
    'Samuel Baker', 'Benjamin Rodriguez', 'Samuel Flores', 'Lucas White', 'James Allen', 
    'Ella Roberts', 'Logan Lee', 'Matthew Young', 'Noah Collins', 'David Young', 
    'Logan Anderson', 'Jackson Smith', 'Ella Smith', 'Michael Young', 'Alexander Stewart', 
    'Emily Nguyen', 'Penelope Carter', 'Penelope Green', 'Chris Edwards', 'Chloe Harris', 
    'Elijah Taylor', 'Isabella Mitchell', 'Sophia Nelson', 'Evelyn Green', 'Mason Carter', 
    'Oliver Flores', 'Madison Campbell', 'Sophia Brown', 'Chris Thompson', 'Robert Green', 
    'Lily Thomas', 'Harper Collins', 'John Baker', 'Anna Murphy', 'Isabella Parker', 
    'Alexander Hall', 'Robert Rogers', 'Daniel Campbell', 'Oliver Parker', 'Daniel Evans', 
    'John Taylor', 'Ava Flores', 'Charlotte Mitchell', 'Scarlett Morris', 'Benjamin Taylor', 
    'John Wright', 'Sarah Taylor', 'David Jackson', 'David Evans', 'Emily Baker', 
    'Jacob Phillips', 'Chris Nelson', 'Samuel Lee', 'Jane Robinson', 'Abigail Thomas', 
    'Matthew Scott', 'Aria Johnson', 'Chris Adams', 'Chris Ramirez', 'Luna Cook', 
    'Liam Parker', 'Noah Scott', 'Jane Rodriguez', 'Benjamin White', 'Emily Phillips', 
    'Olivia Campbell', 'Penelope Stewart', 'Noah Johnson', 'Mason Brown', 'Isabella Baker', 
    'Benjamin Stewart', 'Logan Rogers', 'John Jackson', 'Harper Morris', 'Charlotte Green', 
    'Sophia Martin', 'Robert Taylor', 'Ava Campbell', 'Sophia Rogers', 'Amelia Edwards', 
    'Abigail Evans', 'Luna Young', 'Chris Garcia', 'Sophia Campbell', 'Abigail Evans']
    students_profile = student_profiles(random_names)
    return render(request, 'students_page.html', {'students_profile' : students_profile})
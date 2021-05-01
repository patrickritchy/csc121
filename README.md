# csc121
_______________________________________________________________________

	CSC121	PYTHON Programming
_______________________________________________________________________


Group Project
Objectives

In this project, students will learn:
- How to create modules and functions
- How to pass data from one function to another
- How to store data in lists
- How to create and use selection control structures
- How to create and use iterative control structures
- How to add comments to Python code
Goals

In this project, students will demonstrate the abilities to:
- Create modules and functions
- Pass data from one function to another
- Store data in lists
- Create and use selection control structures
- Create and use iterative control structures
- Add comments to Python code
Project Description

You have learned quite a lot about the basics of Python programming.  In this project, you will integrate what you have learned to develop a larger program.

This program creates a class registration system.  It allows students to log in to add courses, drop courses and list courses they have registered for.

This program has 5 functions in 2 modules: a student module and a main module.

You must define the following functions in the student module.



Function
Specification
add_course(id, c_list, r_list, m_list)
This function adds a student to a course.  It has four parameters: id is the ID of the student to be added; c_list is the list of courses offered; r_list is the list of class rosters; m_list is the list of maximum class sizes.  This function asks user to enter the course he/she wants to add.  If the course is not offered, display error message and stop.  If the course is full, display error message and stop.  If student already registered for the course, display error message and stop.  Add student ID to the course’s roster and display a message if there is no problem.  This function has no return value.
drop_course(id, c_list, r_list)
This function drops a student from a course.  It has three parameters: id is the ID of the student to be dropped; c_list is the list of courses offered; r_list is the list of class rosters. This function asks user to enter the course he/she wants to drop.  If the course is not offered, display error message and stop.  If the student is not enrolled in that course, display error message and stop.  Remove student ID from the course’s roster and display a message if there is no problem.  This function has no return value.
list_courses(id, c_list, r_list)
This function displays and counts courses a student has registered for.  It has three parameters: id is the ID of the student; c_list is the list of courses offered; r_list is the list of class rosters. This function displays the number of courses the student has registered for and which courses they are.  This function has no return value.


You must define the following functions in the main module.

Function
Specification
login(id, s_list)
This function allows a student to log in.  It has two parameters: id and s_list, which is the student list. This function asks user to enter PIN. If the ID and PIN combination is in s_list, display message of verification and return True.  Otherwise, display error message and return False.
main()
This function manages the whole registration system.  It has no parameter.  It creates 4 lists to store data: student list, course list, maximum class size list and roster list.  It uses a loop to serve multiple students.  Inside the loop, ask user to enter ID, and call the login function to verify student’s identity.  If login is successful, use a loop to allow student choose to add courses, drop courses or list courses the student has registered for. This function has no return value.



This program uses a few lists to store data. To make grading easier, data will be added to these lists at the beginning of the main function.

student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
course_list = ['CSC101', 'CSC102', 'CSC103']
max_size_list = [3, 2, 1]
roster_list = [['1004', '1003'], ['1001'], ['1002']]
There are 4 students in this program.  ID and PIN of students are stored as tuples in student_list.  The first element of each tuple is student ID, while the second element is PIN.

Three courses are offered.  The course codes are stored in course_list.  These courses are CSC101, CSC102 and CSC103.

The maximum class size of the courses offered are stored in max_size_list.  The max sizes of CSC101, CSC102 and CSC103 are 3, 2 and 1, respectively.

Rosters of the three classes offered are stored as three lists, which are three elements of roster_list, which is actually a list of lists.  Students 1004 and 1003 are enrolled in CSC101.  Student 1001 is enrolled in CSC102.  Student 1002 is enrolled in CSC103.

The program should have a loop to create multiple student sessions.  In each session, ask user to enter ID, then call the login function to verify the student’s identity.  If login is successful, use a loop to allow the student to add courses, drop courses and list courses registered.

The following is an example.

Enter ID to log in, or 0 to quit: 1234
Enter PIN: 123
ID or PIN incorrect

Enter ID to log in, or 0 to quit: 1001
Enter PIN: 111
ID and PIN verified

Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: 1
Enter course you want to add: CSC121
Course not found

Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: 1
Enter course you want to add: CSC102
You are already enrolled in that course.

Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: 1
Enter course you want to add: CSC103
Course already full.

Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: 1
Enter course you want to add: CSC101
Course added

Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: 2
Enter course you want to drop: CSC121
Course not found

Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: 2
Enter course you want to drop: CSC103
You are not enrolled in that course.

Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: 2
Enter course you want to drop: CSC102
Course dropped

Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: 3
Courses registered:
CSC101
Total number: 1

Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: 1
Enter course you want to add: CSC102
Course added

Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: 3
Courses registered:
CSC101
CSC102
Total number: 2

Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: 0
Session ended.

Enter ID to log in, or 0 to quit: 1002
Enter PIN: 222
ID and PIN verified

Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: 3
Courses registered:
CSC103
Total number: 1

Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: 1
Enter course you want to add: CSC101
Course already full.

Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: 1
Enter course you want to add: CSC102
Course added

Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: 3
Courses registered:
CSC102
CSC103
Total number: 2

Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: 0
Session ended.

Enter ID to log in, or 0 to quit: 0
Format

Unless otherwise arranged, you will be part of a group of 4 students to do this project. I will randomly group you.


Submission Requirements

Choose 1 person in the group that will submit the project. This person must submit:

Student module Python file
Main module Python file
MS Word Information/Feedback document (group effort):
Describe how the work was distributed (e.g. who did what?)
Demonstrate your program to show that it works
  Did you encounter any difficulties and how you overcame them
What you have learned from this experience

Personal peer review document

Each person in the group must submit their personal peer review document as well.
Grading Rubric

Defining and using main function [14 points]
Defining and using login function [14 points]
Defining and using add_course function [14 points]
Defining and using drop_course function [14 points]
Defining and using list_courses function [14 points]
Project presentation [10 points]
Peer evaluation [20 points]



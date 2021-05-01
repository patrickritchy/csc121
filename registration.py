# ----------------------------------------------------------------
# Author:
# Date:
#
# This program creates a class registration system.  It allows
# students to add courses, drop courses and list courses they are
# registered for.
# -----------------------------------------------------------------

import student


def main():
    # ------------------------------------------------------------
    # This function manages the whole registration system.  It has
    # no parameter.  It creates student list, course list,
    # max class size list and roster list.  It uses a loop to serve
    # multiple students. Inside the loop, ask student to enter ID,
    # and call the login function to verify student's identity. Then
    # let student choose to add course, drop course or list courses.
    # This function has no return value.
    # -------------------------------------------------------------

    student_list = [('1001', '111'), ('1002', '222'), ('1003', '333'), ('1004', '444')]
    course_list = ['CSC101', 'CSC102', 'CSC103']
    roster_list = [['1004', '1003'], ['1001'], ['1002']]
    max_size_list = [3, 2, 1]
    while True:
        student_id = input("Enter ID to log in, or 0 to quit: ")
        student_id.upper().strip()
        if student_id == "0":
            exit()
        if login(student_id, student_list):
            print("ID and PIN verified")
            print("")
            while True:
                course_action = input("Enter 1 to add course, 2 to drop course, 3 to list courses, 0 to exit: ")
                if course_action == "1":
                    student.add_course(student_id, course_list, roster_list, max_size_list)
                elif course_action == "2":
                    student.drop_course(student_id, course_list, roster_list)
                    # print(roster_list)
                elif course_action == "3":
                    student.list_courses(student_id, course_list, roster_list)
                elif course_action == "0":
                    print("Session ended.")
                    print("")
                    break
                else:
                    print("Invalid option")
                    print("")
        else:
            print("ID or PIN incorrect")
            print("")
            continue




def login(id, s_list):
    # ------------------------------------------------------------
    # This function allows a student to log in.
    # It has two parameters: id and s_list, which is the student
    # list. This function asks user to enter PIN. If the ID and PIN
    # combination is in s_list, display message of verification and
    # return True. Otherwise, display error message and return False.
    # -------------------------------------------------------------
    pin_number = input("Enter PIN: ")
    for s in s_list:
        if id == s[0] and pin_number == s[1]:
            return True
    return False


if __name__ == '__main__':
    try:
        main()
    except ValueError:
        print("There was a problem with your input")
    else:
        print("Thank you, come again")

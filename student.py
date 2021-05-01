def list_courses(id, c_list, r_list):
    # ------------------------------------------------------------
    # This function displays and counts courses a student has
    # registered for.  It has three parameters: id is the ID of the
    # student; c_list is the course list; r_list is the list of
    # class rosters. This function has no return value.
    # -------------------------------------------------------------
    print("Courses registered:")
    num_courses = 0
    for course in c_list:
        c_index = c_list.index(course)
        # print(course, str(c_index))
        if id in r_list[c_index]:
            num_courses = num_courses + 1
            print(course)
    print("Total number:", num_courses)
    print("")

def add_course(id, c_list, r_list, m_list):
    # ------------------------------------------------------------
    # This function adds a student to a course.  It has four
    # parameters: id is the ID of the student to be added; c_list
    # is the course list; r_list is the list of class rosters;
    # m_list is the list of maximum class sizes.  This function
    # asks user to enter the course he/she wants to add.  If the
    # course is not offered, display error message and stop.
    # If the course is full, display error message and stop.
    # If student has already registered for this course, display
    # error message and stop.  Add student ID to the course’s
    # roster and display a message if there is no problem.  This
    # function has no return value.
    # -------------------------------------------------------------

    while True:
        course_to_add = input("Enter course you want to add: ")
        course_to_add = course_to_add.upper().strip()
        if course_to_add not in c_list:
            print("Course not found")
            print("")
            break
        elif course_to_add in c_list:
            c_index = c_list.index(course_to_add)
            course = r_list[c_index]
            max_size = m_list[c_index]
            if id not in course:
                if len(course) >= max_size:
                    print("Course already full.")
                    print("")
                else:
                    course.append(id)
                    print("Course added")
                    print("")
                break
            else:
                print("You are already enrolled in that course.")
                print("")
                break


def drop_course(id, c_list, r_list):
    # ------------------------------------------------------------
    # This function drops a student from a course.  It has three
    # parameters: id is the ID of the student to be dropped;
    # c_list is the course list; r_list is the list of class
    # rosters. This function asks user to enter the course he/she
    # wants to drop.  If the course is not offered, display error
    # message and stop.  If the student is not enrolled in that
    # course, display error message and stop. Remove student ID
    # from the course’s roster and display a message if there is
    # no problem.  This function has no return value.
    # -------------------------------------------------------------

    while True:
        course_to_drop = input("Enter course you want to drop: ")
        course_to_drop = course_to_drop.upper().strip()
        if course_to_drop not in c_list:
            print("Course not found")
        elif course_to_drop in c_list:
            c_index = c_list.index(course_to_drop)
            course = r_list[c_index]
            if id in course:
                course.remove(id)
                print("Course dropped")
                print("")
                break
            else:
                print("You are not enrolled in that course.")
                print("")
                break

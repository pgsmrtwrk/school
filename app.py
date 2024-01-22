# Import classes from school.py
from school import Admin, Subject, Teacher, Student
from functions import seed_data, get_user_roles, get_new_object_details, get_object_list, get_object_assignment, display_object_list, display_object_details, get_lesson_details, get_object_by_name, return_to_menu

# Create permissions as a dictionary of Tuples because it should be immutable
permissions = {"Init": ("Start"), "Admin": ("Create Admin", "Create Teacher", "Create Student", "Create Subject", "View list of Admins", "View list of Teachers", "View list of Students", "View list of Subjects", "View Admin details", "View Teacher details", "View Student details", "View Subject details", "Assign Teacher to Subject", "Enrol student", "Log out", "Exit"), "Teacher": ("Deliver lesson", "Set test", "Grade Test", "Log out", "Exit"), "Student": ("Attend lesson", "Submit test", "Get grades", "Log out", "Exit")}

# Seed user for each role
seed_data()

# Initialise role and user variables for startup
role = "Init"
action_index = "0"

while permissions[role][int(action_index)] != "Exit":
    # Re-initialise user and role variables on Log Out
    role = "Init"
    active_user = ""
    temp_user_list = []
    action_index = "0"

    print(" ***   ***  *  *   **    **   *   ")
    print("*     *     *  *  *  *  *  *  *   ")
    print(" **   *     ****  *  *  *  *  *   ")
    print("   *  *     *  *  *  *  *  *  *   ")
    print("***    ***  *  *   **    **   ****")

    print("\nWelcome to the School Administrator App.")
    print("\nLet's start by identifying you.\n")

    # Request user role
    roles = get_user_roles()
    while role not in roles:
        print("\nType the name of you user role from the list below:")
        print(roles)
        role = input()
        if role not in roles:
            print("\nRole not in list. Please try again.\n")

    # Use a list comprehension to get a list of users in selected role
    temp_user_list = get_object_list(role)
    
    while active_user not in temp_user_list:
        print("\nThank you. Please enter your name from the list below:")
        print(temp_user_list)
        active_user = input()
        if active_user not in temp_user_list:
            print("\nUser not in list. Please try again.\n")

    print("\nWelcome {name}!".format(name = active_user)) 

    while permissions[role][int(action_index)] not in ["Log out", "Exit"]:
        
        # Present menu items based on role permissions
        print("\nAs a {role}, what would you like to do next?\n ".format(role = role))
        for permission in permissions[role]:
            print(str(permissions[role].index(permission)) + ". " + permission)
        action_index = input("\nSelect an index from the list above: ")

        match permissions[role][int(action_index)]: 
            
            case "Create Admin":
                get_new_object_details("Admin")

            case "Create Teacher":
                get_new_object_details("Teacher")

            case "Create Student":
                get_new_object_details("Student")
            
            case "Create Subject":
                get_new_object_details("Subject")

            case "View list of Teachers":
                display_object_list("Teacher")

            case "View list of Admins":
                display_object_list("Admin")
            
            case "View list of Students":
                display_object_list("Student")
            
            case "View list of Subjects":
                display_object_list("Subject")

            case "View Admin details":
                display_object_details("Admin")
            
            case "View Teacher details":
                display_object_details("Teacher")

            case "View Student details":
                display_object_details("Student")

            case "View Subject details":
                display_object_details("Subject")
            
            case "Assign Teacher to Subject":
                subject, teacher  = get_object_assignment("Subject", "Teacher") 

                # Call the 'assign_teacher' method on the current instance of the Subject class with the Teacher object as a parameter
                subject.assign_teacher(teacher)

                # Pause to allow user to determine timing of return to main menu
                return_to_menu()
            
            case "Enrol student":
                subject, student  = get_object_assignment("Subject", "Student")

                # Call the 'enrol_student' method with the student parameter on the subject object
                subject.enrol_student(student)

                # Pause to allow user to determine timing of return to main menu
                return_to_menu()

            case "Deliver lesson":
                teacher, subject_taught, lesson_date = get_lesson_details("Teacher", active_user)
                
                # Call the 'deliver_lesson' method with subject and lesson data on the teacher object
                teacher.deliver_lesson(subject_taught, lesson_date)

                # Pause to allow user to determine timing of return to main menu
                return_to_menu()
            
            case "Attend lesson":
                student, subject_attended, lesson_date = get_lesson_details("Student", active_user)
                
                # Call the 'attend_lesson' method with subject and lesson data on the teacher object
                student.attend_lesson(subject_attended, lesson_date)

                # Pause to allow user to determine timing of return to main menu
                return_to_menu()

from school import Admin, Teacher, Student, Subject
#from app import user_list

# Initialise empty object lists
user_list = {"Admin": [], "Teacher": [], "Student": []}
subject_list = []

def seed_data():
    user_list["Admin"].append(Admin("Paul"))
    user_list["Teacher"].append(Teacher("Elsa", 8))
    user_list["Student"].append(Student("Amy"))
    subject_list.append(Subject("Maths", 100))

def return_to_menu():
    return_to_menu = "N"
    # Pause to allow user to determine timing of return to main menu
    while return_to_menu.upper() != "Y":
        return_to_menu = input("\nReturn to main menu (Y/N)?: ")

def get_user_roles():
    return list(user_list.keys())

def get_object_list(object_class):
    match object_class:
        case "Admin" | "Teacher" | "Student":
            return [obj.name for obj in user_list[object_class]]
        case "Subject":
            return [obj.name for obj in subject_list]

def get_assigned_object_list(recipient_object, assigned_class):
    full_assigned_list = get_object_list(assigned_class)
    match assigned_class:
        case "Student":
            return [assigned for assigned in get_object_list(assigned_class) if assigned in recipient_object.students]
        case "Teacher":
            return [assigned for assigned in get_object_list(assigned_class) if assigned in recipient_object.teacher]

def get_not_assigned_object_list(recipient_object, assigned_class):
    full_assigned_list = get_object_list(assigned_class)
    match assigned_class:
        case "Student":
            return [assigned for assigned in get_object_list(assigned_class) if assigned not in recipient_object.students]
        case "Teacher":
            return [assigned for assigned in get_object_list(assigned_class) if assigned not in recipient_object.teacher]

def get_lesson_details(role, active_user):
    # Initialise variables
    subject_lesson = ""
    lesson_date = ""
    
    # Use a list comprehension to get the Teacher object for the active user
    object_in_lesson = get_object_by_name(role, active_user)

    match role:
        case "Teacher":
            lesson_role = "teach"
            lesson_role_past = "taught"
            subjects_assigned = object_in_lesson.subjects_taught
            enforce_date_in_lesson_list = False
        
        case "Student":
            lesson_role = "attend"
            lesson_role_past = "attended"
            subjects_assigned = object_in_lesson.subjects_enrolled
            enforce_date_in_lesson_list = True
    
    # Display the list of Subjects currently taught by the Teacher
    print("\nThe Subjects you are currently assigned to " + lesson_role + " are as follows:")
    print(subjects_assigned)
    
    # Gather data on the Subject the Teacher delivered a lesson for
    while subject_lesson not in subjects_assigned:
        subject_lesson = input("\nEnter the name of the Subject you " + lesson_role_past + " a lesson for: ")
        if subject_lesson not in subjects_assigned:
            print("\nThe Subject you entered in not on the list. Please try again")
    
    # Use a list comprehension to get the Subject object the Teacher is delivering a lesson for
    subject_object = get_object_by_name("Subject", subject_lesson)

    # Gather data for the lesson date (string)
    if enforce_date_in_lesson_list:
        lesson_list = [dates for dates in subject_object.lessons_delivered[subject_object.teacher]]
        print("\nThe lessons delivered for " + subject_object.name + " are as follows:")
        print(lesson_list)
        
        while lesson_date not in lesson_list:
            lesson_date = input("\nEnter the date [yyyy-mm-dd] you " + lesson_role_past + " the lesson: ")
            if lesson_date not in lesson_list:
                print("\nThe date you entered is not in the list. Please try again.")
    else:
        lesson_date = input("\nEnter the date [yyyy-mm-dd] you " + lesson_role_past + " the lesson: ")

    return object_in_lesson, subject_object, lesson_date


def display_object_list(object_class):
    object_list = get_object_list(object_class)
    print("\nThe current list of " + object_class + "s is as follows:")
    print(object_list)

    # Pause to allow user to determine timing of return to main menu
    return_to_menu()

def display_object_details(object_class):
    object_name = ""
    object_list = get_object_list(object_class)
    print("\nThe current list of " + object_class + "s is as follows:")
    print(object_list)

    # Gather & verify data
    while object_name not in object_list:
        object_name = input("\nEnter the name of the " + object_class + " you would like to view: ")
        if object_name not in object_list:
            print("\nThe " + object_class + " you entered is not on the list. Please try again.")
    
    # Use a list comprehension to retrieve the Teacher object from the user_list
    object_itself = get_object_by_name(object_class, object_name)
    print(object_itself)

    # Pause to allow user to determine timing of return to main menu
    return_to_menu()

def get_new_object_details(object_class):
    
    # Initialise new user
    new_object = ["<name>"]
    
    # Use list comprehension to create list of strings for display
    print_list("current", object_class, get_object_list(object_class))
    
    # Get new user details from active user
    match object_class:
        
        case "Admin" | "Student":
            # Gather data, create new Admin object and append to user_list
            new_object[0] = input("\nEnter the name of the new " + object_class + " user: ")
        
        case "Teacher":
            # Gather data, create new Teacher object and append to user_list
            new_object[0] = input("\nEnter the name of the new Teacher: ")
            new_object[1] = input("How many years has this teacher been teaching?: ")
        
        case "Subject":
            new_object[0] = input("\nEnter the name of the new Subject: ")
            new_object[1] = input("How many credits is the subject worth?: ")
    
    append_object_list(object_class, new_object)

    # Refresh list of strings for display
    print_list("updated", object_class, get_object_list(object_class))

    # Pause to allow user to determine timing of return to main menu
    return_to_menu()

def print_list(list_status, object, list):
    print("\nThe " + list_status + " list of " + object + "s is as follows:")
    print(list)

def append_object_list(object_class, arguments):
    match object_class: 
        case "Admin":
            user_list["Admin"].append(Admin(arguments[0]))
        case "Teacher":
            user_list["Teacher"].append(Teacher(arguments[0], arguments[1]))
        case "Student":
            user_list["Student"].append(Student(arguments[0]))
        case "Subject":
            subject_list.append(Subject(arguments[0], arguments[1]))

def get_object_by_name(object_class, name):
    match object_class:
        case "Admin" | "Teacher" | "Student":
            return next(obj for obj in user_list[object_class] if obj.name == name)
        case "Subject":
            return next(obj for obj in subject_list if obj.name == name)
        
def get_object_assignment(recipient, assigned):
    # Initialise variables
    recipient_name = ""
    assigned_name = ""
    
    # Get the full list of candidate recipients from the recipient class
    recipient_list = get_object_list(recipient)
    print_list("current", recipient, recipient_list)

    # Gather data for recipient to receive an assigned object
    while recipient_name not in recipient_list:
        recipient_name = input("\nEnter the name of the " + recipient + " to assign a " + assigned + ": ")
        if recipient_name not in recipient_list:
            print("\nThe " + recipient + " you entered is not on the list. Please try again.")
    
    # Retrieve the specific recipient object to receive an assignment
    recipient_object = get_object_by_name(recipient, recipient_name)
    print(recipient_object)

    # Get full list of objects available for assignment to recipient
    full_assigned_list = get_object_list(assigned)
    #print_list("current", assigned, full_assigned_list)

    # Retrieve list of objects currently assigned to recipient
    currently_assigned_list = get_assigned_object_list(recipient_object, assigned)
    print("The list of " + assigned + "s currently assigned to " + recipient_object.name + " is as follows:")
    print(currently_assigned_list)

    # Retrieve list of objects not yet assigned to recipient (as candidates for assignment)
    not_yet_assigned_list = get_not_assigned_object_list(recipient_object, assigned)
    print("The list of " + assigned + "s not yet assigned to " + recipient_object.name + " is as follows:")
    print(not_yet_assigned_list)

    # Gather data for object assigned to the recipient
    while assigned_name not in full_assigned_list:
        assigned_name = input("\nEnter the name of the " + assigned + " you want to assign to {object}: ".format(object = recipient_name))
        if assigned_name not in full_assigned_list:
            print("\nThe " + assigned + " you entered is not on the list. Please try again.")
    
    # Retrieve object to assign to recipient
    assigned_object = get_object_by_name(assigned, assigned_name)
    print(assigned_object)

    return recipient_object, assigned_object 


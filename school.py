class Admin:
  
  def __init__(self, name):
    self.name = name
    print("\n{name} has been added as a new Admin.".format(name = self.name))

  def __repr__(self):
    return "\n{name} is an Admin.".format(name = self.name)



class Subject:
  def __init__(self, name, credits):
    self.name = name
    self.teacher = ""
    self.credits = credits
    self.students = []
    self.lessons_delivered = {}
    self.tests_set = {}
    print("\n{subject} has been added as a new Subject.".format(subject = self.name))
  
  def __repr__(self):
    return "\n{subject} is a Subject worth {credits} credits.".format(subject = self.name, credits = self.credits)
  
  def enrol_student(self, student):
    # Append student name to list of students enrolled in subject
    self.students.append(student.name)
    # Append subject name to list of subjects student has enrolled in
    student.subjects_enrolled.append(self.name)
    # Update student's lessons_attended with subject name
    student.lessons_attended.update({self.name: []})
    # Confirm student enrolment
    print("\n{student} has been enrolled in {subject}".format(student = student.name, subject = self.name))
  
  def assign_teacher(self, teacher):
    # Assign teacher name to the subject
    self.teacher = teacher.name
    # Append subject name to list of subjects taught by teacher
    teacher.subjects_taught.append(self.name)
    # Update teacher's lesson_delivered and tests_set dictionaries with subject and empty list
    teacher.lessons_delivered.update({self.name: []})
    teacher.tests_set.update({self.name: []})
    # Update subject's lesson_delivered and tests_set dictionaries with teacher and empty list
    self.lessons_delivered.update({teacher.name: []})
    self.tests_set.update({teacher.name: []})
    # Confirm assignment of teacher
    print("\n{teacher} has been assigned to {subject}".format(teacher = teacher.name, subject = self.name))


class Teacher:
  def __init__(self, name, tenure):
    self.name = name
    self.tenure = tenure
    self.subjects_taught = []
    self.lessons_delivered = {}
    self.tests_set = {}
    print("\n{name} has been added as a new Teacher".format(name = self.name))
  
  def __repr__(self):
    return "\n{name} is a Teacher with {tenure} years experience.".format(name = self.name, tenure = self.tenure)
  
  def deliver_lesson(self, subject, date):
    # Update teacher's lessons_delivered against subject with lesson date
    self.lessons_delivered[subject.name].append(date)
    # Update subject's lessons delivered against teacher with lesson date
    subject.lessons_delivered[self.name].append(date)
    print("\n{teacher} delivered a {subject} lesson on {date}.".format(teacher = self.name, subject = subject.name, date = date))
  
  def set_test(self, subject, topic):
    # Append teacher's tests_set with new subject topic
    self.tests_set[subject.name].append(topic)
    # Append subject's tests_set with new teacher topic
    subject.tests_set[self.name].append(topic)
    print("\n{teacher} has set a {topic} test for the {subject} subject.".format(teacher = self.name, topic = topic, subject = subject.name))
  
  def grade_test(self, subject, topic, student, grade):
    student.grades[subject.name][topic].append(grade)
    print("\n{teacher} awarded a grade of {grade}% to {student} for the {test} test in {subject}.".format(teacher = self.name, grade = str(grade), student = student.name, test = topic, subject = subject.name))
    

class Student:
  def __init__(self, name):
    self.name = name
    self.subjects_enrolled = []
    self.lessons_attended = {}
    self.tests_submitted = {}
    self.grades = {}
    self.credits = 0
    print("\n{name} has been added as a new Student.".format(name = self.name))
  
  def __repr__(self):
    return "\n{name} is a Student enrolled in {count} Subjects.".format(name = self.name, count = len(self.subjects_enrolled))
  
  def attend_lesson(self, subject, date):
    # Update student's lessons_attended against subject with lesson date
    self.lessons_attended[subject.name].append(date)
    print("\n{student} attended a {subject} lesson on {date}.".format(student = self.name, subject = subject.name, date = date))
    
  def submit_test(self, subject, test):
    # Update the grades disctionary with an empty grade for the test submitted
    self.grades.update({subject.name: {test: []}})
    print("\n{name} submitted a {test} test for grading as part of the {subject} subject.". format(name = self.name, test = test, subject = subject.name))

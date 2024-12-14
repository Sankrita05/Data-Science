class Course:
    def __init__(self, course_name):
        self.course_name = course_name


class Student:
    def __init__(self, student_name):
        self.student_name = student_name
        self.courses = []

    def list_enrolled_courses(self):
        for course in self.courses:
            print(course.course_name, end=" ")
        print()


course1 = Course("Introduction to Programming")
course2 = Course("Data Structures")

student1 = Student("Alice")
student2 = Student("Bob")

student1.courses.extend([course1, course2])
student2.courses.append(course1)

print("Courses enrolled by Alice:", end=" ")
student1.list_enrolled_courses()

print("Courses enrolled by Bob:", end=" ")
student2.list_enrolled_courses()



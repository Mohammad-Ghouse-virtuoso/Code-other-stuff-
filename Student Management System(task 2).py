class Course:
    def __init__(self, name, credit_hours):
        self.name = name
        self.credit_hours = credit_hours
        self.roster = []

    def add_student(self, student):
        self.roster.append(student)

    def remove_student(self, student):
        if student in self.roster:
            self.roster.remove(student)
            print(f"Student {student.name} removed from {self.name}")
        else:
            print(f"Student {student.name} not enrolled in {self.name}")

class Student:
    def __init__(self, name, major):
        self.name = name
        self.major = major
        self.courses = {}
        self.grades = {}

    def enroll(self, course):
        self.courses[course.name] = course
        course.add_student(self)
        print(f"Student {self.name} enrolled in {course.name}")

    def drop_course(self, course):
        if course.name in self.courses:
            del self.courses[course.name]
            course.remove_student(self)
            if course.name in self.grades:
                del self.grades[course.name]
            print(f"Student {self.name} dropped {course.name}")
        else:
            print(f"Student {self.name} not enrolled in {course.name}")

    def assign_grade(self, course_name, grade):
        if course_name in self.courses:
            self.grades[course_name] = grade
            print(f"Grade {grade} assigned to {self.name} for {course_name}")
        else:
            print(f"Student {self.name} not enrolled in {course_name}")

    def update_grade(self, course_name, new_grade):
        if course_name in self.grades:
            self.grades[course_name] = new_grade
            print(f"Grade updated to {new_grade} for {self.name} in {course_name}")
        else:
            print(f"Student {self.name} not enrolled in {course_name}")

    def calculate_gpa(self):
        total_credits = 0
        total_points = 0
        for course_name, grade in self.grades.items():
            course = self.courses[course_name]
            total_credits += course.credit_hours
            grade_points = self.get_grade_points(grade)
            total_points += grade_points * course.credit_hours
        if total_credits == 0:
            return 0
        else:
            return total_points / total_credits

    def get_grade_points(self, grade):
        if grade == "O":
            return 10.0
        elif grade == "A+":
            return 9.0
        elif grade == "A":
            return 8.0
        elif grade == "B+":
            return 8.0
        elif grade == "B":
            return 7.5
        elif grade == "C":
            return 7.0
        elif grade == "D":
            return 6.0
        elif grade == "E":
            return 5.5
        elif grade == "F":
            return 4.0
        else:
            return 0

# Example usage
courses = []
students = []

while True:
    print("\nMenu:")
    print("1. Add Course")
    print("2. Add Student")
    print("3. Enroll Student in Course")
    print("4. Drop Student from Course")
    print("5. Assign Grade")
    print("6. Update Grade")
    print("7. Display Students")
    print("8. Calculate Student GPA")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == "1":
        name = input("Enter course name: ")
        credit_hours = int(input("Enter credit hours: "))
        course = Course(name, credit_hours)
        courses.append(course)
        print(f"{name} course added successfully.")

    elif choice == "2":
        name = input("Enter student name: ")
        major = input("Enter student major: ")
        student = Student(name, major)
        students.append(student)
        print(f"{name} student added successfully.")

    elif choice == "3":
        student_name = input("Enter student name: ")
        course_name = input("Enter course name: ")
        student = next((s for s in students if s.name == student_name), None)
        course = next((c for c in courses if c.name == course_name), None)
        if student and course:
            student.enroll(course)
        else:
            print("Invalid student or course name.")

    elif choice == "4":
        student_name = input("Enter student name: ")
        course_name = input("Enter course name: ")
        student = next((s for s in students if s.name == student_name), None)
        course = next((c for c in courses if c.name == course_name), None)
        if student and course:
            student.drop_course(course)
        else:
            print("Invalid student or course name.")

    elif choice == "5":
        student_name = input("Enter student name: ")
        course_name = input("Enter course name: ")
        grade = input("Enter grade: ")
        student = next((s for s in students if s.name == student_name), None)
        if student:
            student.assign_grade(course_name, grade)
        else:
            print("Invalid student name.")

    elif choice == "6":
        student_name = input("Enter student name: ")
        course_name = input("Enter course name: ")
        new_grade = input("Enter new grade: ")
        student = next((s for s in students if s.name == student_name), None)
        if student:
            student.update_grade(course_name, new_grade)
        else:
            print("Invalid student name.")

    elif choice == "7":
        print("\nStudents:")
        for student in students:
            print(f"Name: {student.name}, Major: {student.major}")
            print("Enrolled Courses:")
            for course_name, course in student.courses.items():
                print(f"- {course_name}")
            print("Grades:")
            for course_name, grade in student.grades.items():
                print(f"  {course_name}: {grade}")
            print()

    elif choice == "8":
        student_name = input("Enter student name: ")
        student = next((s for s in students if s.name == student_name), None)
        if student:
            gpa = student.calculate_gpa()
            print(f"{student_name}'s GPA: {gpa:.2f}")
        else:
            print("Invalid student name.")

    elif choice == "9":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please try again.")

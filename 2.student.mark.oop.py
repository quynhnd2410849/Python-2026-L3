class Student:
    def __init__(self, sid, name, dob):
        self.id = sid
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}"


class Course:
    def __init__(self, cid, name):
        self.id = cid
        self.name = name

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"


class MarkManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {} 

    def input_students(self):
        n = int(input("Enter number of students: "))
        for _ in range(n):
            sid = input("Student ID: ")
            name = input("Student name: ")
            dob = input("Date of birth: ")
            self.students.append(Student(sid, name, dob))

    def input_courses(self):
        n = int(input("Enter number of courses: "))
        for _ in range(n):
            cid = input("Course ID: ")
            name = input("Course name: ")
            self.courses.append(Course(cid, name))

    def input_marks(self):
        course_id = input("Enter course ID to input marks: ")
        if course_id not in [c.id for c in self.courses]:
            print("Course not found!")
            return
        if course_id not in self.marks:
            self.marks[course_id] = {}
        for student in self.students:
            mark = float(input(f"Enter mark for {student.name} (ID: {student.id}): "))
            self.marks[course_id][student.id] = mark

    def list_students(self):
        print("\n--- Students ---")
        for s in self.students:
            print(s)

    def list_courses(self):
        print("\n--- Courses ---")
        for c in self.courses:
            print(c)

    def show_marks(self):
        course_id = input("Enter course ID to show marks: ")
        if course_id not in self.marks:
            print("No marks recorded for this course.")
            return
        print(f"\n--- Marks for course {course_id} ---")
        for sid, mark in self.marks[course_id].items():
            student = next(s for s in self.students if s.id == sid)
            print(f"{student.name} (ID: {sid}): {mark}")


def main():
    manager = MarkManagement()
    while True:
        print("\n--- Student Mark Management (OOP) ---")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show marks")
        print("0. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            manager.input_students()
        elif choice == "2":
            manager.input_courses()
        elif choice == "3":
            manager.input_marks()
        elif choice == "4":
            manager.list_students()
        elif choice == "5":
            manager.list_courses()
        elif choice == "6":
            manager.show_marks()
        elif choice == "0":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

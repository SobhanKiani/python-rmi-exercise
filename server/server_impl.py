from application.api import CourseAPI
from application.classes import Course, Student


class ServerImpl(CourseAPI):
    def __init__(self) -> None:
        self.course_list = []

    def create(self, name: str, capacity: int, teacher_name: str):
        new_course = Course(name, capacity, teacher_name)
        self.course_list.append(new_course)
        return ("Course Added", new_course.id), 200

    def add_student(self, student: Student, course_id: int):
        course = self.find_course(course_id)
        if course == None:
            return "Course Not Found", 404
        else:
            if course.capacity > len(course.students):
                course.add_student(student)
                return "Student Added", 200
            else:
                return "The Course Is Full And No New Students Can Be Added", 400

    def remove_student(self, student_id: int, course_id: int):
        course: Course = self.find_course(course_id)
        student = course.remove_student(student_id)
        if student == None:
            return "Student Not Found", 404
        else:
            return "Student Removed From The Course", 200

    def remove_course(self, course_id: int):
        for idx, course in enumerate(self.course_list):
            if course_id == course.id:
                del self.course_list[idx]
                return "Course Removed", 200
        return "Course Not Found", 404

    def change_capacity(self, course_id: int, new_capacity: int):
        course: Course = self.find_course(course_id)
        if course == None:
            return "Course Not Found", 404
        else:
            msg, is_done = course.set_capacity(new_capacity)
            if is_done:
                return msg, 200
            else:
                return msg, 400

    def get_student_list(self, course_id: int):
        course: Course = self.find_course(course_id)
        if course == None:
            return "Course Not Found", 404
        else:
            return course.students, 200

    def find_course(self, course_id: int):
        curr_course: Course = None
        for course in self.course_list:
            if course.id == course_id:
                curr_course = course
                break
        return curr_course

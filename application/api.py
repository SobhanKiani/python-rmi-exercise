from abc import ABC, abstractmethod, abstractstaticmethod
from .classes import Student


class CourseAPI(ABC):

    @abstractmethod
    def create(self, name: str, capacity: int, teacher_name: str):
        pass

    @abstractmethod
    def add_student(self, student: Student, course_id: int):
        pass

    @abstractmethod
    def remove_student(self, student_id: int, course_id: int):
        pass

    @abstractmethod
    def remove_course(self, course_id: int):
        pass

    @abstractmethod
    def change_capacity(self, course_id: int, new_capacity: int):
        pass

    @abstractmethod
    def get_student_list(self, course_id:int):
        pass

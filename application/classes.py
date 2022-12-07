import random


class Student:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

    def to_string(self) -> str:
        return f'{self.id}:{self.name}'


class Course:
    def __init__(self, name: str, capacity: int, teacher_name: str):
        self.name = name
        self.capacity = capacity
        self.teacher_name = teacher_name
        self.students = []
        self.id = random.randint(1, 100000)

    def add_student(self, student: Student):
        self.students.append(student)
        return self.students

    def remove_student(self, student_id):
        for idx, student in enumerate(self.students):
            if student_id == student.id:
                del self.students[idx]
                return student

    def set_capacity(self, new_capacity):
        if new_capacity >= self.capacity:
            self.capacity = new_capacity
            return "Capacity Changed", True
        else:
            return "You Cannot Lower The Capacity As Some Students May Be Removed", False

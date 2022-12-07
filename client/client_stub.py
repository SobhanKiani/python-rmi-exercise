from client.stub_base import StubBase
from application.api import CourseAPI
from application.classes import Student
import json


class ClientStub(StubBase, CourseAPI):

    def create(self, name: str, capacity: str, teacher_name: str):
        invocation_msg = {
            'method_name': "create",
            'params': [
                {'name': 'name', 'value': name, 'type': 'str'},
                {'name': 'capacity', 'value': capacity, 'type': 'int'},
                {'name': 'teacher_name', 'value': teacher_name, 'type': 'str'},
            ]
        }

        response = self.invoke(invocation_msg)

        # first index is text message
        # second index is course id
        return response.msg

    def add_student(self, student: Student, course_id: int):
        invocation_msg = {
            'method_name': "add_student",
            'params': [
                {'name': 'student', 'value': json.dumps(
                    student.__dict__), 'type': 'ref', 'instanceof': 'Student'},
                {'name': 'course_id', 'value': course_id, 'type': 'int'},
            ]
        }

        response = self.invoke(invocation_msg)
        return response.msg

    def remove_course(self, course_id: int):
        invocation_msg = {
            'method_name': "remove_course",
            'params': [
                {'name': 'course_id', 'value': course_id, 'type': 'int'},
            ]
        }
        response = self.invoke(invocation_msg)
        return response.msg

    def remove_student(self, student_id: int, course_id: int):
        invocation_msg = {
            'method_name': 'remove_student',
            'params': [
                {'name': 'course_id', 'value': course_id, 'type': 'int'},
                {'name': 'student_id', 'value': student_id, 'type': 'int'},
            ]
        }

        response = self.invoke(invocation_msg)
        return response.msg

    def change_capacity(self, course_id: int, new_capacity: int):

        invocation_msg = {
            'method_name': "change_capacity",
            'params': [
                {'name': 'course_id', 'value': course_id, 'type': 'int'},
                {'name': 'course_id', 'value': new_capacity, 'type': 'int'},
            ]
        }

        response = self.invoke(invocation_msg)
        return response.msg

    def get_student_list(self, course_id: int):
        invocation_msg = {
            'method_name': "get_student_list",
            'params': [
                {'name': 'course_id', 'value': course_id, 'type': 'int'},
            ]
        }

        response = self.invoke(invocation_msg)
        student_list = response.msg
        studnet_list = [Student(**std) for std in student_list]
        return studnet_list

from .server_impl import ServerImpl
from application.api import CourseAPI, Student
from server.skeleton_base import SkeletonBase
from messages import SendingMessage, MessageTypes
from .utils import prepare_normal_paramter, prepare_ref_paramter
import json


class ServerSkeleton(SkeletonBase, CourseAPI):
    def __init__(self, port, ip, obj: ServerImpl):
        super().__init__(port, ip, 'Course', '1.0.0')
        self.server_impl = obj

    def create(self, name: str, capacity: int, teacher_name: str):
        return self.server_impl.create(name, capacity, teacher_name)

    def add_student(self, student: Student, course_id: int):
        return self.server_impl.add_student(student, course_id)

    def remove_course(self, course_id: int):
        return self.server_impl.remove_course(course_id)

    def remove_student(self, student_id: int, course_id: int):
        return self.server_impl.remove_student(student_id, course_id)

    def change_capacity(self, course_id: int, new_capacity: int):
        return self.server_impl.change_capacity(course_id, new_capacity)

    def get_student_list(self, course_id: int):
        return self.server_impl.get_student_list(course_id)

    # This Message Handler Calls The Functions By Correct Params
    # Then returns the response to client stub

    def stub_message_handler(self):
        while True:
            c, req = self.sm.recieve_message()
            function = eval('self.'+req.msg['method_name'])
            params = {}
            for param in req.msg['params']:
                if param['type'] == 'ref':
                    param_name, param_value = prepare_ref_paramter(param)
                    params[param_name] = param_value
                else:
                    param_name, param_value = prepare_normal_paramter(param)
                    params[param_name] = param_value
            msg, status = function(**params)

            if req.msg['method_name'] == 'get_student_list':
                msg = [std.__dict__ for std in msg]

            response = SendingMessage(msg,
                                      MessageTypes.FUNCTION_INVOCATION_RESPONSE, status)
            c.send(response.dumps())

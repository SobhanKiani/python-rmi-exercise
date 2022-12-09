import sys

parent_module = sys.modules['.'.join(__name__.split('.')[:-1]) or '__main__']
if __name__ == '__main__' or parent_module.__name__ == '__main__':
    from client.client_stub import ClientStub
    from api.classes import Student
else:
    from .client.client_stub import ClientStub
    from .api.classes import Student


if __name__ == '__main__':
    course_stub = ClientStub('localhost', 9992)
    course_stub.lookup("Course", '1.0.0')

    msg, course_id = course_stub.create('Math', 10, 'Mohammadi')
    print('1', msg)

    new_student = Student('Sobhan Kiani', 1)
    result = course_stub.add_student(new_student, course_id)
    print('2', result)
    
    stds = course_stub.get_student_list(course_id)
    stds_repr = [std.to_string() for std in stds]
    print('3', stds_repr,)
    print(f'Number Of Students In The Class: {len(stds_repr)}')

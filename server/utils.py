import json

class TestObj:
    def __init__(self, data) -> None:
        self.data = data


def prepare_ref_paramter(ref_parameter):
    object_paramters_dict = json.loads(ref_parameter['value'])
    class_name = eval(ref_parameter['instanceof'])
    return ref_parameter['name'], class_name(**object_paramters_dict)


def prepare_normal_paramter(param):
    param_type = eval(param['type'])
    return param['name'], param_type(param['value'])
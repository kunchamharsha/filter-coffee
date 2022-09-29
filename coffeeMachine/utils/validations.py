

def input_params_validation(input_params):
    return True

def service_id_validation(data):
    return True


def validate_input(data,key):
    if key == 'input_params':
        return input_params_validation(data)
    if key == 'service_id':
        return service_id_validation(data)
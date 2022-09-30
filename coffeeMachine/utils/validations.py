

def input_params_validation(input_params):
    return True

def service_id_validation(data):
    return True
def eval_params_check(data):
    return  True
    if len(data.get('required'))>len(data.get('given')):
        return False
    for input_param in data.get('required'):
        if input_param not in data.get('given'):
            return False
    return True

def validate_input(data,key):
    if key == 'input_params':
        return input_params_validation(data)
    if key == 'service_id':
        return service_id_validation(data)
    if key == 'eval_params_check':
        return 
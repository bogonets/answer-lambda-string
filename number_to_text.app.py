import numpy as np
import sys

TRUE_STR_LIST = ['true']


enable_default = False
default_value = ''


def on_set(k, v):
    if k == 'default_value':
        global default_value
        default_value = v
    elif k == 'enable_default':
        global enable_default
        enable_default = True if v.lower() in TRUE_STR_LIST else False


def on_get(k):
    if k == 'default_value':
        return str(default_value)
    elif k == 'enable_default':
        return str(enable_default)


def on_run(number):

    if not number.shape or len(number.shape) != 1 or number.shape[0] != 1:
        return return_negative()

    try:
        string_data = str(number[0])
    except:
        return return_negative()

    return {'text' : string_data}


def return_negative():
    if enable_default:
        return {'text': default_value}
    else:
        return {'text': None}


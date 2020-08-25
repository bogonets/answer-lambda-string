# -*- coding: utf-8 -*-


delimiter = ''


def on_set(key, val):
    if key == "delimiter":
        global delimiter
        delimiter = val


def on_get(key):
    if key == "delimiter":
        return delimiter


def on_run(left_string, right_string):
    left_data = "".join([chr(item) for item in left_string])
    right_data = "".join([chr(item) for item in left_string])

    return {'text': f'{left_data}{delemiter}{right_data}'}

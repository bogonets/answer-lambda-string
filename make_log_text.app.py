# -*- coding: utf-8 -*-

import numpy as np
import time
import sys


prefix = ''
suffix = ''


def on_set(key, val):
    if key == "prefix":
        global prefix
        prefix = val
    elif key == "suffix":
        global suffix
        suffix = val


def on_get(key):
    if key == "format":
        return format_str


def on_run(string):
    t = time.time()
    v = time.strftime("%Y%m%dT%H%M%S", time.localtime(t))

    input_data = "".join([chr(item) for item in string])

    # sys.stdout.write(f"[make_log_text] f: {format_str}, v : {v}, t: {t}")
    # sys.stdout.flush()

    txt = f'[{v}] {prefix}{input_data}{suffix}'

    return {'text': txt}


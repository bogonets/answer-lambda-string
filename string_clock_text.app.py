# -*- coding: utf-8 -*-

import numpy as np
import time
import sys


format_str = "%Y%m%dT%H%M%S"


def on_set(key, val):
    if key == "format":
        global format_str
        format_str = val


def on_get(key):
    if key == "format":
        return format_str


def on_init():
    return True


def on_valid():
    return True


def on_run():
    t = time.time()
    
    v = time.strftime(format_str, time.localtime(t))

    # sys.stdout.write(f"[string_clock_text] f: {format_str}, v : {v}, t: {t}")
    # sys.stdout.flush()

    return {'text': v}
    #bv = v.encode('utf-8')
    #return {'text': np.frombuffer(bv, dtype=np.uint8)}


def on_destroy():
    return True


if __name__ == '__main__':
    pass

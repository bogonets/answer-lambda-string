# -*- coding: utf-8 -*-

import numpy as np
import time
import sys
import re


pattern = ''


def on_set(key, val):
    if key == "pattern":
        global pattern
        pattern = val


def on_get(key):
    if key == "pattern":
        return pattern


def on_run(string):
    t = time.time()
    
    input_data = "".join([chr(item) for item in string])

    result = re.search(pattern, input_data)

    # sys.stdout.write(f"[make_log_text] f: {format_str}, v : {v}, t: {t}")
    # sys.stdout.flush()

    if not result:
        return {'match': None, 'span': None}

    return {'match': result[0], 'span': np.array(result.span())}


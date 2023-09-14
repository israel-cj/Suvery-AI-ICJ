import copy
import numpy as np
from typing import Any, Dict, Optional
import pandas as pd
import ast

def run_llm_code(code):
    try:
        paper = None
        globals_dict = {'paper': paper}
        output = {}
        exec(code, globals_dict, output)
        paper = output['paper']
        print('This is the paper')
        print(paper)

    except Exception as e:
        print("Code could not be executed", e)
        raise (e)

    return paper



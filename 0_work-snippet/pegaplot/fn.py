#!/usr/bin/env python
# coding: utf-8
# ver. 2020.04.01.
# Jehyun Lee (jehyun.lee@gmail.com)
import os, copy, sys, io, json
import numpy as np
import pandas as pd

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import seaborn as sns

from krfont import add_KRFONT  

def chktype(var, typename):
    if typename in str(type(var)):
        return True
    else:
        if typename == 'list':
            if 'array' in str(type(var)):
                return True
            else:
                return False
        else:
            return False
    



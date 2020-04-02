#!/usr/bin/env python
# coding: utf-8
# ver. 2020.04.01.
# Jehyun Lee (jehyun.lee@gmail.com)

### Korean Font Setting

import matplotlib as mpl
import matplotlib.font_manager as fm
import platform, os


def add_KRFONT(KRFONT: str):
    mpl.rcParams['font.sans-serif'] = [KRFONT] + mpl.rcParams['font.sans-serif']
    mpl.rcParams['font.serif'] = [KRFONT] + mpl.rcParams['font.serif']
    mpl.rcParams['font.cursive'] = [KRFONT] + mpl.rcParams['font.cursive']
    mpl.rcParams['font.fantasy'] = [KRFONT] + mpl.rcParams['font.fantasy']
    mpl.rcParams['font.monospace'] = [KRFONT] + mpl.rcParams['font.monospace']


def set_KRFONT(KRFONT: str):
    system = platform.system()

    if system == 'Windows' or 'Linux':
        if system == 'Windows':
            datapath = os.getcwd() + '\\'
            imagepath = datapath + 'images\\'

            # ttf 폰트 전체개수
            font_list[:10]

            f = [f.name for f in fm.fontManager.ttflist]
            f[:10]

            [(f.name, f.fname) for f in fm.fontManager.ttflist if 'Nanum' in f.name]

            path = 'C:\\Windows\\Fonts\\NanumBarunGothic.ttf'

        elif system == 'Linux':
            datapath = os.getcwd() + '//'
            imagepath = datapath + 'images//'

        #     !apt-get update -qq
        #     !apt-get install fonts-nanum* -qq

            path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'  
            KRFONT = fm.FontProperties(fname=path, size=10).get_name()

            fm._rebuild()
            mpl.rcParams['axes.unicode_minus'] = False

        KRFONT = fm.FontProperties(fname=path, size=10).get_name()
        add_KRFONT(KRFONT)

        print(f"# matplotlib 한글 사용 가능: {KRFONT}")


    else:
        sys.exit('ERROR: Sorry, my code has compatibility with Windows and Linux only.')

    return KRFONT


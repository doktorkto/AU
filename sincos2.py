#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import numpy
import matplotlib.pyplot as mpp
"""
Здесь загружаются необходимые для программы модули.
"""


if __name__=='__main__':
    arguments = numpy.r_[0:200:0.1]
    mpp.plot(
        arguments,
        [math.sin(a) * math.cos(a/20.0)**2 for a in arguments]
        # В данной части прогламмы задаётся вид функции, т.е. оси и вид функции.
    )
    mpp.show()

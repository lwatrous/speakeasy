#!/usr/bin/env python
from __future__ import division
import numpy
# import matplotlib.pyplot as plt
from numpy import pi
from scipy.io import wavfile

SAMPLE_RATE = 48000

t = numpy.arange(1 * SAMPLE_RATE) / SAMPLE_RATE
y = numpy.sin(t * 2 * pi * 100)
y = numpy.asarray(y * 32767, numpy.int16)

wavfile.write('test.wav', SAMPLE_RATE, y)

# plt.plot(t, y)
# plt.show()

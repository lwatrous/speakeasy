#!/usr/bin/env python
from __future__ import division
import json
import numpy
from scipy.io import wavfile

SAMPLE_RATE = 48000
LOW_FREQ = 20
HIGH_FREQ = 20000
POINTS_PER_OCTAVE = 30
MIN_CYCLES = 20
MIN_SECONDS = 0.1
NAME = '1-min-sweep'


def main():
    metadata = build_metadata()
    write_metadata(metadata)
    write_signal(metadata)


def write_metadata(metadata):
    with open(NAME + '.json', 'w') as f:
        json.dump(metadata, f, indent=4, sort_keys=True)


def write_signal(metadata):
    wavfile.write(NAME + '.wav', SAMPLE_RATE, build_signal(metadata))


def build_signal(metadata):
    total_length = int(
        ((metadata[-1]['start'] + metadata[-1]['length']) * SAMPLE_RATE)) + 1
    samples = numpy.zeros(total_length, dtype=numpy.int16)
    for item in metadata:
        chunk = build_single_freq_chunk(item['frequency'], item['length'])
        start_sample = int(item['start'] * SAMPLE_RATE)
        samples[start_sample:start_sample+len(chunk)] += chunk
    return samples


def build_single_freq_chunk(frequency, length):
    t = numpy.arange(int(length * SAMPLE_RATE)) / SAMPLE_RATE
    y = numpy.sin(2 * numpy.pi * frequency * t)
    return numpy.asarray(y * 32767, dtype=numpy.int16)


def build_metadata():
    freq = LOW_FREQ
    freq_step = 2**(1/POINTS_PER_OCTAVE)
    t_offset = 0
    data = []
    while freq <= HIGH_FREQ:
        length = max(MIN_CYCLES / freq, MIN_SECONDS)
        data.append({
            'start': t_offset,
            'length': length,
            'frequency': freq,
        })
        freq *= freq_step
        t_offset += length
    return data


if __name__ == '__main__':
    main()

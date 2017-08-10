#!/usr/bin/env python
import sys
import json
from scipy.io import wavfile


def main():
    sample_file = sys.argv[1]
    metadata_file = sys.argv[2]

    srate, samples = wavfile.read(sample_file)
    with open(metadata_file) as f:
        metadata = json.load(f)


def analyze_samples(samples, metadata, srate):



def window(sample_length):



if __name__ == '__main__':
    main()

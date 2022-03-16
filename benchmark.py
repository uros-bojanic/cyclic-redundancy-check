# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Uros Bojanic
# Created Date: 2022/03/14
# ---------------------------------------------------------------------------

# Python program to automatically test and assess the performance of CRC
from generators import get_generators
from crc_otr import crc_check
import numpy as np
import logging
import random
import time


# Function to return a randomly generated binary sequence of given size (n)
def get_random_sequence(n):
    return bin(random.randint(0, 2 ** n - 1))


# Driver code
if __name__ == "__main__":
    # Logging configuration
    logging.basicConfig(filename='benchmark.log',
                        filemode='w',
                        level=logging.DEBUG,
                        format='%(asctime)s:(levelname)s:%(message)s')

    # Iterate over all commonly used generators
    for gen in get_generators():
        # Get current generator polynomial and algorithm name
        generator = int(gen[0], 2)  # ex. 0b10101
        algorithm = gen[1]          # ex. CRC-3-GSM

        # Generate information sequences of variable length
        for sequence_length in (1 << s for s in range(0, 16)):  # range(1, 10001)
            # Measure execution times
            execution_time = []
            # Generate 10 random information sequences with current length
            for iteration in range(0, 10):
                sequence = int(get_random_sequence(sequence_length), 2)
                # Initiate cyclic redundancy check
                # logging.debug("CRC check started...")
                # logging.debug("\t* encoded sequence:     {:b}".format(int(sequence)))
                # logging.debug("\t* generator polynomial: {:b}".format(int(generator)))
                start_time = time.time()
                # Perform cyclic redundancy check
                crc_remainder = crc_check(sequence=sequence, generator=generator)
                # End cyclic redundancy check
                end_time = time.time()
                time_diff = 1000 * (end_time - start_time)  # [ms]
                execution_time.append(time_diff)
                # logging.debug("CRC check took {} ms (RESULT = {:b}).".format(time_diff, crc_remainder))
            # Calculate mean execution time for this pair
            print("{},{},{},{}".format(algorithm, generator.bit_length()-1, sequence_length, np.mean(execution_time)))

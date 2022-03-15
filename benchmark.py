# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Uros Bojanic
# Created Date: 2022/03/14
# ---------------------------------------------------------------------------

# Python program to automatically test and assess the performance of CRC
from crc_otr import crc_check
import logging
import time


# Driver code
if __name__ == "__main__":
    # Logging configuration
    logging.basicConfig(
        filename='benchmark.log',
        filemode='a',
        level=logging.DEBUG,
        format='%(asctime)s:(levelname)s:%(message)s'
    )

    # Generate information sequence and generator polynomial
    sequence = 0b11011011011
    generator = 0b10101

    # Initiate cyclic redundancy check
    logging.debug("CRC check started...")
    logging.debug("\t* encoded sequence:     {:b}".format(int(sequence)))
    logging.debug("\t* generator polynomial: {:b}".format(int(generator)))
    start_time = time.time()

    # Perform cyclic redundancy check
    crc_remainder = crc_check(sequence=sequence, generator=generator)

    # End cyclic redundancy check
    end_time = time.time()
    logging.debug("CRC check took {} ms (RESULT = {:b}).".format(1000 * (end_time - start_time), crc_remainder))

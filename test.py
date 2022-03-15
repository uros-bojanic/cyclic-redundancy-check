# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Uros Bojanic
# Created Date: 2022/03/14
# ---------------------------------------------------------------------------

# Python program to manually test CRC on 3 sets of data blocks
from crc_otr import crc_decode, crc_encode


# Driver code
if __name__ == "__main__":
    # CRC_DECODE - Manual Tests
    print("Decode (tests):")
    decode_tests = [
        (0b11011010000, 0b10101),   # >>> False
        (0b11011011011, 0b10101),   # >>> True
        (0b100100000, 0b1101),      # >>> False
        (0b100100001, 0b1101),      # >>> True
        (0b11001110111, 0b11001),   # >>> False
        (0b11001110010, 0b11001)    # >>> True
    ]
    # Run tests
    for d in decode_tests:
        # information sequence
        test_seq = d[0]
        # generator polynomial
        test_gen = d[1]
        # call CRC to check for errors in the given information sequence
        test_res = crc_decode(sequence=test_seq, generator=test_gen)
        # print result
        print("[{:12b}] % [{:5b}] -> {}".format(test_seq, test_gen, test_res))

    # CRC_ENCODE - Manual Tests
    print("Encode (tests):")
    encode_tests = [
        (0b1101101, 0b10101),       # >>> 0b11011011011
        (0b100100, 0b1101),         # >>> 0b100100001
        (0b1100111, 0b11001)        # >>> 0b11001110010
    ]
    # Run tests
    for e in encode_tests:
        # information sequence
        test_seq = e[0]
        # generator polynomial
        test_gen = e[1]
        # call CRC to generate suffix for the given information sequence
        test_res = crc_encode(sequence=test_seq, generator=test_gen)
        # call CRC to check for errors in the generated code (verify)
        decoded = crc_decode(test_res, test_gen)
        # print result
        print("[{:12b}] % [{:5b}] -> {:b}\t# {}".format(test_seq, test_gen, test_res, decoded))

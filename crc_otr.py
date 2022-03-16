# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Uros Bojanic
# Created Date: 2022/03/14
# ---------------------------------------------------------------------------

__author__ = "Uros Bojanic"
__version__ = "1.0.1"

"""This module provides users with cyclic redundancy check tooling
under the `crc_otr` package - a Python library for cyclic redundancy
check (CRC) using polynomial long division in GF(2).

Functions:
----------
    crc_check(int, int) : int
        Performs a cyclic redundancy check (CRC) on the given information sequence.
    crc_padding(int, int) : int
        Adds padding (trailing zeros) to the given information sequence.
    crc_decode(int, int) : bool
        Decodes an information sequence using the provided generator polynomial.
    crc_encode(int, int) : int
        Encodes an information sequence using the provided generator polynomial.
"""

# Import libraries
from helper import xor_operation, shl_operation, clear_bit


# Function to perform cyclic redundancy check (CRC)
def crc_check(sequence, generator):
    """Performs a cyclic redundancy check (CRC) on the given information
    sequence (`sequence`) using polynomial long division with the generator
    polynomial (`generator`). Taking the sequence as the dividend and the
    generator as the divisor, the quotient is discarded and the remainder
    becomes the result of the CR check (if this remainder is equal to 0,
    there are no errors in the sequence - otherwise, errors are detected).

    Parameters:
    -----------
        sequence : int
            the information sequence (a binary number) on which CRC will be performed
        generator : int
            generator polynomial (binary representation) used as the divisor in CRC

    Returns:
    --------
        crc_check(int, int) : int
            terminal remainder of the polynomial long division of sequence by generator

    Examples:
    ---------
        >>> crc_check(0b11011010000, 0b10101)
        0b1011
        >>> crc_check(0b11011011011, 0b10101)
        0b0
    """
    # Calculate length of generator & sequence bit-vectors
    generator_length = generator.bit_length()  # generator polynomial (binary representation)
    sequence_length = sequence.bit_length()  # encoded sequence (padded)

    # Calculate remainder of encoded sequence division by the generator polynomial
    next_bit = sequence_length - generator_length - 1
    temp = sequence >> next_bit + 1 if next_bit > 0 else sequence
    while next_bit >= 0:  # iterate over the entire encoded sequence
        temp = xor_operation(temp, generator_length - 1, generator)  # calculate XOR result in each iteration
        temp = shl_operation(temp, next_bit, sequence)  # use long-division method to find remainder
        temp = clear_bit(temp, generator_length)  # clear the oldest (most significant) bit
        next_bit -= 1

    # Find remainder (equals 0 if no errors are detected) and return as result
    crc_remainder = xor_operation(temp, generator_length - 1, generator)
    return crc_remainder


# Function to add padding to an information sequence
def crc_padding(sequence, generator=0b100000100110000010001110110110111):
    """Adds padding (trailing zeros in the binary representation) to the
    given binary number (`sequence`) with length of the padding equal to
    1 less than the length of the generator polynomial (`generator`),
    and returns the padded information sequence.

    Parameters:
    -----------
        sequence : int
            the original information sequence (a binary number) which will be padded
        generator : int
            generator polynomial (binary representation) used as the divisor in CRC

    Returns:
    --------
        crc_padding(int, int) : int
            padded sequence (a binary number) - as the result of adding trailing zeros

    Examples:
    ---------
        >>> crc_padding(0b1101101, 0b10101)
        0b11011010000
        >>> crc_padding(0b100100, 0b1101)
        0b100100000
    """
    # Add padding (length one less than generator sequence)
    return sequence << generator.bit_length() - 1


# Function to decode an information sequence
def crc_decode(sequence, generator=0b100000100110000010001110110110111):
    """Decodes a binary number (`sequence`) using the provided generator
    polynomial (`generator`), and returns a boolean value indicating
    whether there are errors in the original information sequence or not,
    based on the result of a cyclic redundancy check. If generator is not
    passed as an argument, CRC32 is used by default.

    Parameters:
    -----------
        sequence : int
            the original information sequence (a binary number) which will be decoded
        generator : int
            generator polynomial (binary representation) used as the divisor in CRC

    Returns:
    --------
        crc_decode(int, int) : bool
            True if no errors are detected in the information sequence, False otherwise

    Examples:
    ---------
        >>> crc_decode(0b11011010000, 0b10101)
        False
        >>> crc_decode(0b11011011011, 0b10101)
        True
        >>> crc_decode(0b1101010011110100101111101011011100111001000011010001)
        True
    """
    # Check if the CRC remainder is equal to 0
    return crc_check(sequence, generator) == 0


# Function to encode an information sequence
def crc_encode(sequence, generator):
    """Encodes a binary number (`sequence`) using the provided generator
    polynomial (`generator`), and returns the resulting (encoded) message.
    The original binary sequence is expanded (padding is added), and the
    appropriate suffix is added as a result of the cyclic redundancy check.
    If generator is not passed as an argument, CRC32 is used by default.

    Parameters:
    -----------
        sequence : int
            the original information sequence (a binary number) which will be encoded
        generator : int
            generator polynomial (binary representation) used as the divisor in CRC

    Returns:
    --------
        crc_encode(int, int) : int
            encoded sequence (a binary number) - as the result of CRC

    Examples:
    ---------
        >>> crc_encode(0b1101101, 0b10101)
        0b11011011011
        >>> crc_encode(0b01100111, 0b11001)
        0b11001110010
        >>> crc_encode(0b11101010111010100110010101111010110101)
        0b1110101011101010011001010111101011010111000111000111001000111111010010
    """
    # Add padding for given sequence-generator pair
    sequence = crc_padding(sequence, generator)
    # Add the CRC remainder for given sequence-generator pair
    return sequence + crc_check(sequence, generator)

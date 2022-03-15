# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Uros Bojanic
# Created Date: 2022/03/14
# ---------------------------------------------------------------------------

__author__ = "Uros Bojanic"
__version__ = "1.0.1"

"""This module provides helper functions for various bit-wise operations
utilized in the cyclic redundancy check tool (`crc_otr`).

Functions:
----------
    get_bit(int, int) : int
        Selects and returns a particular bit from the given binary number.
    set_bit(int, int) : int
        Sets the value of a particular bit in given binary number to 1.
    clear_bit(int, int) : int
        Sets the value of a particular bit in given binary number to 0.
    shl_operation(int, int, int) : int
        Shifts given binary number to the left by one under certain conditions.
    xor_operation(int, int, int) : int
        Performs a XOR operation on the given binary numbers under certain conditions.
"""


# Function to get a specific bit from a number
def get_bit(value, bit):
    """Selects and returns a particular bit (`bit`) from the given binary number (`value`).

    Parameters:
    -----------
        value : int
            a binary number from which the bit will be selected
        bit : int
            ordinal indicator of the bit to be selected from the number

    Returns:
    --------
        get_bit(int, int) : int
            value of a single selected bit from the original number

    Raises:
    -------
        ValueError : if `bit` is not a non negative number

    Examples:
    ---------
        >>> get_bit(0b1011, 0)
        1
        >>> get_bit(0b1011, 1)
        1
        >>> get_bit(0b1011, 2)
        0
        >>> get_bit(0b1011, 3)
        1
        >>> get_bit(0b1011, 99)
        0
        >>> get_bit(0b1011, -1)
        ValueError
    """
    if not bit >= 0:
        raise ValueError('Invalid bit ordinal indicator.')
    return (value >> bit) & 1


# Function to set a specific bit from a number to 1
def set_bit(value, bit):
    """Sets the value of a particular bit (`bit`) in given binary number (`value`) to 1.

    Parameters:
    -----------
        value : int
            a binary number in which the specific bit will be set
        bit : int
            ordinal indicator of the bit to be set to 1

    Returns:
    --------
        set_bit(int, int) : int
            integer value of the new (modified) binary number

    Raises:
    -------
        ValueError : if `bit` is not a non negative number

    Examples:
    ---------
        >>> set_bit(0b1011, 2)
        0b1111
        >>> set_bit(0b1011, 0)
        0b1011
        >>> set_bit(0b1011, 5)
        0b101011
        >>> set_bit(0b1011, 9)
        0b1000001011
        >>> set_bit(0b1011, -1)
        ValueError
    """
    if not bit >= 0:
        raise ValueError('Invalid bit ordinal indicator.')
    return value | (1 << bit)


# Function to set a specific bit from a number to 0
def clear_bit(value, bit):
    """Sets the value of a particular bit (`bit`) in given binary number (`value`) to 0.

    Parameters:
    -----------
        value : int
            a binary number in which the specific bit will be cleared
        bit : int
            ordinal indicator of the bit to be set to 0

    Returns:
    --------
        clear_bit(int, int) : int
            integer value of the new (modified) binary number

    Raises:
    -------
        ValueError : if `bit` is not a non negative number

    Examples:
    ---------
        >>> clear_bit(0b1011, 1)
        0b1001
        >>> clear_bit(0b1011, 2)
        0b1011
        >>> clear_bit(0b1011, 3)
        0b11
        >>> clear_bit(0b1011, 9)
        0b1011
        >>> clear_bit(0b1011, -1)
        ValueError
    """
    if not bit >= 0:
        raise ValueError('Invalid bit ordinal indicator.')
    return value & ~(1 << bit)


# Function to perform shift left operation for CRC polynomial long-division
def shl_operation(value, bit, sequence):
    """Shifts given binary number (`value`) to the left by one, adds the
    selected bit (`bit`) from another binary number sequence (`sequence`)
    as the first (least significant) bit and returns the resulting number.

    Parameters:
    -----------
        value : int
            a binary number which will be shifted to the left as described
        bit : int
            ordinal indicator of the bit from the following sequence
        sequence : int
            a binary number from which the filling bit will be copied

    Returns:
    --------
        shl_operation(int, int, int) : int
            integer value of the new (resulting) binary number

    Raises:
    -------
        RuntimeError : if `bit` ordinal indicator is invalid

    Examples:
    ---------
        >>> shl_operation(0b1101, 2, 0b1011)
        0b1010
        >>> shl_operation(0b1101, 1, 0b1011)
        0b1011
        >>> shl_operation(0b1001, 2, 0b1011)
        0b10
        >>> shl_operation(0b1000, 2, 0b1011)
        0b0
        >>> shl_operation(0b1101, -1, 0b1011)
        RuntimeError
    """
    try:
        return (value << 1) | get_bit(sequence, bit)
    except ValueError as exc:
        raise RuntimeError('Failed to execute operation.') from exc


# Function to perform exclusive disjunction operation for CRC polynomial long-division
def xor_operation(value, bit, sequence):
    """Performs a XOR bit-wise operation on the given binary number (`value`)
    and another binary number sequence (`sequence`) if and only if the selected
    bit (`bit`) of the given number (`value`) is equal to 1, and returns the
    resulting number (equals `value` if the selected bit is equal to 0).

    Parameters:
    -----------
        value : int
            a binary number which will be the first operand in the XOR bit-wise operation
        bit : int
            ordinal indicator of the bit from `value` used to evaluate above condition
        sequence : int
            a binary number which will be the second operand in the XOR bit-wise operation

    Returns:
    --------
        xor_operation(int, int, int) : int
            integer value of the new (resulting) binary number

    Raises:
    -------
        RuntimeError : if `bit` ordinal indicator is invalid

    Examples:
    ---------
        >>> xor_operation(0b1001, 2, 0b1111)
        0b1001
        >>> xor_operation(0b1001, 2, 0b1100)
        0b101
        >>> xor_operation(0b1001, 1, 0b1111)
        0b1001
        >>> xor_operation(0b1001, 1, 0b1100)
        0b1001
        >>> xor_operation(0b1001, -1, 0b1111)
        RuntimeError
    """
    try:
        return value ^ sequence if get_bit(value, bit) else value
    except ValueError as exc:
        raise RuntimeError('Failed to execute operation.') from exc

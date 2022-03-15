from helper import get_bit, clear_bit, shl_operation, xor_operation
import logging
import time

def crc_check(sequence, generator):
  '''Performs a cyclic redundancy check (CRC) on the given information
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
  '''
  # Initiate cyclic redundancy check (CRC)
  logging.debug("CRC check started...")
  logging.debug("\t* encoded sequence:     {:b}".format(int(sequence)))
  logging.debug("\t* generator polynomial: {:b}".format(int(generator)))
  start_time = time.time()

  # Calculate length of generator & sequence bit-vectors
  generator_length = generator.bit_length()                       # generator polynomial (binary representation)
  sequence_length = sequence.bit_length()                         # encoded sequence (padded)
  payload_length = sequence_length - generator_length + 1         # encoded sequence (payload only)

  # Calculate remainder of encoded sequence division by the generator polynomial
  next_bit = sequence_length - generator_length - 1
  temp = sequence >> next_bit + 1
  while next_bit >= 0:                                            # iterate over the entire encoded sequence
    temp = xor_operation(temp, generator_length - 1, generator)   # calculate XOR result in each iteration
    temp = shl_operation(temp, next_bit, sequence)                # use long-division method to find remainder
    temp = clear_bit(temp, generator_length)                      # clear the oldest (most significant) bit
    next_bit -= 1
    logging.debug("\t- iteration #{}: remainder = {:{}b}".format(payload_length - 2 - next_bit, temp, generator_length))
  
  # Find remainder (equals 0 if no errors are detected)
  crc_check = xor_operation(temp, generator_length - 1, generator)

  # End Cyclic Redundancy Check (CRC) & return result
  end_time = time.time()
  logging.debug("CRC check took {} ms (RESULT = {:b}).".format(1000 * (end_time - start_time), crc_check))
  return crc_check

def crc_padding(sequence, generator):
  return sequence << generator.bit_length() - 1

def crc_decode(sequence, generator):
  '''Decodes a binary number (`sequence`) using the provided generator
  polynomial (`generator`), and returns a boolean value indicating
  whether there are errors in the original information sequence or not,
  based on the result of a cyclic redundancy check.

  Parameters:
  -----------
    sequence : int
      the original information sequence (a binary number) which will be encoded
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
  '''
  return crc_check(sequence, generator) == 0

def crc_encode(sequence, generator):
  '''Encodes a binary number (`sequence`) using the provided generator
  polynomial (`generator`), and returns the resulting (encoded) message.
  The original binary sequence is expanded (padding is added), and the
  appropriate suffix is added as a result of the cyclic redundancy check.

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
  '''
  sequence = crc_padding(sequence, generator)
  return sequence + crc_check(sequence, generator)

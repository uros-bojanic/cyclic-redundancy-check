# cyclic-redundancy-check
[Telecommunications] A Python library for cyclic redundancy check (CRC) using polynomial long division in GF(2).

Homework/project in **Fundamentals of Telecommunications (13E033OTR)** at the University of Belgrade, School of Electrical Engineering.

## CRC Library - crc_otr

This module provides users with cyclic redundancy check tooling under the `crc_otr` package - a Python library for cyclic redundancy check (CRC) using polynomial long division in GF(2).

### Installing

crc_otr can be installing using pip with:
```
pip install crc_otr
```

### Usage

`crc_decode(sequence, generator)` - Decodes a binary number (`sequence`) using the provided generator polynomial (`generator`), and returns a boolean value indicating whether there are errors in the original information sequence or not, based on the result of a cyclic redundancy check. If generator is not passed as an argument, CRC32 is used by default.
```
>>> crc_decode(0b11011010000, 0b10101)
False
>>> crc_decode(0b11011011011, 0b10101)
True
>>> crc_decode(0b1101010011110100101111101011011100111001000011010001)
True
```

`crc_encode(sequence, generator)` - Encodes a binary number (`sequence`) using the provided generator polynomial (`generator`), and returns the resulting (encoded) message. The original binary sequence is expanded (padding is added), and the appropriate suffix is added as a result of the cyclic redundancy check. If generator is not passed as an argument, CRC32 is used by default.
```
>>> crc_encode(0b1101101, 0b10101)
0b11011011011
>>> crc_encode(0b01100111, 0b11001)
0b11001110010
>>> crc_encode(0b11101010111010100110010101111010110101)
0b1110101011101010011001010111101011010111000111000111001000111111010010
```

## Cyclic Redundancy Check (CRC)

### Polynomial long division in GF(2)
Payload (data block) - original information sequence:
i(x) = 1101101
Generator polynomial - binary representation (reversed):
g(x) = 10101
GF(2) polynomial division remainder ```r(x) = i(x) % g(x)```:
r(x) = **1011**

For CRC, r(x) is used as a **check sequence** for given i(x) and g(x).

Encoded information sequence (payload || check sequence):
1101101**1011**

#### Example 1
```
 11011010000  ->  information sequence
^10101        ->  generator polynomial
 -----
 011100
 ^10101
  -----
  010011
  ^10101
   -----
   001100
   ^00000
    -----
    011000
    ^10101
     -----
     011010
     ^10101
      -----
      011110
      ^10101
       -----
       01011

rem. =  1011 (error detected)
```

#### Example 2
```
 11011011011  ->  information sequence
^10101        ->  generator polynomial
 -----
 011100
 ^10101
  -----
  010011
  ^10101
   -----
   001101
   ^00000
    -----
    011010
    ^10101
     -----
     011111
     ^10101
      -----
      010101
      ^10101
       -----
       00000
rem. =  0000 (no errors)
```

## Tests

### Manual test
```test.py``` provides a python program to manually test CRC on 3 sets of data blocks. To start manual test, run:
```
python test.py
```

Results of manual tests are provided as console output:
```
Decode (tests):
[ 11011010000] % [10101] -> False
[ 11011011011] % [10101] -> True
[   100100000] % [ 1101] -> False
[   100100001] % [ 1101] -> True
[ 11001110111] % [11001] -> False
[ 11001110010] % [11001] -> True
Encode (tests):
[     1101101] % [10101] -> 11011011011	# True
[      100100] % [ 1101] -> 100100001	# True
[     1100111] % [11001] -> 11001110010	# True
```

### Automatic test (benchmark)

```benchmark.py``` provides a python program to automatically test and assess the performance of CRC using random information sequences, and a set of commonly used generator polynomials (available in ```generators.py```). To start benchmark, run:
```
python benchmark.py
```

Results of benchmark are provided as console output, but are also conveniently available in ```benchmark.csv``` file.

### Benchmark analysis
```performance.py``` provides a python program to analyze and plot CRC benchmark results. To visualize CRC performance, run:
```
python performance.py
```

Results of the performance analysis are provided as 3D plot (```performance.gif```), with all PNG figures (frames) also available in ```benchmark_plot/``` folder.

from crc_otr import crc_decode, crc_encode

# CRC_DECODE - Manual Tests
print("Decode (tests):")
decode_tests = [
  (0b11011010000, 0b10101),
  (0b11011011011, 0b10101),
  (0b100100000, 0b1101),
  (0b100100001, 0b1101),
  (0b11001110111, 0b11001),
  (0b11001110010, 0b11001)
]
for d in decode_tests:
  test_seq = d[0]
  test_gen = d[1]
  test_res = crc_decode(sequence=test_seq, generator=test_gen)
  print("[{:12b}] % [{:5b}] -> {}".format(test_seq, test_gen, test_res))

# CRC_ENCODE - Manual Tests
print("Encode (tests):")
encode_tests = [
  (0b1101101, 0b10101),
  (0b100100, 0b1101),
  (0b1100111, 0b11001)
]
for e in encode_tests:
  test_seq = e[0]
  test_gen = e[1]
  test_res = crc_encode(sequence=test_seq, generator=test_gen)
  decoded = crc_decode(test_res, test_gen)
  print("[{:12b}] % [{:5b}] -> {:b}\t# {}".format(test_seq, test_gen, test_res, decoded))

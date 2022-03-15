# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Created By  : Uros Bojanic
# Created Date: 2022/03/14
# ---------------------------------------------------------------------------

# Function to return a list of commonly used CRC generator polynomials
def get_generators():
    return [bin((x << 1) + 1) for x in list(generators_hex.keys())]


# Source: https://en.wikipedia.org/wiki/Cyclic_redundancy_check
generators_hex = {
    0x1: 'CRC-1',
    0x5: 'CRC-3-GSM',
    0x9: 'CRC-4-ITU',
    0x14: 'CRC-5-EPC',
    0x1A: 'CRC-5-ITU',
    0x12: 'CRC-5-USB',
    0x33: 'CRC-6-CDMA2000-A',
    0x23: 'CRC-6-CDMA2000-B',
    0x2C: 'CRC-6-DARC',
    0x37: 'CRC-6-GSM',
    0x21: 'CRC-6-ITU',
    0x44: 'CRC-7',
    0x72: 'CRC-7-MVB',
    0xEA: 'CRC-8',
    0x97: 'CRC-8-AUTOSAR',
    0xD3: 'CRC-8-Bluetooth',
    0x83: 'CRC-8-CCITT',
    0x98: 'CRC-8-Dallas/Maxim',
    0x9C: 'CRC-8-DARC',
    0xA4: 'CRC-8-GSM-B',
    0x8E: 'CRC-8-SAE J1850',
    0xCD: 'CRC-8-WCDMA',
    0x319: 'CRC-10',
    0x3EC: 'CRC-10-CDMA2000',
    0x2BA: 'CRC-10-GSM',
    0x5C2: 'CRC-11',
    0xC07: 'CRC-12',
    0xF89: 'CRC-12-CDMA2000',
    0xE98: 'CRC-12-GSM',
    0x1E7A: 'CRC-13-BBC',
    0x2402: 'CRC-14-DARC',
    0x3016: 'CRC-14-GSM',
    0x62CC: 'CRC-15-CAN',
    0x740A: 'CRC-15-MPT1327',
    0x978A: 'CRC-16-Chakravarty',
    0xD015: 'CRC-16-ARINC',
    0x8810: 'CRC-16-CCITT',
    0xE433: 'CRC-16-CDMA2000',
    0x82C4: 'CRC-16-DECT',
    0xC5DB: 'CRC-16-T10-DIF',
    0x9EB2: 'CRC-16-DNP',
    0xC002: 'CRC-16-IBM',
    0xAC9A: 'CRC-16-OpenSafety-A',
    0xBAAD: 'CRC-16-OpenSafety-B',
    0x8EE7: 'CRC-16-Profibus',
    0x1B42D: 'CRC-17-CAN',
    0x18144C: 'CRC-21-CAN',
    0xAEB6E5: 'CRC-24',
    0xC3267D: 'CRC-24-Radix-64',
    0xC00031: 'CRC-24-WCDMA',
    0x30185CE3: 'CRC-30',
    0x82608EDB: 'CRC-32',
    0x8F6E37A0: 'CRC-32C',
    0xBA0DC66B: 'CRC-32K',
    0x992C1A4C: 'CRC-32K2',
    0xC0A0A0D5: 'CRC-32Q',
    0x8002410004: 'CRC-40-GSM',
    0xA17870F5D4F51B49: 'CRC-64-ECMA',
    0x800000000000000D: 'CRC-64-ISO'
}

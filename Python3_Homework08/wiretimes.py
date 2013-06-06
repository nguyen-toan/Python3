'''
Created on May 28, 2013
@author: tnguyen7

wiretimes.py: print the timestamp for each packet in seconds and microseconds from wireshark.bin
'''
import struct

f = open("wireshark.bin", "rb")
# Read through global header
f.read(24)
# Packet counter
packets = 0
while True:
    # Read packet header
    packet_header = f.read(16)
    if not packet_header:
        break
    # Get packet header content
    ts_sec, ts_usec, incl_len, orig_len = struct.unpack('=LLLL', packet_header)
    # Print out packet timestamp
    packets += 1
    print('[Packet %d] timestamp seconds=%s, microseconds=%s' % (packets, ts_sec, ts_usec))
    # Read through packet
    f.read(incl_len)

f.close()

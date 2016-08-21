#!/usr/bin/python
import struct
import sys
# each record is 10 least significant bits of 2 bytes, records are output in pairs
record_len = 4
records = 0
try:
	#with open(sys.stdin, 'r') as fh:
		fh = sys.stdin
		record = fh.read(record_len)
		while record != "":
			records += 1
			chan1, chan2 = struct.unpack("hh", record)
			if records % 10000 == 0:
				print("[%10d] 1 = %04d 2 = %04d" % (records, chan1, chan2))
			record = fh.read(record_len)
except KeyboardInterrupt:
	pass
print("read %d records" % records)

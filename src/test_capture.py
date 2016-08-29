#!/usr/bin/python
import struct
import sys
# each record is 10 least significant bits of 2 bytes, records are output in pairs
record_len = 4
records = 0
last_record = None
err_records = []
with open('processed', 'w') as out_fh:
#	with open('raw', 'r') as fh:
		fh = sys.stdin
		record = fh.read(record_len)
		while record != "":
			records += 1
			chan1, chan2 = struct.unpack("hh", record)
			if records % 10000 == 0:
				print("processed %d records" % records)
			if last_record:
				if last_record == 4095:
					if chan1 != 0:
						print("non sequential sample [%d] %d - %d = %d" % (records, chan1, last_record, chan1 - last_record))
						err_records.append(records)
				else:
					if chan1 - last_record != 1:
						print("non sequential sample [%d] %d - %d = %d" % (records, chan1, last_record, chan1 - last_record))
						err_records.append(records)
			out_fh.write("%d\n" % chan1)
			last_record = chan1
			record = fh.read(record_len)
			if records > 5000000:
				print("finishing early")
				break
print("read %d records" % records)
print("errors:")
print(err_records)

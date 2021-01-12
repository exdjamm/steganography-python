from utils import *

def get_two_bytes_significante(byte_array: bytearray) -> bytearray:
	result_bytearray = bytearray()

	for byte in byte_array:
		two_byte = 0x3 & byte

		result_bytearray.append(two_byte)

	return result_bytearray

def bytes_message_to_text(byte_message: bytearray) -> str:
	result_bytearray = bytearray()

	for index in range(0,len(byte_message), 4):
		range_byte = byte_message[index: index+4]
		run_byte_values = [i  for i in range(6, -2, -2) ]
		
		new_range_byte = [byte << run for (byte, run) in zip(range_byte, run_byte_values)]

		original_byte = sum(new_range_byte)
		
		result_bytearray.append(original_byte)

	return result_bytearray.decode('utf-8')

if __name__ == '__main__':
	info_file = ('output/img_message', 'jpeg')

	byte_array_file = read_bytes_file(info_file)
	byte_array_message = get_two_bytes_significante(byte_array_file)

	message = bytes_message_to_text(byte_array_message)
	print(message)
	
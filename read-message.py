from utils import *

def get_two_bytes_significante(byte_array: bytearray, len_message: int) -> bytearray:
	result_bytearray = bytearray()

	count_byte = 0
	for byte in byte_array:
		if count_byte == len_message -1:
			break

		two_byte = 0x3 & byte

		result_bytearray.append(two_byte)

		count_byte += 1

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
	len_message = int(input("Quantos caracteres tem a mensagem? >>> "))
	len_message *= 4

	info_file = ('output/img_message', 'jpeg')

	byte_array_file = read_bytes_file(info_file)
	byte_array_message = get_two_bytes_significante(byte_array_file, len_message)
	
	message = bytes_message_to_text(byte_array_message)
	print(message)
	
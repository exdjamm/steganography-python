from utils import *

def insert_message_into_bytes_file(byte_file, byte_message) -> bytearray:
	result_bytes = bytearray()

	count_byte = 1
	for (byte_m, byte_f) in zip(byte_message, byte_file):
		byte_f_corrected = ( (byte_f >> 2 ) << 2)  
		new_byte = byte_f_corrected | (byte_m)

		result_bytes.append(new_byte)

		count_byte += 1

	if count_byte < len(byte_file):
		result_bytes += byte_file[count_byte:] 

	return result_bytes

if __name__ == '__main__':
	info_file = ('input/img', 'jpeg')

	byte_file = read_bytes_file(info_file)[905:]
	
	byte_message = bytearray(input("Escreva a mensagem que queira colocar no arquivo >>> "), 'utf-8')
	split_byte_message = slit_message_into_two_sig_bytes(byte_message)

	result_bytes = insert_message_into_bytes_file(byte_file, split_byte_message)

	info_file = ('output/img_message', 'jpeg')
	write_bytes_to_file(info_file, result_bytes)	

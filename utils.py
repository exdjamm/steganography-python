def read_bytes_file(info_file: tuple) -> bytearray:
	file_path_name, file_extension = info_file
	PATH_FILE = f"{file_path_name}.{file_extension}"
	METHOD = 'rb'
	bytes_file = bytearray()

	with open(PATH_FILE, METHOD) as file:
		 content_file = file.read()
		 bytes_file = bytearray(content_file)

	return bytes_file

def write_bytes_to_file(info_file: tuple, file_bytearray: bytearray):
	"""
	info_file : tuple(str)
	contendo o nome do arquivo e sua extensão.

	bytes_file: bytearray
	contendo os bytes do arquivo a ser escrito.
	"""	
	file_path_name, file_extension = info_file
	PATH_FILE = f"{file_path_name}.{file_extension}"
	METHOD = 'wb'

	with open(PATH_FILE, METHOD) as file:
		file_bytes = bytes(file_bytearray)
		
		file.write(file_bytes)

def slit_message_into_two_sig_bytes(bytearray_message: bytearray):
	result_bytearray = bytearray()

	for byte in bytearray_message:
		two_bytes_1 = (byte & (2+1)) >> 0
		two_bytes_2 = (byte & (8+4)) >> 2 
		two_bytes_3 = (byte & (32+16)) >> 4 
		two_bytes_4 = (byte & (128+64)) >> 6 

		slit_bytes = [two_bytes_1, two_bytes_2,
					  two_bytes_3, two_bytes_4]

		slit_bytes.reverse()
		slit_bytes = bytearray(slit_bytes)

		result_bytearray += slit_bytes

	return result_bytearray


from termcolor import colored


def print_info(text: str):
	"""
	Provide an elegant way of printing text.

	:param text: The text to be printed.
	"""
	print(colored(text, 'white', attrs=['reverse']))


def get_password_length(min_length: int) -> int:
	"""
	Get password length from the user and evaluate its length and type.

	:param min_length: Minimum valid length for the password.
	:return: Validated length of the password.
	"""
	length = input(f'Please enter length of the password (atleast {min_length}): ')
	try:
		length = int(length)
		if length < min_length:
			length = min_length
	except ValueError:
		length = min_length

	return length

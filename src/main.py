from src.password_generator import (MemorablePasswordGenerator,
                                    PinCodeGenerator, RandomPasswordGenerator)
from src.utils import get_password_length, print_info


if __name__ == '__main__':
	while True:
		print('\n1. Pincode')
		print('2. Random Password')
		print('3. Memorable Password')
		user_request = input(f'\nPlease enter what kind of password you wish to generate, your options are (q to exit): ')

		if user_request.lower() == 'q':
			print_info('Goodbye')
			break
		elif not user_request in ['1', '2', '3']:
			print()
			print_info('Invalid input. you should enter one of the options: [1, 2, 3]')
			continue

		if user_request == '1':
			length = get_password_length(min_length=8)
			pin_code = PinCodeGenerator(length=length)
			password = pin_code.generate()
			print_info(f'Your password: {password}')
			break
		elif user_request == '2':
			length = get_password_length(min_length=8)
			numbers = input('If you want the password to include numbers enter Y otherwise enter any key: ')
			symbols = input('If you want the password to include symbols enter Y otherwise enter any key: ')

			if numbers.upper() == 'Y':
				numbers = True
			else:
				numbers = False

			if symbols.upper() == 'Y':
				symbols = True
			else:
				symbols = False

			random_password = RandomPasswordGenerator(length=length, numbers=numbers, symbols=symbols)
			password = random_password.generate()
			print_info(f'Your password: {password}')
			break
		elif user_request == '3':
			length = get_password_length(min_length=4)
			separator = input('Please enter the separator: (enter blank to use default "-"): ')

			if not separator.split():
				separator = '-'

			memorable_password = MemorablePasswordGenerator(length=length, separator=separator)
			password = memorable_password.generate()
			print_info(f'Your password: {password}')
			break

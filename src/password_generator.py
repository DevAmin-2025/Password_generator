import random
import string
from abc import ABC, abstractmethod


class PasswordGenerator(ABC):
	"""
	Abstract base class for password generators.

	Methods:
	- generate: Generate a password of the specified type.
	"""
	@abstractmethod
	def generate(self):
		"""
		Generate a password. this method should be implemented by subclasses.
		"""
		pass


class PinCodeGenerator(PasswordGenerator):
	"""
	Generate a PIN code of a specified length.

	:param length: Length of the PIN code.

	Methods:
	- generate: Generate a PIN code of the specified length.
	"""
	def __init__(self, length: int):
		self.numbers = string.digits
		self.length = length

	def generate(self) -> str:
		"""
		Generate a PIN code of the specified length.

		:return: A string representing the PIN code.
		"""
		return ''.join([random.choice(self.numbers) for _ in range(self.length)])


class RandomPasswordGenerator(PasswordGenerator):
	"""
	Generate a random password of a specified length.

	:param length: Length of the password.
	:param numbers: Whether to include numbers in password.
	:param symbols: Whether to include symbols in password.

	Methods:
	- generate: Generate a random password of the specified attributes.
	"""
	def __init__(self, length: int, numbers: bool, symbols: bool):
		self.length = length
		self.characters = string.ascii_letters
		if numbers is True:
			self.characters += string.digits
		if symbols is True:
			self.characters += string.punctuation

	def generate(self) -> str:
		"""
		Generate a random password of the specified length.

		:return: A string representing the password.
		"""
		while True:
			password = ''.join([random.choice(self.characters) for _ in range(self.length)])
			# Check if string.digits and string.punctuations are added to self.characters
			if '1' in self.characters and '!' in self.characters:
				flag_digit, flag_punc = False, False
				for i in password:
					if i in string.digits:
						flag_digit = True
					if i in string.punctuation:
						flag_punc = True

				if flag_punc and flag_digit:
					return password
				else:
					continue
			return password


class MemorablePasswordGenerator(PasswordGenerator):
	"""
	Generate a password of a specified number of words.

	:param length: Number of words in password.
	:param separator: Separator between the words, defaults to '-'.

	Methods:
	- generate: Generate a memorable password of the specified number of words.
	- build_data: Build the vocabulary list used as the main data for generating the password.
	"""
	def __init__(self, length: int, separator: str = '-'):
		self.length = length
		self.separator = separator
		self.vocabulary = self.build_data()

	def build_data(self) -> list:
		vocabulary = list()
		with open('data/vocabulary.txt') as f:
			for word in f:
				word = word.replace('\n', '')
				if len(word) >= 3:
					vocabulary.append(word)
		return vocabulary

	def generate(self) -> str:
		"""
		Generate a password of the specified number of words.

		:return: A string representing the password.
		"""
		return self.separator.join([random.choice(self.vocabulary) for _ in range(self.length)])

from translate import Translator

translator=Translator(to_lang='ja')
try:
	with open('./test.txt',mode='r') as my_file:
		text=my_file.read()
		Translation=translator.translate(text)
		with open('./test-ja.txt',mode='w') as my_file2:
			my_file2.write(Translation)
except FileNotFoundError as e:
	print('check your file path')
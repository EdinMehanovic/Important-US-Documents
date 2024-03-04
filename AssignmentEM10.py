from os import system, path, get_terminal_size
window_width = get_terminal_size().columns

from datetime import date
today = date.today().strftime("%B %d, %Y")
#########################################################################################
def header():
	system("cls||clear")
	print("\n\n"+"{0} {1}". format("Edin Mehanovic CIS125 Structure and Logic", today).center(window_width)+"\n\n")
#########################################################################################
def center(phrase):
	phrase = str(phrase)
	return ('%s'.center(get_terminal_size().columns-len(phrase))%phrase)
#########################################################################################
def input_center (phrase):
	return input("".ljust((window_width - len(phrase))//2)+ phrase)	
#########################################################################################
def formating_process(phrase):
	print(center("{0:<60} ".format(phrase)))
#########################################################################################
def wait():
	from msvcrt import getch
	from os import get_terminal_size
	print("Press any key to continue... ".center(get_terminal_size().columns))
	getch()
#########################################################################################
def read_file(my_file):
	global all_words
	all_words = []
	
	file = open(my_file)
	for line in file: 
		clean_str = ""
		line=line.strip().upper()
		for a in line:
			if a >= "A" and a <= "Z" or a == " ":
				clean_str += a
		words = clean_str.split(" ")
		all_words += words
		
	file.close()
	all_words.sort()
#########################################################################################
def file_check(my_file):
	if path.isfile(my_file):
		read_file(my_file)
	else:
		print((my_file +" does not exist!!!").center(window_width))
#########################################################################################
def input_america():
	# global number_input
	number_input = ""
	found = True
	print()
	while(found):
		found = False
		number_input = input_center("Choose the number of the document you wish to see: ")
		if number_input == "1":
			file_check("ArtCon.txt")
			
			
		elif number_input == "2":
			file_check("USCon.txt")
			
			
		elif number_input == "3":
			file_check("DoI.txt")
			
			
		elif number_input == "4":
			file_check("EmanProc.txt")
			
		else:
			print()
			formating_process(number_input + " is an invalid entry:\n\n")
			found = True	
########################################################################################		
def process_america():
	global amount, final_word
	amount = []
	final_word = []
	for y in all_words:
		if not y in final_word:
			final_word += [y]
			amount += [1]
		else:
			amount[-1] += 1
########################################################################################			
def output_american():
	rows = 0
	count = 0
	center_string = ""
	system ("cls||clear")
	print("\n\n\n")
	for a in range(len(amount)):
		count += 1 
		center_string += "{0:>4} {1:<20}".format(amount[a], final_word[a])
		if count % 5 == 0:
			print(center(center_string))
			center_string = ""
			rows += 1
			if rows % 30 == 0:
				wait()
				system ("cls||clear")
				print("\n\n\n")			
########################################################################################			
def main_bus(repeat = "y"):
	TAoC = "1. The Articles of Confederation "
	TUSC = "2. The United States Constitution "
	TUSDoI = "3. The United States Declaration of Independence "
	TEP = "4. The Emancipation Proclamation \n"
	if repeat == 'n' or repeat == 'N':
		print("\n\n\n")
		print(center('''"Have a nice day!"'''))
		input_center("Press <Enter> to continue... ")
		return
	elif repeat == "y" or repeat == "Y":
		header()
		formating_process(TAoC)
		formating_process(TUSC)
		formating_process(TUSDoI)
		formating_process(TEP)
		input_america()
		process_america()
		output_american()
		print()
		repeat = input_center("Would you like to run again (Y/N): ")
		main_bus(repeat)
	
	else:
		print("\n\n")
		print(center(repeat+" is an invalid entry\n\n"))
		repeat = input_center("Would you like to run again (Y/N): ")
		main_bus(repeat)


main_bus()

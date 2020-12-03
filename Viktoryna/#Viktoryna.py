#Viktoryna
# Игшра на выбор правильного ответа.
#  вопросы которой начинаются из тектстового файла vikwords.
import sys, pickle
from functools import reduce


def open_file(file_name, mode):
	""" open a file """
	try:
		the_file= open(file_name, mode, encoding='utf-8')
	except IOEerror as e:
		print("Не удалось получить доступ к файлу, возможно файл был удален.", file_name, "Рбаота программы будет завершена.\n,", e)
		input("Please push the Enter")
		sys.exit()
	else:
		return the_file
def next_line(the_file):
 	""" озварщает в отформатированном воиде очередную строгу кигрвогоо файла."""
 	line=the_file.readline()
 	line=line.replace("/", "\n")
 	return line


def next_block(the_file):
 	"""return block  informate in the file"""
 	category= next_line(the_file)
 	question=next_line(the_file)
 	answers=[]
 	for i in range(4):
 		answers.append(next_line(the_file))
 	correct=next_line(the_file)
 	if correct:
 		correct=correct[0]
 	explanation=next_line(the_file)
 	return category, question, answers, correct, explanation

def welcome(title):
 	""" пприветствует игрока и сообщает тему игры"""
 	print("\t\tДобро пожаловать в игру 'Викторина'!\n")
 	print("\t\t", title, "\n")


def main():
 	vikwords_file=open_file("vikwords.txt", "r")
 	title=next_line(vikwords_file)
 	welcome(title)
 	level=0
 	score=0
 	k=[]
 	p=[500, 1500, 2500 ]
 	category, question, answers, correct, explanation=next_block(vikwords_file)
 	while category and level!=3:
 		print(category)
 		print(question)
 		for i in range(4):
 			print("\t", i + 1, "-", answers[i])
 			# returnt input
 		answer=input("Ваш ответ:  ")
 		# check input
 		if answer == correct:
 			print("\nYes!", end=" ")
 			score+=1
 			level+=1
 			k.append(1)
 		else:
 			print("\nНет.", end=" ")
 			k.append(0)
 			level+=1		
 		print(explanation)
 		print("Счет: ", score, "\n\n")
 		
 		#  next answer
 		category, question, answers, correct, explanation =next_block(vikwords_file)
 	vikwords_file.close()
 	c=[x*y for x, y in zip(k,p)]
 	dollars=(reduce(lambda x, y: x+y, c))
 	print("Это был последний вопрос!")
 	print("На вашем счету: ", score, "points and " , dollars, "$")
 	name=str(input("Пожайлуста введите ваше имя: "))
 	save_rec=[score, dollars]
 	save_rec.append(name)
 	save_rec.reverse()
 	record=save_rec
 	print(record)
 	# records=open("records.dat", "ab+")
 	# pickle.dump(record, records)
 	# records.close()
 	# print("распаковка рекордов....")
 	# records=open("records.dat", "rb")
 	# record=pickle.load(records)
 	# print(record)
 	# print("Запаковка рекордов...")
 	# records.close()
 	records=open("records.txt", "a+")
 	records.writelines(f"{record}\n")
 	records.close()

 	
 	
 	# print (sum[500, 1500, 2500])


main()
input("\n\n Push the Enters")



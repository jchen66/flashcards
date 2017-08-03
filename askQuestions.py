import csv
import re
import sys
import random


path = '/Users/JiaYin/Desktop/Flashcards/'


def QuizMe(sName):
	##tmpPath=path+'DB_'+sName+'.csv'
	tmpPath="DB_"+sName+".csv"
	numQuestions=0
	allQuestions=[]
	correctQuestions=[]
	wrongQuestions=[]
	isSmart=False
	numAnswers=0
	cRow=0
	#first pass
	with open(tmpPath,'r') as quizFile:
		reader=csv.reader(quizFile)
		currentQuestion=0
		

		for row in reader:				
			tmpRow=row
			

			#skip first row
			#collect numAnswers here
			#numAnswers= total#columns -(id) -question -answer
			if cRow==0:
				cRow+=1
				numAnswers=len(row)-3
				continue
			numQuestions+=1
			
			#else: randomize the answers
			tmpChoices=[]
			
			allQuestions.append(row)

			#store temporarily the choices to randomize it
			for y in range(2, numAnswers+2):
				tmpChoices.append(tmpRow[y])
			#tmp store the answer
			tmpAns=tmpRow[numAnswers+2]

			random.shuffle(tmpChoices)

			#print question
			printQ=str(numQuestions)
			printQ+=". "+row[1]
			print(printQ)
			for x in range(1, numAnswers+1):
				print("     "+str(x)+'. '+tmpChoices[x-1])
			input_var=""
			ans=1
			isAnsValid=False

			#verify answer ()check if int && is between 1 and numQuestions
			while not isAnsValid:
				input_var=input('Your Answer: ')
				if not (isinstance(input_var,int)!=True):
					print("Invalid Answer. Please enter a number!")
					continue
				else:
					ans=int(input_var)
					if(ans>numAnswers or ans<1):
						print("Invalid Answer. Please enter a number between 1 and "+str(numAnswers)+"!")
						continue
					else:
						isAnsValid=True

			if tmpChoices[ans-1]==tmpAns:
				print("Correct Answer! Good Job!\n\n\n")

				correctQuestions.append(row)
			else:
				print("Wrong Answer! >:( \n\n\n")
				wrongQuestions.append(row)



	#check if any wrong questions
	if len(wrongQuestions)==0:
		isSmart=True
		print("Wow! You are so smart! You got all the questions right!")
	else:
		print("You only have "+str(len(correctQuestions))+" out of "+str(numQuestions)+" questions right! Let's study some more!")
	

	#secondpass, loops until you get all questions right
	while(isSmart!=True):
		nQ=0
		tmpQuestions=wrongQuestions
		#reset questions stats
		wrongQuestions=[]
		correctQuestions=[]
		for q in tmpQuestions:
			nQ+=1
			tmpChoices=[]
			#store temporarily the choices to randomize it
			for y in range(1, numAnswers):
				tmpChoices.append(q[y])
			#tmp store the answer
			tmpAns=q[numAnswers+1]

			random.shuffle(tmpChoices)


			#print question
			print(""+str(nQ)+". "+q[0])
			for x in range(1, numAnswers+1):
				print("     "+str(x)+'. '+tmpChoices[x-1])
			input_var=""
			ans=1
			isAnsValid=False

			#verify answer ()check if int && is between 1 and numQuestions
			while not isAnsValid:
				input_var=input('Your Answer: ')
				if not (isinstance(input_var,int)!=True):
					print("Invalid Answer. Please enter a number!")
					continue
				else:
					ans=int(input_var)
					if(ans>numAnswers or ans<1):
						print("Invalid Answer. Please enter a number between 1 and "+str(numAnswers)+"!")
						continue
					else:
						isAnsValid=True

			if tmpChoices[ans-1]==tmpAns:
				print("Correct Answer! Good Job!\n\n\n")
				correctQuestions.append(q)
			else:
				print("Wrong Answer! >:( \n\n\n")
				wrongQuestions.append(q)
		if (len(wrongQuestionss)==0):
			isSmart=True

	print("Wow you finished answering all the questions!! You are ready to ace that test! :D ")

print(sys.argv[1])
QuizMe(str(sys.argv[1]))






			









       
	

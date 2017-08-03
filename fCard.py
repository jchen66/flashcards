#!/usr/bin/python
import csv
import re
import sys


path = '/Users/JiaYin/Desktop/Flashcards/'

def printMainMenu():
	print('    ++ Menu ++')
	print('1. Add Subject')
	print('2. List all Subjects')
	print('3. Choose Subject')
	print('4. Quit')

	input_var=input('Choose Action: ')
	return input_var

def printAddSubjMenu():
	print('   ++ Add Subject Menu ++')
	print('1. Enter "return" for Main Menu')

	input_var=input('Subject Name: ')
	return input_var

def printChooseSubjMenu():
	print('  ++ Choose Subject Menu ++')
	print('1. Enter "return" for Main Menu')

	input_var=input('Subject Name: ')
	return input_var


def printListSubjMenu():
	print('  ++ List of all Subjects ++')
	subj=None
	num=1
	with open('subjectNames.txt') as f:
		subj=f.readlines()

	for s in subj:
		tmp=s.strip()
		print(num+'. '+tmp)
		num=num+1
	print(num+'. Type "return" for Main Menu')
	input_var=input('Enter Subject Name: ')

	return input_var

def subjExist(sName):
	try:
		tmp=open(sName,'rw')
		return True
	except:
		print("The Subject: '"+sName+"' DNE. Please create one")
		return False


def printSubjMenu(sName):
	print('  ++ Subject: '+sName+' ++')
	print('1. Test me!')
	print('2. Add Flashcards')
	print('3. Delete Subject')
	print('4. Return to Main Menu')







with open(path,'r',encoding="utf-8") as origFile:
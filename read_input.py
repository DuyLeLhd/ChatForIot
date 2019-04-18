import os


class readInputData():
	def read_input():
		read_ = open("input.txt","r",encoding = 'utf-8')
		read_ = read_.read()
		read_ = read_.lower()
		
		return read_

if __name__ == '__main__':
	
	readInputData.read_input()


import math
from random import shuffle

def generateList(f, s):
	slist = []
	if s != 0:
		num = math.ceil(len(f)/s)
	else:
		slist.append(f)
		return slist

	tempstr = ""
	midpos = 0
	end = len(f)
	while midpos < end:
		pos = 0
		while pos < midpos:
			tempstr = tempstr+'_'
			pos += 1

		for char in range(num):
			try:
				tempstr = tempstr+f[pos]
				pos += 1
			except:
				pass

		while pos < end:
			tempstr = tempstr+'_'
			pos += 1

		slist.append(tempstr)
		tempstr = ""
		midpos += num
	shuffle(slist)
	return slist

def main():
	fullpass = input("Input secret word: ")
	splitnum = int(input("How many splits? "))

	splitlist = generateList(fullpass, splitnum)
	shuffle(splitlist)
	f = open("pass.txt","w")
	
	for word in splitlist:
		f.write(word+"\n")
	print("Successfully sent to file")

main()
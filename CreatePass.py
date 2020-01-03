import math
import random

def generateList(f, s):
	slist = []
	if s != 0:
		num = math.ceil(len(f)/int(s))
	else:
		slist.append(f)
		return slist

	'''
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
	'''

	# pick indexes at random from list of nums
	numlist = []
	for i in range(len(f)): # generate num list
		numlist.append(i)

	stringlist = []
	templist = []
	while len(numlist) > 0:
		print("num:",num)
		for i in range(num):
			print("len of numlist:", len(numlist))
			if len(numlist) != 0:
				templist.append(numlist.pop(random.randint(0,len(numlist)-1))) #grab a random number and put it on the templist
		slist.append(templist)
		templist = []

	# sort each list
	for lists in slist:
		lists.sort()
	
	# assign each val to a password char
	finallist = []
	for nums in slist: # go through each numlist comparing them to each char in f, if index isn't in numlist then replace with an '_'
		for letter in range(len(f)):
			if not letter in nums:
				templist.append("_")
			else:
				templist.append(f[letter])
		finallist.append("".join(templist))
		templist = []
	return finallist

def main():
	fullpass = input("Input secret word: ")
	splitnum = int(input("How many splits? "))

	splitlist = generateList(fullpass, splitnum)
	fi = open("pass.txt","w")

	for word in splitlist:
		fi.write(word)
		fi.write("\n")
	print("Sent to file (pass.txt)")

main()

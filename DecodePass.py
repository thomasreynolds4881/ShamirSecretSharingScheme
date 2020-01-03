# Get data from pass.txt
file = open('pass.txt','r')
passlist = file.read().splitlines()
file.close()

# Create finalpass list
finalpass = []
for i in passlist[0]:
	finalpass.append('_')

# Update the finalpass list every time there's a new character to replace a '_'
j = 0
overlapconflict = False
lengthconflict = False
for i in passlist: # go through passlist
	index = 0
	for j in i: # go through each string in passlist
		if j != '_':
			try:
				if j == finalpass[index] or finalpass[index] == '_':
					finalpass[index] = j
				else:
					# warning happens when two chars share an index
					conflict = True
					finalpass[index] = '?'
			except:
				# warning happens if a string is longer than a previous string (but if it's shorter it can be resolved)
				lengthconflict = True
				break

		index += 1

# print warning messages
if "_" in finalpass:
	print("WARNING: unable to fully decipher")

if lengthconflict:
	print("WARNING: inconsistent string lengths; result may be inaccurate")

if overlapconflict:
	print("WARNING: conflicts in data have been found and are marked with \'?\'")
 
print("".join(finalpass))

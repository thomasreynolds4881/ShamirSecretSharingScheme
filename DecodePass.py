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
conflict = False
for i in passlist: # go through passlist
	index = 0
	for j in i: # go through each string in passlist
		if j != '_':
			if j == finalpass[index] or finalpass[index] == '_':
				finalpass[index] = j
			else:
				conflict = True
				finalpass[index] = '?'
		index += 1

if "_" in finalpass:
	print("WARNING: unable to fully decipher")

if conflict:
	print("WARNING: conflicts in data have been found and are marked with \'?\'")
 
print("".join(finalpass))

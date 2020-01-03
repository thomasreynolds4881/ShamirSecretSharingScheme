# Get data from pass.txt
file = open('pass.txt','r')
passlist = file.read().splitlines()
file.close()
print(passlist)

# Create finalpass list
finalpass = []
for i in passlist[0]:
	finalpass.append('_')

# Update the finalpass list every time there's new data
j = 0
for i in passlist: # go through passlist
	index = 0
	for j in i: # go through each string in passlist
		if j != '_':
			finalpass[index] = j
		index += 1
 
print("".join(finalpass)) 
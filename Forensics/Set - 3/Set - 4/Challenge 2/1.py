with open('swap.png','rb') as f:
	buff = f.read()

buff = buff[::-1]

temp = ""

for i in range(1,len(buff)):

	if i%2 != 0:
		temp += buff[i]
		temp += buff[i-1]

with open("final.png", "wb") as g:
    g.write(temp)
    g.close()
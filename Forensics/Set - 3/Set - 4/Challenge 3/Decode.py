from zipfile import ZipFile

text=""

for i in range(1000):
    filename=""
    filename = "fix"
    filename+=str(i)
    filename+=".zip"
    
    with open(filename,'rb') as f:
	    buff = f.read()

    temp = ""

    for j in range(0,len(buff)):
	    if j == 0:
		    temp += "P"
		    continue
	    if j == 1:
		    temp += "K"
		    continue
	    if j == 2:
		    temp += ""
		    continue
	    if j == 3:
		    temp += ""
		    continue
		 
	    temp += buff[j]
    temp1 = temp[:137]
    #temp2 = temp[137:141]
    temp3 = temp[141:]
    temp4 = "504b0506".decode("hex")

    temp = ""
    temp += temp1
    temp += temp4
    temp += temp3

    with open(filename, "wb") as g:
	g.write(temp)
	g.close()

    with ZipFile(filename, 'r') as zip:
	zip.extractall()

    with open('text','r') as f:
	text+= f.read()


print(text)
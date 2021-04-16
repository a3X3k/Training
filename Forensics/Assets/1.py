filename = 'revers.me'
f = open("1.txt", "w") 

for line in open(filename, 'r'):
 
	line = line[::-1] 
	f.writelines(line) 
  
f.close()


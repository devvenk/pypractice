f = open(r'C:\Users\Venky\Dropbox\001_SockDoc.txt', "r")
contents = f.read()
f.close()
for line in contents:
	print (line, end='')

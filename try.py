fw = open('sample.txt','w')
fw.write('asdasdasdadsdas\n')
fw.write('I am Ishan\n')
fw.close()


fr = open('sample.txt','r')
text=fr.read()
print(text)
fr.close()
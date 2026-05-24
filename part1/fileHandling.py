#FILE HANDLING 


#OPENING A FILE 
#TAKES TWO ARGUMENT ONE IS FILE NAME AND OTHER IS MODE OF FILE 
#f=open('myfile.txt','r')


#PRINTING A FILE 
#text=f.read()
#print(text)
#f.close

#OPENING FILE IN READ AND BINARY MODE 
'''f=open('myfile.txt','rb')
text=f.read()
print(text)'''

#WRITING A FILE 
'''f=open('myfile.txt','w')
f.write('nice to meet you')
f.close()'''


#APPEND IN FILE
'''f=open('myfile.txt','a')
f.write('nice to meet you ')
f.close()'''


#WITH FUNCTION 
'''f=open('myfile.txt','a')
with open('myfile.txt','a'):
    f.write("hey i am here")'''


#READLINE METHOD IN PYTHON 
#TO READ A FILE LINE BY LINE 
'''f=open('myfile.txt','r')
while True:
    line=f.readline()
    if not line:
        break
    print(line)'''
'''f=open('myfile.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(line)'''


#WRITELINES METHOD IN PYTHON
'''f=open('myfile.txt','w')
lines=['line 1\n','line 2\n','line 3\n']
f.writelines(lines)
f.close'''


#SEEK AND TELL FUNCTIONS
'''with open('myfile.txt','r') as f:
    print(type(f))
    #MOVE TO THE 10TH BYTE IN THE FILE
    f.seek(10)
    #READ THE NEXT 5 BYTES
    print(f.tell())    #TELL US THE POSITION OF SEEK
    data=f.read(5)
    print(data)'''


#TRUNCATE METHOD 
#IT LIMITS THE SIZE OF FILE 
'''with open('myfile.txt','w') as f:
    f.write('hello world!')
    f.truncate(5)

with open('myfile.txt','r') as f:
    print(f.read())'''









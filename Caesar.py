cipher=input('Enter the cipher:: ')
key=int(input('Enter the key:: '))
alphabets={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',10:'J',11:'K',12:'L',13:'M',14:'N',15:'O',16:'P',17:'Q',18:'R',19:'S',20:'T',21:'U',22:'V',23:'W',24:'X',25:'Y',26:'Z',27:' '}
temp=[]
decipher=''
for x in range(27-key,27):
	temp.append(alphabets[x])
for y in range(1,27-key):
	temp.append(alphabets[y])
temp.append(' ')
for z in cipher:
	decipher=decipher+alphabets[temp.index(z)+1]
print('The hidden message is:: '+decipher)
#print(temp)





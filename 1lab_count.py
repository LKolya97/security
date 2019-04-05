def findMax( count):
    i=0
    answer=[0,0,0,0,0]
    a0=0
    a1=0
    a2=0
    a3=0
    a4=0
    while i<len(count):
        if count[i]>=a0:
            a4=a3
            a3=a2
            a2=a1
            a1=a0
            answer[4] = answer[3]
            answer[3] = answer[2]
            answer[2]=answer[1]
            answer[1]=answer[0]
            a0=count[i]
            answer[0]=i
        elif count[i]>=a1:
            a4=a3
            a3=a2
            a2=a1
            a1=count[i]
            answer[4]=answer[3]
            answer[3]=answer[2]
            answer[2]=answer[1]
            answer[1]=i
        elif count[i]>=a2:
            a4=a3
            a3=a2
            a2=count[i]
            answer[4]=answer[3]
            answer[3]=answer[2]
            answer[2]=i
        elif count[i]>=a3:
            a4=a3
            a3=count[i]
            answer[4]=answer[3]
            answer[3]=i
        i=i+1
    return answer
def CaesarCipherChar(c,k):
    if alp.find(c)!=-1:
        if alp.index(c)+k>25:
            a=alp[(alp.index(c)+k)%26]
        else:
            a=alp[alp.index(c)+k]
    elif  alph.find(c)!=-1:
        if alph.index(c)+k>25:
            a=alph[(alph.index(c)+k)%26]
        else:
            a=alph[alph.index(c)+k]
    else:
        a=c
    return a
def CaesarCipher(S,k):
    S1=""
    i=0
    while i < len(S):
        S1=S1+CaesarCipherChar(S[i],k)
        i+=1
    return S1
alp="abcdefghijklmnopqrstuvwxyz"
alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
f=open('output.txt', 'r')
f1=open('book.txt', 'r')
f2=open('uncrypt.txt','w')
symb=f.read(1)
count=[]
if alph.find(symb)!=-1:
    symb=alp[alph.find(symb)]    
count.append(0)
S=symb
while symb:
    if alph.find(symb)!=-1:
        symb=alp[alph.find(symb)]  
    if S.find(symb)==-1 and alp.find(symb)!=-1:
        S+=symb
        count.append(0)
    elif alp.find(symb)!=-1:
        count[S.find(symb)]+=1   
    symb=f.read(1)

#i=0
#while i<len(count):
  # print(S[i],"-",count[i])
   #i+=1
answer=[]
answer=findMax(count)
print("Наиболее часто вречающиеся буквы в зашифрованном тексте: ",S[answer[0]],S[answer[1]], S[answer[2]],S[answer[3]], S[answer[4]])
symb=f1.read(1)
count=[]
if alph.find(symb)!=-1:
    symb=alp[alph.find(symb)]
count.append(0)
S1=symb
while symb:
    if alph.find(symb)!=-1:
        symb=alp[alph.find(symb)]
    if S1.find(symb)==-1 and alp.find(symb)!=-1:
        S1+=symb
        count.append(0)
    elif alp.find(symb)!=-1:
        count[S1.find(symb)]+=1
    symb=f1.read(1)

#i=0
#while i<len(count):
   #print(S1[i],"-",count[i])
   #i+=1
answer1=[]
answer1=findMax( count)
print("Наиболее часто вречающиеся буквы в исходном тексте: ",S1[answer1[0]],S1[answer1[1]], S1[answer1[2]],S1[answer1[3]], S1[answer1[4]])

f.close()
f=open('output.txt','r')
dif=alp.find(S1[answer1[0]])-alp.find(S[answer[0]])
dif=dif%26
ans=""
symb=f.read(1)
while symb:
    S=symb
    ans=ans+CaesarCipher(S,dif)
    symb=f.read(1)
f2.write(ans)
f1.close()
f.close()
f2.close()
f=open('output.txt', 'r')
symb=f.read(2)
countby=[]
S=""
if alph.find(symb[0])!=-1:
    symb=alp[alph.find(symb[0])]+symb[1]
if alp.find(symb[0])!=-1 and alp.find(symb[1])!=-1:
 countby.append(1)
 S=symb
ad=f.read(1)
symb=symb[1]+ad
while ad:
    if alph.find(symb[0])!=-1:
        symb=alp[alph.find(symb[0])]+symb[1]
    if S.find(symb)==-1 and alp.find(symb[0])!=-1 and alp.find(symb[1])!=-1:
        S+=symb
        countby.append(1)
    elif alp.find(symb)!=-1:
        countby[int(S.find(symb)/2)]+=1
    ad=f.read(1)
    if ad:
        symb=symb[1]+ad
       # print(symb)
i=0
f.close()
answerby=[]
print("Самые частые биграммы в зашифрованном тексте")
answerby=findMax(countby)
while i<len(answerby):
 print(S[answerby[i]*2],S[answerby[i]*2+1]," ",end=" ")
 i=i+1
f=open('book.txt', 'r')
symb=f.read(2)
countby=[]
Sby=""
if alph.find(symb[0])!=-1:
    symb=alp[alph.find(symb[0])]+symb[1]
if alp.find(symb[0])!=-1 and alp.find(symb[1])!=-1:
 countby.append(1)
 Sby=symb
ad=f.read(1)
symb=symb[1]+ad
while ad:
    if alph.find(symb[0])!=-1:
        symb=alp[alph.find(symb[0])]+symb[1]
    if Sby.find(symb)==-1 and alp.find(symb[0])!=-1 and alp.find(symb[1])!=-1:
        Sby+=symb
        countby.append(1)
    elif alp.find(symb)!=-1:
        countby[int(Sby.find(symb)/2)]+=1
    ad=f.read(1)
    if ad:
        symb=symb[1]+ad

i=0
f.close()
answerby1=[]
answerby1=findMax(countby)
print("\nСамые частые биграммы в исходном тексте")
while i<len(answerby):
 print(Sby[answerby1[i]*2],Sby[answerby1[i]*2+1]," ",end=" ")
 i=i+1
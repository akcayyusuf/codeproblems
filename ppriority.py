inp = input()


operators=[]
terms=[]

for i in range(len(inp)):
    if inp[i]=="*" or inp[i]=="/" or inp[i]=="+" or inp[i]=="-" :
        operators.append(inp[i])


inp=inp.replace("*",",")
inp=inp.replace("/",",")
inp=inp.replace("+",",")
inp=inp.replace("-",",")

inp =inp.split(",")

print(inp)
print(operators)
i=0
while i<len(operators):
    if operators[i]=="*":
        inp[i]=float(inp[i])*float(inp[i+1])
        operators.pop(i)
        inp.pop(i+1)
        i-=1
    i+=1
    print(inp)
    print(operators)
i=0
while i<len(operators):
    if operators[i]=="/":
        inp[i]=float(inp[i])/float(inp[i+1])
        operators.pop(i)
        inp.pop(i+1)
        i -= 1
    i+=1
    print(inp)
    print(operators)

i=0
while i<len(operators):
    if operators[i]=="+":
        inp[i]=float(inp[i])+float(inp[i+1])
        operators.pop(i)
        inp.pop(i+1)
        i -= 1
    i+=1
    print(inp)
    print(operators)
i=0
while i<len(operators):
    if operators[i]=="-":
        inp[i]=float(inp[i])-float(inp[i+1])
        operators.pop(i)
        inp.pop(i+1)
        i -= 1
    i+=1
    print(inp)
    print(operators)



print(inp)
print(operators)
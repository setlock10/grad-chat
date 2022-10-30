with open("raw-chat.data", mode='r') as f:
    content = f.readlines()
# print(content)

# print(len(content))

# for x in range(0,len(content),2):
#     print(content[x])
list=[]
for x in content:
    key = x.split(' ')
    if key[0]=="From":
        list.append(key[1]+" "+key[2])
       

list.sort()
sifted=[]
sifted.append(list[0])
# print (sifted)


prev=list[0]

for x in range(1,len(list)):
    if list[x]!=prev:
        sifted.append(list[x])
    prev=list[x]



# print(list)
# print(sorted)
print(sifted)
print(len(sifted))

with open("chat-names.txt", mode='w') as f:
    # print(sifted)
    for x in sifted:
        f.write('User.create(nickname: "'+x+'", username: "ABC", password:"procoder")'+ "\n")








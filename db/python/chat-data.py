
# Read in entire text file 
with open("raw-chat.data", mode='r') as f:
    content = f.readlines()

# Open output file
f=open("chat-data.json", "w")

# Create empty array (list)
list=[]


for x in range(0, len(content)):
    line1=content[x].strip()
    key = line1.split(' ')
    if key[0]=="From":
        f.write('{\n    "name":'+'"'+(key[1]+" "+key[2])+'"'+",\n")
        f.write('    "time":"'+key[5]+'",\n')
#         list.append(key[1]+" "+key[2])
    # else:
        # f.write('    "message":"'+y+'"'+"\n},\n")
        line2=content[x+1].strip()
        line3=content[x+2].strip()
        key3 = line3.split(' ')
        if key3[0]!="From":
            # f.write('    "message":"'+line2+"\n" + line3+'"},\n')
            f.write('    "message":"'+line2+'"'+",\n")
            f.write('    "message2":"'+line3+'"'+"\n},\n")

        else:
            f.write('    "message":"'+line2+'"'+"\n},\n")


       

# list.sort()
# sifted=[]
# sifted.append(list[0])
# # print (sifted)

f.close()


# prev=list[0]

# for x in range(1,len(list)):
#     if list[x]!=prev:
#         sifted.append(list[x])
#     prev=list[x]



# # print(list)
# # print(sorted)
# print(sifted)
# print(len(sifted))





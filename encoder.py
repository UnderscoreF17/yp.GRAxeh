string = "kaishimibenchiscool"
key = 2

# What you need to input -^

string_split = []
length = len(string)
for letter in string:
    string_split.append(letter)
string_result = []
for i in range(1,key+1,1):
    string_result.append(string[length-i])
    string_split.pop()

for i in range(0,length-key,1):
    string_result.append(string[i])

temp = []
for i in range(0,(length//5),1):
    for j in range(0,5,1):
        temp.append(string_result[(i*5)+j])
for i in range(0,length%5, 1):
    temp.append(string_result[((length//5)*5)+i])

encoded = []
add = 0
sub = 1
for j in range(0,5,1):
    for i in range(0,(length//5)+1,1):
        encoded.append(temp[add])
        if (add+5) > length-1:
            add = add - i*5  + sub
            break
        else:
            add += 5
encoded = ''.join(encoded)

import os

# r = Read
# a = Append
# w = Wrute
# x = Create

#Read -error if doesn't exist

f = open("names.txt")
print(f.read())
print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("names.txt")
    print(f.read())
except:
    print("The file you want to read doesnt exist")
finally:
    f.close()        


#Append - create ther file if it doesnt exist
f = open("names.txt", "a")
f.write("Neil")
f.close()

f = open("names.txt")
print(f.read())
f.close()  

#Write (overwrite)
f = open("context.txt", "w")
f.write("I delete all of context")
f.close()

f = open("context.txt")
print(f.read())
f.close()

#Two ways to create a new file

#Opens a dile for writing, creates the file if it does not exist
f = open("name_list.txt" ,"w")
f.close()

#Creates the specefied file , but returns an error if the file exist

if not os.path.exists("ellis.txt"):
    f = open("ellis.txt", "x")
    f.close()

# Delete a file 
# 
# avoid a error if it doesnt existt
if os.path.exists("ellis.txt"):
    os.remove("ellis.txt")
else:
    print("The file you wish to delete does not exist")        

with open("more_names.txt") as f:
    content = f.read()

with open("names.txt", "w") as f:
    f.write(content)
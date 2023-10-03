import math 

# String data type

# literal assigment
first = "ellis"
last = "velandia"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Constructor function

# pizza = str("pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))


# Concatenation

fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

#casting a number to a string
decade = str(1993)
print(type(decade))
print(decade)

statement = "I like rock musisc from the " + decade + "s."
print(statement)

#Multiples lines
multiline= '''
hyey, how are you?

I was just cheking in.
 
                  All good?
'''

print(multiline)

#Escaping special characteres

sentence = 'I\'m back at work!\they!\n\nWhere\'s this at\\located?'
print(sentence)


#String Methods

print(first)
print(first.lower())
print(first.upper())
print(first.capitalize())

print(multiline.title())
print(multiline.replace("good", "ok"))
print(len(multiline))

print(len(multiline))
multiline += "                                              "
multiline = "                                                " + multiline
print(len(multiline))


print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")
#Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16,".") + "$1".rjust(4))
print("Muffi".ljust(16,".") + "$2".rjust(4))
print("Cheesecake".ljust(16,".") + "$4".rjust(4))

print("")

#string index values
print(first[0].upper())
print(first[1])
print(first[2])
print(first[3])
print(first[-1])

# some methos retunr booleean data
print(first.startswith("A"))
print(first.endswith("s"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# NUmeric data types
price = 100
best_price = int(80)

print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# comples type
comp_value =  5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))

print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# Cating a string to a number
zipcode = "100001"
zip_value = int(zipcode)
print(type(zip_value))
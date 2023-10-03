users = ["Ellis", "Chirs", "Maria"]

data = ["crisanto", 30 , True]

emptylist = []

print("Ellis" in data)

print(users[0])
print(users[-1])
print(users[-2])
print(users.index("Maria"))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(users))


users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(["Robert", "Jimmy"])
print(users)

users.extend(data)
print(users)

users.insert(0,"Bob")
print(users)

users[2:2] = ["Eddie", "Alex"]
print(users)

users[1:3] = ["Robert", "Jpj"]
print(users)


users.remove("Bob")
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

# del data
data.clear()
print(data)

# users[1:2] = ["dave"]
# users.sort()
# print(users)

# users.sort(key=str.lower)
# print(users)

nums = [4,25,78,5,20]
nums.reverse()
print(nums)
# nums.sort(reverse=True)
print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil",True ])
print(mylist)

#Tuples
mytuple = tuple(("Ellis", 30 , True))

anothertuple = (1,4,2,8)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append("Neil")
newtuple = tuple(newlist)
print(newtuple)

(one,*two, hey) = anothertuple
print(one)
print(two)
print(hey)
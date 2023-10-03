band = {
    "vocals" : "Plant",
    "guitar" : "Page"
}

band2 = dict(vocal="plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(type(band2))

#Access items
print(band["vocals"])
print(band.get("guitar"))

#list all keys
print(band.keys())

#list all values
print(band.values())

#list of key/ value pairs as tuples
print(band.items())

# verufy a key exits
print("guitar" in band)
print("triangle" in band)

# change values
band["vocals"] = "Coverdale"
band.update({"bass" :  "JPJ "})

print(band)

#Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())
print(band)

#Delete and clear

band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

# copy dictionaries
# band2 = band # create a reference
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Ellis"
# print(band)

band2 = band.copy()
band2["drums"] = "ellis"
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("Good copy")
print(band3)



#Nested dictionaries

member1 = {
    "name": "tom",
    "instrument": "guitar"
}
member2 = {
    "name": "travis",
    "instrument": "drummer"
}

band = {
    "member1": member1,
    "member2": member2
}

print(band)
print(band["member1"]["name"])

#sets

nums = {1 ,2, 3, 4}
nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#no duplicates 
nums = { 1 ,2, 2, 3}
print(nums)

#True is a dupe of 1 , False es a dupe of  0
nums = {1 ,True, 2, False, 3 , 4 , 0}
print(nums)

#check if a value is in a set
print(2 in nums)

#but you cannot refer to an element in the with an index position or a key

# A dd a new element to a set 
nums.add(8)
print(nums)

# Add elements form one set to another 
morenums = {5,6,7}
nums.update(morenums) 
print(nums)

# you can use update with list , tuples , adn dictionaroes too

# Merge two sets to create a new set
one = {1,2,3}
two = {5,6,7}


mynewset = one.union(two)
print(mynewset)

#keep only the duplicates
one = {1,2,3}
two = {2,3,4}

one.intersection_update(two)
print(one)

#keep everything except the duplicates
one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one)

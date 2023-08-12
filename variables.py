# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 10
myfloat = 9.9
mystr = "This is a string"
mybool = True
mylist = [0, 1, "nine", 5.2, False]
mytuple = (0, 1, 2) # immutable, can not change it
mydict = {"name" : "Valentin", "height" : 189, "Exercises":["hiking", "riding a bike", "sleepin"]}

# Multiple assignments
mya = myb = myc = 100

# Multiple values assigned to multiple variables
a, b, c = "alpha", "beta", 42

print(myint)
print(type(myint))
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(type(mytuple))
print(mydict)

# re-declaring a variable works
mya = "abc"
print (mya)

# to access a member of a sequence type, use []
print(mylist[2])
print(mytuple[1])
# use slices to get parts of a sequence
print(mylist[1:4:2])
# you can use slices to reverse a sequence
print(mylist[::-1])

# dictionaries are accessed via keys
print(mydict["name"]) 

# ERROR: variables of different types cannot be combined
#print ("string type " + 123)
print ("string type " + str(123))

# Global vs. local variables in functions
def someFunction():
    #global mystr
    mystr = "def"
    print (mystr)

someFunction()
print (mystr) 

del mystr

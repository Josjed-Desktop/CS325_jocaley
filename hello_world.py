import random

code = ["miniconda", "packages", "pushing to git", "python"]

print("Hello World!\n")

print ("This for CS325")
print ("We are testing out:")
for x in code:
    print(x)
for y in code:
    random.seed(y)
    print(random.random())
import os

# Step 1
f = open("file.txt", "r")

# Step 2
print(f.read())

# Step 3
print(f.readline())

# Step 4
for x in f:
    print(x)
f.close()

# Step 5
if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("File does not exist.")
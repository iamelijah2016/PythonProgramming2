# f = open("file.txt", "x")

# f = open("file.txt", "w")
# f.write("This is a sample text file")

f = open("file.txt", "a")
f.write("\nThis is a another line")

f = open("file.txt", "r")
print(f.read())
f.close()
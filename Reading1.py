#reading files
print("Reading files")
print("-----------------------------------------------")

a = open("demo.txt", "r")
print(a.read())

print("-----------------------------------------------")
print("Reading files - Readingline()")

a = open("demo.txt", "r")
print(a.readline())
a.close()

print("-----------------------------------------------")

a = open("demo.txt", "r")
print(a.read(7))

print("-----------------------------------------------")
print("Reading files - `with`")

with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)

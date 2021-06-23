#reading files
print("-----------------------------------------------")

with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)

a = open("demo.txt", "w")
a.write("what has happned now?")
a.close()


print("-----------------------------------------------")

with open("demo.txt") as myfile:
    contents = myfile.read()
    print(contents)

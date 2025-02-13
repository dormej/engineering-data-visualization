import sys

print("zad1")
list = []
for i in range (1,100):
    if (i%4 == 0):
        list.append(i)
file1 = open("ex1.txt", "w")
file1.write(str(list))
file1.close()

print("\nzad2")

file1 = open("ex1.txt","r")
divisible_by_4 = file1.read()
print(divisible_by_4)
file1.close()

print("\nzad3")
text = "\nNumbers divisible by 4."

with open ("ex1.txt", "a+") as file1:
    file1.write(text)
    print(text)
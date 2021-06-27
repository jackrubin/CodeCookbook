# Python program to convert decimal into other number systems

num = '42'
dnum = int(num)

print("dnum is",dnum,"of type", (type(dnum)))

onum = oct(dnum)
print("onum is",onum[2:],"of type", (type(onum)))

hnum = hex(dnum)
print("hnum is",hnum[2:],"of type", (type(hnum)))


# Octal to Binary

print("Enter Octal Number: ", end="")
onum = input()

bnum = int(onum, 8)
bnum = bin(bnum)

print("\nEquivalent Binary Value =", bnum[2:])

print(),print()

# ----codescracker.com----

# print("Enter Octal Number: ", end="")
# onum = input()

dnum = int(onum, 8)
hnum = hex(dnum)
print("\nEquivalent Hexadecimal Value =", hnum[2:])

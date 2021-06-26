# Python program to convert decimal into other number systems

print('Enter decimal number: ', end='')
dec = int(input())

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

print(),print()
# Octal to Binary

print("Enter Octal Number: ", end="")
onum = input()

bnum = int(onum, 8)
bnum = bin(bnum)

print("\nEquivalent Binary Value =", bnum[2:])

print(),print()

# ----codescracker.com----

print("Enter Octal Number: ", end="")
onum = input()

dnum = int(onum, 8)
hnum = hex(dnum)
print("\nEquivalent Hexadecimal Value =", hnum[2:])

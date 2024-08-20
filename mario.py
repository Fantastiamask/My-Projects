# Get size
n = 0
while n < 1 or n > 8:
    try:
        n = int(input("Size: "))
    except:
        print("Not a Number")

# Print grid of blocks
i = n
j = 1
d = 0
z = 0
while i >= 1:
   # , end="", flush=True
    j = i-1
    d += 1
    z = 0
    h = 0
    while z != j:
        print(" ", end="", flush=True)
        z += 1
    while h != d:
        print("#", end="", flush=True)
        h += 1
    print("\n", end="", flush=True)

    i -= 1

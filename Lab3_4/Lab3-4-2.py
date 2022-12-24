def collatz(n):
    sequence = [n]
    while n > 1:
        if n % 2:
            n = 3 * n + 1
            sequence.append(n)
        else:
            n = n // 2
            sequence.append(n)
    return sequence


notint = 1
while notint:
    n = int(input("Enter n: "))
    if isinstance(n, int):
        notint = 0
        print(collatz(n))
    else:
        print("Please enter an integer")

sequenceLen = [0] * 999
for i in range(1, 1000):
    sequenceLen[i - 1] = len(collatz(i))

# print("sorted lengths of sequences: ", sorted(sequenceLen))

maxIndex = sequenceLen.index(max(sequenceLen)) + 1
print(
    "\nInteger which its collatz sequence has maximum length is: ",
    maxIndex,
    "\nIts squence is: ",
    collatz(maxIndex),
)

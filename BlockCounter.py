InputCount = input("What's the number you'd like converted to blocks?\n>>")
InputCount = int(InputCount)
blocks = int(InputCount / 50) + 1
numRows = input("How many columns would you like?\n>>")
numRows = int(numRows)
while blocks > numRows:
        print(" ".join(['\u25A0' for x in range(numRows)]))
        blocks -= numRows
print(' '.join(['\u25A0' for x in range(blocks)]))
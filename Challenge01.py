from ChallengeBase import ChallengeBase

print("Starting Challenge 1")

challenge = ChallengeBase(1)

firstValues = list()
secondValues = list() 

data = challenge.LoadData()
for row in data:
  values = row.split()
  firstValues.append(int(values[0]))
  secondValues.append(int(values[1]))

def partOne():
  firstValues.sort()
  secondValues.sort()

  if len(firstValues) != len(secondValues):
    print("Data is not valid")
    exit()

  totalDiff = 0
  for row in enumerate(firstValues):
    i = row[0]
    rowDiff = abs(firstValues[i] - secondValues[i])
    totalDiff += rowDiff

  print(totalDiff)

def partTwo():
  for row in enumerate(firstValues):
    i = row[0]
    

def partTwo():
  totalSum = 0
  for value in firstValues:
    fA = secondValues.count(value)
    totalSum += value * fA

  print(totalSum)

partTwo()
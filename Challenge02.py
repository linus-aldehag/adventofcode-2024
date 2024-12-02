from ChallengeBase import ChallengeBase

print("Starting Challenge 2")

challenge = ChallengeBase(2)

data = challenge.LoadData()

safeReports = 0
for report in data:
  levels = report.split()
  direction = 'unknown'
  dampenerAvailable = True
  
  currentLevel = int(levels[0])

  for index in range(1, len(levels)):
    lastLevel = currentLevel
    currentLevel = int(levels[index])

    if currentLevel == lastLevel:
        if dampenerAvailable:
          dampenerAvailable = False
        else:
            break
    elif currentLevel > lastLevel:
      if currentLevel - lastLevel > 3:
        if dampenerAvailable:
          dampenerAvailable = False
        else:
          break
      elif direction == 'unknown':
        direction = 'up'
      elif direction == 'down':
        if dampenerAvailable:
          dampenerAvailable = False
        else:
          break
    elif currentLevel < lastLevel:
      if lastLevel - currentLevel > 3:
        if dampenerAvailable:
          dampenerAvailable = False
        else:
            break
      elif direction == 'unknown':
        direction = 'down'
      elif direction == 'up':
        if dampenerAvailable:
          dampenerAvailable = False
        else:
            break

    if index == len(levels) - 1:
      safeReports += 1

print(safeReports)

#more than 503
#less than 521
from ChallengeBase import ChallengeBase

challenge = ChallengeBase(2)

data = challenge.load_data()

safeReports = 0
for report in data:
  levels = report.split()
  direction = 'unknown'
  dampener_available = False
  
  current_level = int(levels[0])

  for index in range(1, len(levels)):
    lastLevel = current_level
    current_level = int(levels[index])

    if current_level == lastLevel:
        if dampener_available:
          dampener_available = False
        else:
            break
    elif current_level > lastLevel:
      if current_level - lastLevel > 3:
        if dampener_available:
          dampener_available = False
        else:
          break
      elif direction == 'unknown':
        direction = 'up'
      elif direction == 'down':
        if dampener_available:
          dampener_available = False
        else:
          break
    elif current_level < lastLevel:
      if lastLevel - current_level > 3:
        if dampener_available:
          dampener_available = False
        else:
            break
      elif direction == 'unknown':
        direction = 'down'
      elif direction == 'up':
        if dampener_available:
          dampener_available = False
        else:
            break

    if index == len(levels) - 1:
      safeReports += 1

def part_one():
  print(safeReports)

def part_two():
  print("Part Two Not Implemented")

#more than 503
#less than 521

part_one()
part_two()
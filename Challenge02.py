from ChallengeBase import ChallengeBase
def process_report(levels):
  direction = 'unknown'
  current_level = int(levels[0])

  for index in range(1, len(levels)):
    last_level = current_level
    current_level = int(levels[index])

    if current_level == last_level:
      return index
    elif current_level > last_level:
      if current_level - last_level > 3:
        return index
    elif direction == 'unknown':
      direction = 'up'
    elif direction == 'down':
      return -1
    elif current_level < last_level:
      if last_level - current_level > 3:
        return -1
    elif direction == 'unknown':
      direction = 'down'
    elif direction == 'up':
      return -1

challenge = ChallengeBase(2)

data = challenge.load_data()

safeReports = 0
for reportRow in data:
    levelData = reportRow.split()
    dampenerUsed = False
    result = process_report(levelData)
    if result != -1:
      safeReports += 1
    else:
      if not dampenerUsed:
        dampenerUsed = True
        correctedRow = levelData.pop(result)
        result = process_report(levelData)
        if result != -1:
          safeReports += 1

def part_one():
  print(safeReports) #incorrect

def part_two():
  print(safeReports)


part_one()
part_two()
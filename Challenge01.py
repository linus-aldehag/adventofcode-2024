from ChallengeBase import ChallengeBase

challenge = ChallengeBase(1)

first_values = list()
second_values = list()

data = challenge.load_data()
for data_row in data:
  values = data_row.split()
  first_values.append(int(values[0]))
  second_values.append(int(values[1]))

def part_one():
  first_values.sort()
  second_values.sort()

  if len(first_values) != len(second_values):
    print("Data is not valid")
    exit()

  total_diff = 0
  for row in enumerate(first_values):
    i = row[0]
    row_diff = abs(first_values[i] - second_values[i])
    total_diff += row_diff

  print(total_diff)

def part_two():
  total_sum = 0
  for value in first_values:
    f_a = second_values.count(value)
    total_sum += value * f_a

  print(total_sum)

part_one()
part_two()
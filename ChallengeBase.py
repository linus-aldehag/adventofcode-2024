class ChallengeBase:
  def __init__(self, challenge_no):
    self.challengeId = str(challenge_no)
    print("Starting Challenge " + self.challengeId)

  def load_data(self):
    with open("input\\" + self.challengeId + ".txt", "r") as file:
      data = list()
      read_data = file.readline()
      while read_data:
        data.append(read_data)
        read_data = file.readline()
      return data
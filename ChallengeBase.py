class ChallengeBase:
  def __init__(self, challengeNo):
    self.challengeId = str(challengeNo)
  
  def LoadData(self):
    with open("input\\" + self.challengeId + ".txt", "r") as file:
      data = list()
      readData = file.readline()
      while readData:
        data.append(readData)
        readData = file.readline()
      return data
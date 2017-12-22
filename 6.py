import random

#
# CLASSES
#
class Draw:
  def __init__(self, seq, date, numbers, bonus):
    self.seq = seq #i-i
    self.date = date
    self.numbers = numbers #list of 5 int
    self.bonus = bonus #int

  def subSeq(self):
    return self.seq[-1]

  def pr(self):
    print(self.seq, self.date, self.numbers, self.bonus)

class Results:

  def __init__(self):
    matchTypes = ['0','1','2','2+','3','4','5','5+','6']
    self.results = {i: 0 for i in matchTypes}

  def add(self, result, n=1):
    self.results[result] += n

  def pr(self):
    for k, v in (self.results).items():
      print(k, v)

#
#FUNCTIONS
#
def readData(file):
  with open(file) as f:
    lines = [line.rstrip('\n') for line in f]

  print("File lines:", len(lines))
  data = []
  for line in lines[1:]: #do not include header line
    j = line.split(',')
    d = Draw(
      j[1] + "-" + j[2],
      j[3],
      [int(j[4]), int(j[5]), int(j[6]), int(j[7]), int(j[8]), int(j[9])],
      int(j[10])
      )
    data.append(d)
    #print data[-1]
  print("Data lines:", len(data), '\n')  #should be 1 less than file lines because of header
  return data

def winnings(picks, winners, bonus):
  matches = 0
  for n in picks:
      if (n in winners):
        matches += 1
  if (matches == 2) or (matches == 5):
    if (bonus in picks):
      matches = str(matches) + '+'
  return str(matches)

def randomDraw():
  s = list(range(1,50))
  w = random.sample(s,6)
  w.sort()
  return w

def randomTrial(winners):
  # train algorythm with first 2000
  #     do nothing this is not a trained algorythim

  r = Results()
  for w in winners[2000:]:
    p = randomDraw()
    w = winnings(p, w.numbers, w.bonus)
    r.add(w)
  return r

def trialsRandom(winners):
  random.seed()

  trials = 10
  rTotals = Results()
  
  for i in range(trials):
    # create trail and add it to total
    r = randomTrial(winners)
    for k, v in r.results.items():
      rTotals.add(k, v)
  # Find and print the average values
  rAvg = Results()
  for k, v in rTotals.results.items():
      rAvg.add(k, v/trials)
  print('# Trials:', trials)
  rAvg.pr()
  #print(rAvg.results)
  


#
#MAIN
#
def main():
  winners = readData('data.csv')

  trialsRandom(winners)


if __name__ == "__main__":
    main()

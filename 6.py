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
    self.results = [0,0,0,0,0,0,0,0,0]

  def add(self, result, n=1):
    if result == '0':
      self.results[0] += n
    elif result == '1':
      self.results[1] += n
    elif result == '2':
      self.results[2] += n
    elif result == '2+':
      self.results[3] += n
    elif result == '3':
      self.results[4] += n
    elif result == '4':
      self.results[5] += n
    elif result == '5':
      self.results[6] += n
    elif result == '5+':
      self.results[7] += n
    elif result == '6':
      self.results[8] += n

  def pr(self):
    print('0:', self.results[0])
    print('1:', self.results[1])
    print('2:', self.results[2])
    print('2+:', self.results[3])
    print('3:', self.results[4])
    print('4:', self.results[5])
    print('5:', self.results[6])
    print('5+:', self.results[7])
    print('6:', self.results[8])

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
        matches +=1
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
  for i in range(9):
    r = randomTrial(winners)
  r.pr()
  print(r.results)


#
#MAIN
#
def main():
  winners = readData('data.csv')
  print(len(winners))

  trialsRandom(winners)


if __name__ == "__main__":
    main()

import random 
import matplotlib.pyplot as plt

def RollDie():
  return random.randint(1,6)

def GetMeans(N):
  accum = 1
  means=[]
  rollSum = 0
  for i in range(N):
    rollSum += RollDie()
    means.append(rollSum/accum)
    accum+=1
  plt.plot(means)
  plt.ylabel('Means')
  plt.xlabel('Trials')
  plt.show()
  return means

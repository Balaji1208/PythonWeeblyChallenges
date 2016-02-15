# bubble sort
def bubbleSort():
  import random
  ranfomlist = []
  for i in range (1000):
    x = random.randint(1,1000)
    ranfomlist.append(x)
  lenlist = len(ranfomlist)
  for i in range (lenlist):
    for j in range (lenlist - 1):
      if ranfomlist[j] > ranfomlist[i]:
        x = ranfomlist[j]
        ranfomlist[j] = ranfomlist[i]
        ranfomlist[i] = x
  print('final')
  print(ranfomlist)

bubbleSort()

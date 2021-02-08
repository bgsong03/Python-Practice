array = [[100], [0, 1], [0], [10, 0, 1], [80, 70]]

def Sum(elem):
  sum = 0
  for i in range(len(elem)):
    sum += elem[i]
  return sum

array.sort(key = lambda x: Sum(x), reverse = True)
print(array)
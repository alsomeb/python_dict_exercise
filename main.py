myDict = {"First":3, "Second":25, "Third":65, "Fourth":98}

def biggestNrDict(dict:dict)->int:
  biggestValue = 0
  for value in dict.values():
    if value > biggestValue:
      biggestValue = value
  return biggestValue


def lowestNrDict(dict:dict)->int:
  lowestValue = 99 # random high nr
  for value in dict.values():
    if value < lowestValue:
      lowestValue = value
  return lowestValue


def secondBiggestNrDict(dict:dict)->int:
  list_of_values = []
  for val in dict.values():
    if val not in list_of_values:
      list_of_values.append(val)
  
  sorted_list = sorted(list_of_values, reverse=True)
  secondBiggestValue = sorted_list[1] #Because its reversed we know [0] is biggest
                                     # so [1] must be second biggest value
  return secondBiggestValue



print("The values in the dictionary are:")

val_nr = 1
for val in myDict.values():
  print(f"{val_nr}. {val}")
  val_nr = val_nr + 1

res_biggest_value = biggestNrDict(myDict)
res_lowest_value = lowestNrDict(myDict)
res_second_biggest_value = secondBiggestNrDict(myDict)

print()
print(f"The biggest value in dict: {res_biggest_value}")
print(f"The lowest value in dict: {res_lowest_value}")
print(f"The 2nd biggest value in dict: {res_second_biggest_value}")

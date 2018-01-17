from json import load as json
from glob import glob

def selectOne(options): 
  try:
    i = int(input("> "))
    if i >= len(options):
      print("Input should be between 0 and %i." % (len(options)-1))
      return selectOne(options)
  except Exception as e:
    print("Input an integer corresponding with your choice.")
    return selectOne(options)
  return options[i]

files = glob("./*.json")
if files:
  print("Choose your adventure:")
  
  for i, file in enumerate(files):
    print("%i: %s" % (i, file))
  
  data = json(open( selectOne(files) ))
  current = data['steps'][data['startStep']]
  while(True):
    print(current['text'])
    if 'options' not in current: break;
    for i, option in enumerate(current['options']):
      print("%i: %s" % (i, option['text']))

    answer = selectOne(current['options'])
    current = data['steps'][answer['goto']]

else:
  print("Found no json adventure files in this directory.")

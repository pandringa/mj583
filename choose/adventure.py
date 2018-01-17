import json
from glob import glob

def intInput(): 
  try:
    return int(input("> "))
  except Exception as e:
    print("Input an integer corresponding with your choice.")
    return intInput()


def main():
  files = glob("./*.json")
  if files:
    print("Choose your adventure:")
    
    for i, file in enumerate(files):
      print("%i: %s" % (i, file))
    data = json.load(open(files[intInput()]))
    
    current = data['steps'][data['startStep']]
    while(True):
      print(current['text'])
      if 'options' not in current: break;
      for i, option in enumerate(current['options']):
        print("%i: %s" % (i, option['text']))
      answer = current['options'][intInput()]
      current = data['steps'][answer['goto']]

  else:
    print("Found no json adventure files in this directory.")

main();
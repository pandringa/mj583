height = input("What's your height? ")
weight = input("What's your weight? ")

print("Your BMI is %s" % (int(weight) / int(height)**2 * 703))
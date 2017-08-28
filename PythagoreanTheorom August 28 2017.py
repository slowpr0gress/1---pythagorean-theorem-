#use pythagorean theorom
import math
print('What are the two values you know so far?')
a = input()
b = input()
b = int(b)
a = int(a)
c = math.sqrt((math.pow(a, 2)) + (math.pow(b, 2)))
print(str(round(c)) + ' This answer has been rounded.')

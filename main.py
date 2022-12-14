from src.utilities.utility import objectutils 

utl = objectutils()

_add = utl.add(3,5)

_sub = utl.sub(5, 2)

print(_add)
print(_sub)

print(utl.sub(2,5))

# A collection of type list can contain many occurances of the same element
basket = ['mango','apple','plum','peach','mango','mango','peach','apple','peach','plum']


# Mango weighs 100 fl oz, Apple weighs 30 fl oz, plum weighs 25 fl oz and peach weigh 15 fl oz. 
# A dictionary in python holds key value pairs
fruitWeightMap = {'mango':100, 'apple': 30, 'peach': 15, 'plum': 25}

weightOfBasket = 0
for fruitPicked in basket: 
  weightOfBasket = weightOfBasket + fruitWeightMap[fruitPicked]

print('Total weight ',weightOfBasket)
  

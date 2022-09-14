# Collection of fruits in a basket as a list
basket = ['mango','apple','plum','peach','mango','mango','peach','apple','peach','plum']


# Mango weighs 100 fl oz, Apple weighs 30 fl oz, plum weighs 25 fl oz and peach weigh 15 fl oz. 
fruitWeightMap = {'mango':100, 'apple': 30, 'peach': 15, 'plum': 25}

weightOfBasket = 0
for fruitPicked in basket: 
  weightOfBasket = weightOfBasket + fruitWeightMap[fruitPicked]

print('Total weight ',weightOfBasket)
  
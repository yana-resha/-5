class Animals:
  def __init__(self, name, weight):
    self.name = name   
    self.weight = weight
  def feed(self):
    return('кормить')

class Birds(Animals):
  name_1 = 'гусь'
  name_2 = 'утка'
  name_3 = 'кура'
  voice_1 = 'Га-Га'
  voice_2 = 'Кря-Кря'
  voice_3 = 'Ко-Ко'
  def take_eggs(self):
    return('яйца')

class Sheep(Animals):
  name_1 = 'овца'
  voice_1 = 'Бееее'
  def cut(self):
    return('шерсть')

class Take_milk(Animals):
  name_1 = 'корова'
  name_2 = 'коза'
  voice_1 = 'Мууууу'
  voice_2 = 'Меееее'
  def take_milk(self):
    return('молоко')

weight_list = []
weight_dict = {}    

goose_grey = Birds('Серый', 7)

print(f'{goose_grey.name_1} {goose_grey.name}, он говорит {goose_grey.voice_1} и весит {goose_grey.weight} кг, его нужно {goose_grey.feed()} и собирать {goose_grey.take_eggs()}')

weight_list.append(goose_grey.weight)
weight_dict[goose_grey.name] = goose_grey.weight


goose_white = Birds('Белый', 8)

print(f'{goose_white.name_1} {goose_white.name}, он говорит {goose_white.voice_1} и весит {goose_white.weight} кг, его нужно {goose_white.feed()} и собирать {goose_white.take_eggs()}')

weight_list.append(goose_white.weight)
weight_dict[goose_white.name] = goose_white.weight

duck_1 = Birds('Кряква', 3)

print(f'{duck_1.name_2} {duck_1.name}, она говорит {duck_1.voice_2} и весит {duck_1.weight} кг, ее нужно {duck_1.feed()} и собирать {duck_1.take_eggs()}')

weight_list.append(duck_1.weight)
weight_dict[duck_1.name] = duck_1.weight

chiсken_1 = Birds('Ко-Ко', 1)

print(f'{chiсken_1.name_3} {chiсken_1.name}, она говорит {chiсken_1.voice_3} и весит {chiсken_1.weight} кг, ее нужно {chiсken_1.feed()} и собирать {chiсken_1.take_eggs()}')

weight_list.append(chiсken_1.weight)
weight_dict[chiсken_1.name] = chiсken_1.weight

chiсken_2 = Birds('Кукареку', 2)

print(f'{chiсken_2.name_3} {chiсken_2.name}, она говорит {chiсken_2.voice_3} и весит {chiсken_2.weight} кг, ее нужно {chiсken_2.feed()} и собирать {chiсken_2.take_eggs()}')

weight_list.append(chiсken_2.weight)
weight_dict[chiсken_2.name] = chiсken_2.weight

sheep_1 = Sheep('Барашек', 30)

print(f'{sheep_1.name_1} {sheep_1.name}, он говорит {sheep_1.voice_1} и весит {sheep_1.weight} кг, его нужно {sheep_1.feed()} и стричь {sheep_1.cut()}')

weight_list.append(sheep_1.weight)
weight_dict[sheep_1.name] = sheep_1.weight

sheep_2 = Sheep('Кудрявый', 35)

print(f'{sheep_2.name_1} {sheep_2.name}, он говорит {sheep_2.voice_1} и весит {sheep_2.weight} кг, его нужно {sheep_2.feed()} и стричь {sheep_2.cut()}')

weight_list.append(sheep_2.weight)
weight_dict[sheep_2.name] = sheep_2.weight

cow_1 = Take_milk('Манька', 450)

print(f'{cow_1.name_1} {cow_1.name}, она говорит {cow_1.voice_1} и весит {cow_1.weight} кг, ее нужно {cow_1.feed()} и доить {cow_1.take_milk()}')

weight_list.append(cow_1.weight)
weight_dict[cow_1.name] = cow_1.weight

goat_1 = Take_milk('Рога', 45)

print(f'{goat_1.name_2} {goat_1.name}, она говорит {goat_1.voice_2} и весит {goat_1.weight} кг, ее нужно {goat_1.feed()} и доить {goat_1.take_milk()}')

weight_list.append(goat_1.weight)
weight_dict[goat_1.name] = goat_1.weight

goat_2 = Take_milk('Копыта', 47)

print(f'{goat_2.name_2} {goat_2.name}, она говорит {goat_2.voice_2} и весит {goat_2.weight} кг, ее нужно {goat_2.feed()} и доить {goat_2.take_milk()}')

weight_list.append(goat_2.weight)
weight_dict[goat_2.name] = goat_2.weight

print(f'Общий вес всех животных {sum(weight_list)} кг')

max_animal = [(value, key) for key, value in weight_dict.items()]

print(f'Самое тяжелое животное на ферме {max(max_animal)[1]}')
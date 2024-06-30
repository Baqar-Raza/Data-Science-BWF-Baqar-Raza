#Data Structures

#LISTS

fruits = ['apple', 'mango', 'banana', 'guava']
print(fruits)
print(fruits[2])
print(fruits[-1])

message = "I eat a "+ fruits[1].title() +"."
print(message)

#changing elements
fruits[0]="grapes"
print(fruits)

#adding element
fruits.append("coconut")
print(fruits)

#dynamic property
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#inserting element
motorcycles.insert(0, 'ducati')     #inserting at pos 0
print(motorcycles)

#removing element
del motorcycles[0]
print(motorcycles)

#using pop
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#Sorting
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.reverse()
print(cars)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
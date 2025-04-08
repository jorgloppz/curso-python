to_do = ['comer', 'dormir', 'estudiar', 'trabajar', 'jugar']
print(to_do)
numbers = [1, 2, 3, 4, 'cinco']
print(numbers)
print(type(numbers))
mixed = [1, 2, 3, 4, True, [6, 7, 8]]
print(mixed)
print(len(mixed))
print('primer elemento', mixed[0])
print('segundo elemento', mixed[1])
print('tercer elemento', mixed[2])
print('cuarto elemento', mixed[3])
print('ultimo elemento', mixed[-1])
print(mixed)
mixed.append(False)
print(mixed)
mixed.append(['a', 'b'])
print(mixed)
mixed.insert(1, ['a', 'b'])
print(mixed)
mixed.pop() # Elimina el último elemento
print(mixed)
mixed.pop(1) # Elimina el elemento en la posición 1
print(mixed)
mixed.remove(3) # Elimina el elemento 3
print(mixed)
mixed.index(4) # Devuelve la posición del elemento 4
print(mixed)
mixed.reverse() # Invierte la lista
print(mixed)
mixed.sort() # Ordena la lista
print(mixed)
mixed.clear() # Elimina todos los elementos de la lista
print(mixed)
mixed = [1, 2, 3, 4, True, [6, 7, 8]]
print(mixed)

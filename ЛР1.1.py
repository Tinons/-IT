numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
s = sum(x for x in numbers if x is not None)
n = len(numbers)
avg = s / n
missing_index = numbers.index(None)
numbers[missing_index] = avg

print("Измененный список:", numbers)

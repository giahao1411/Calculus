odd = 0
even = 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in numbers:
    if i %2 == 0:
        odd += 1
    if i %2 != 0:
        even += 1

print("Number of odd numbers:", odd)
print("Number of even numbers:", even)
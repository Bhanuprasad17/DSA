print("1. range(stop):")
for i in range(5):
    print(i, end=' ')
print("\n" + "-"*30)

print("2. range(start, stop):")
for i in range(2, 6):
    print(i, end=' ')
print("\n" + "-"*30)

print("3. range(start, stop, step):")
for i in range(1, 10, 2):
    print(i, end=' ')
print("\n" + "-"*30)

print("4. Negative step (reverse range):")
for i in range(5, 0, -1):
    print(i, end=' ')
print("\n" + "-"*30)

print("5. Negative start and stop:")
for i in range(-5, 0):
    print(i, end=' ')
print("\n" + "-"*30)

print("6. Negative start, stop, step:")
for i in range(-1, -6, -1):
    print(i, end=' ')
print("\n" + "-"*30)

print("7. Convert range to list and tuple:")
print("List:", list(range(1, 6)))
print("Tuple:", tuple(range(3)))
print("-"*30)

print("8. Using range with len():")
names = ['bhanu', 'raj', 'vinay']
for i in range(len(names)):
    print(f"Index {i}: {names[i]}")
print("-"*30)

print("9. Using range to mimic enumerate:")
for i in range(len(names)):
    print(i, names[i])
print("-"*30)

print("10. Step size greater than 1:")
for i in range(0, 20, 5):
    print(i, end=' ')
print("\n" + "-"*30)

print("11. Empty range (no output):")
for i in range(5, 2):  # This won't print anything
    print(i, end=' ')
print("\n(No output expected)\n" + "-"*30)

print("12. Invalid step = 0 (commented to avoid error):")
# range(1, 5, 0)  # Uncommenting this will raise: ValueError
print("range(1, 5, 0) → ValueError: step must not be zero")

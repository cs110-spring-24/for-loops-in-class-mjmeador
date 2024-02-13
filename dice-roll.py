import random

dice_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for _ in range(100):
    roll = random.randint(1, 6)
    print(roll)
    dice_count[roll] += 1

print("Number of 1s:", dice_count[1])
print("Number of 2s:", dice_count[2])
print("Number of 3s:", dice_count[3])
print("Number of 4s:", dice_count[4])
print("Number of 5s:", dice_count[5])
print("Number of 6s:", dice_count[6])

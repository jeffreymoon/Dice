#03_02_dice
import random
# for x in range(1, 11):
# #    random_number = random.randint(1, 6)
# #    print(random_number)
#     throw_1 = random.randint(1, 6)
#     throw_2 = random.randint(1, 6)
#     total = throw_1 + throw_2
#     print(total)
#     if total == 7:
#         print('Seven Thrown!')
#     if total == 11:
#         print('Eleven Thrown!')
#     if throw_1 == throw_2:
#         print('Double Thrown!')

# print(10 > 9)
# print(10 < 9)
# if not (total < 5 or total > 9):
#     print('not bad')
# else:
#     print('bad')

# throw_1 = random.randint(1, 6)
# throw_2 = random.randint(1, 6)
# while not (throw_1 == 6 and throw_2 == 6):
#     total = throw_1 + throw_2
#     print(total)
#     throw_1 = random.randint(1, 6)
#     throw_2 = random.randint(1, 6)
# print('Double Six throw!')

while True:
    throw_1 = random.randint(1, 6)
    throw_2 = random.randint(1, 6)
    total = throw_1 + throw_2
    print(total)
    if (throw_1 == 6 and throw_2 == 6):
        break
print('Double Six thrown!')
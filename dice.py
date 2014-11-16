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

# while True:
#     throw_1 = random.randint(1, 6)
#     throw_2 = random.randint(1, 6)
#     total = throw_1 + throw_2
#     print(total)
#     if (throw_1 == 6 and throw_2 == 6):
#         break
# print('Double Six thrown!')

book_name = 'Programming Raspberry Pi'
print(book_name)
print(len(book_name))
print(book_name[0])
print(book_name[1])
print(book_name[0:11])
print(book_name[12:])
book_name += ' by Simon Monk'
print(book_name)
numbers = [123, 34, 55, 321, 9]
print(len(numbers))
print(numbers[0])
print(numbers[1:3])
numbers[0] = 1
print(numbers)
more_numbers = [5, 6, 44]
print(numbers + more_numbers)
numbers.sort()
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(1)
print(numbers)
numbers.insert(1, 66)
print(numbers)

big_list = [123, 'hello', ['inner list', 2, True]]
print(big_list)

list = [1, 'one', 2, True]
for item in list:
    print(item)

def make_polite(sentence):
    polite_sentence = sentence + ' please'
    return polite_sentence

print(make_polite('Pass the Salt'))

def say_hello(n):
    for x in range(0, n):
        print('Hello')

say_hello(5)

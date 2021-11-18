# even_sum = 0
# for i in range(10, 31):
#   if i % 2 == 0:
#     even_sum = even_sum + i
# print(even_sum)


number = input('Type any integer number: ')
for i in range(int(number)):
  print('Hello!')

user_input = input('Input number ')
if user_input.isdigit():
  n = int(user_input)
  for _ in range(n):
    print('Hello')
else:
  print('Enter number, not text symbols')


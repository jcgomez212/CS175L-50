# CS175L-50
# Juliana Gomez
# AverageFromInput

infile = open('numbers.txt', 'r')

sum_nums = 0
counter = 0

for line in infile.readlines():
    counter = counter + 1
    sum_nums += float(line)
    
    print(f'I read in {counter} number(s) Current number is: {float(line)} Total is: {sum_nums}')

print('Average:', sum_nums / counter)

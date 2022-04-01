# CS175L-50
# Juliana Gomez
# AverageFromInputWithExceptionHandling

import sys

def main():
    try:
        infile = open('numbers.txt', 'r')
    except IOError:
        print('An error occurred trying to read the file.')
        sys.exit()
    
    sum_nums = 0
    counter = 0

    for line in infile.readlines():
        counter = counter + 1
        try:
            num = float(line)
        except ValueError:
            print('Non-numeric data found in the file')
            counter = counter - 1
            continue
        sum_nums += num
        
        print (f'I read in {counter} number(s) Current number is: {num} Total is: {sum_nums}')
    


main()

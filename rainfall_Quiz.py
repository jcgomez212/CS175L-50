# CS 175
# Juliana Gomez
# rainfall.py

total_rainfall = 0
monthly_rainfall = 0
average = 0
num_years = 0
total_months = 0

num_years = int(input('Enter the number of years (1 - 3 years): '))

while num_years < 1 or num_years > 3:
    print('Please enter a number greater than or equal to 1 or less than or equal to 3')
    num_years = int(input('Enter the number of years (1 - 3 years): '))

for year in range(0, num_years + 1):
    print('For year ', year + 1, ':')

for month in range(12):
    monthly_rainfall = float(input('Enter the amount of rainfall for the month: '))
    total_months += 1
    total_rainfall += monthly_rainfall

average = total_rainfall / total_months


print('For', total_months, 'months')
print('Total rainfall: ', total_rainfall)
print('Average monthly rainfall: ', average, 'inches')

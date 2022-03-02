# CS175L-50
# Juliana Gomez
# average_grade.py

#   calculate the average using users input for 5 scores
def calc_average(score1,score2,score3,score4,score5):
    average = 0
    grades_sum = score1 + score2 + score3 + score4 + score5
    average = grades_sum / 5
    return average

#   determine the ltter grade from the numeric grade
def determine_grade(score):
    if score >= 90:
        return'A'
    elif score >= 80:
        return'B'
    elif score >=70: 
        return 'C'
    elif score >=60: 
        return 'D'
    else:
        return 'F'
        
# start with a loop (keep everything in loop)
another_calc = True

while another_calc:
    score1 = int(input('Enter score 1: '))
    score2 = int(input('Enter score 2: '))
    score3 = int(input('Enter score 3: '))
    score4 = int(input('Enter score 4: '))
    score5 = int(input('Enter score 5: '))
    scores = [score1, score2, score3, score4, score5]
    

    print('Score\t\t   Numeric Grade\tLetterGrade')
    print('--------------------------------------------------------')
    counter = 1
    for score in scores:
        print(f'Score {counter}:\t\t{score}\t\t     {determine_grade(score)}')
        counter = counter + 1
        
#   print the data "Score 1:        60      D"
#                   (continued until last letter score is determined)
#                  "Average score:  80      B"
#   def data_table():
    average = calc_average(score1, score2, score3, score4, score5)
    print(f"Average score:\t\t{average}\t\t     {determine_grade(average)}")
        
#   repeat loop?
    response = input("Enter 'yes' if you would like to do another calculation: ")
    if response == 'yes':
        another_calc = True
    else:
        break

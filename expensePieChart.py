# CS175L-50
# Juliana Gomez
# expensePieChart.py

import matplotlib.pyplot as plt

def main():
    infile = open('expenses.txt' , 'r')

    label = []
    value = []
    for line in infile.readlines():
        line = line.replace('Payment', '')
        label.append(str(line.split()[0]))
        value.append(int(line.split()[1]))
    plt.pie(value, label=label, colors = ('g', 'r', 'm', 'y', 'b', 'c'))
    plt.show()


main()

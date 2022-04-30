#CS175L-50
#Juliana Gomez
#stocks.py


com_rate = float(input("What was the commission rate?:"))

numShar = float(input("How many shares did you purchase?:"))

purchPrice = float(input("What was the purchase price?:"))

sellPrice = float(input("What was the selling price?:"))

AmtPaid = (numShar * purchPrice)

print("Amount paid for stock: $", AmtPaid)

purchPay = (com_rate * AmtPaid)

print("Commision paid on the purchase: $", purchPay)

soldFor = (numShar * sellPrice)

print("Amount the stock sold for: $", soldFor)

salePay = (soldFor * com_rate)

print("Commission paid on the sale: $", soldFor *com_rate)

totalCom = (purchPay + salePay)

print("Total commission paid: $", totalCom)

profit = (soldFor - AmtPaid - totalCom)

print("Profit (or loss if negative): $", profit)

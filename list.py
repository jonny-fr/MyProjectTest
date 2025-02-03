from datetime import datetime, timedelta
import re

transactions = []

def addtotransactions(typ, amount):
    time=datetime.now().date()
    transactions.append({'type':typ, 'amount':amount, 'date':time})


def totalAmount():
    total = 0
    for transaction in transactions:
        total +=transaction['amount']
    return total

def printTransactions():
    for transaction in transactions:
        print('Type:', transaction['type'])
        print('Amount:', transaction['amount'])
        print('Date:', transaction['date'])
        print('')

def yesterdaysTransactons():
    amount=0
    for transaction in transactions:
        if transaction['date'] == (datetime.now().date())- timedelta(days=1):
            amount +=1
    return amount

addtotransactions('deposit',1000)
addtotransactions('withdraw',-500)



def checkdate(date):
    return bool(re.match(r'^\d{4}-\d{2}-\d{2}$', date))


print(checkdate('2020-12-12'))

print(checkdate('2020-12-11'))

printTransactions()

print(totalAmount())

print((datetime.now().date())- timedelta(days=1))

print(yesterdaysTransactons())


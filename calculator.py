age= int(input("Enter your age: "))

baseprice= 20

if age < 18:
    price= baseprice * 0.5

elif age > 65:
    price= baseprice * 0.7

elif age<30:
    price= baseprice * 0.8

else:
    price= baseprice * 1.0

print("Your ticket price is: ", price)
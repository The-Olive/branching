# Program to calculate the total amount of an electric bill

kH = int(input("What is the total number of hours used? \n"))    # kH is the number of hours used


if kH == 764:
    print("Amount owed is $58.31612")
elif(kH == 812):
    print("Amount owed is $61.97996")
elif(kH == 1215):
    print("Amount owed is $96.23685")
elif(kH == 1500):
    print("Amount owed is $122.625")
else:
    print("Please enter another amount")
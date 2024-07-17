import pandas as pd
import matplotlib.pyplot as plt


main_course = {
    'Burger': 200,
    'Sandwich': 100,
    'Pizza': 300,
    'Pasta': 250

}
appetizer = {
    'nachoz':200,
    'crackers':100
}
drinks= {
    'Coke':100,
    'Lemonade':300,
    'Mohito':500
}
order = []
order_amount = []
total_amount = 0
choice = ''
bill = 0
print("Main Course: \n")
for mc, price in main_course.items():
    print(mc, price)

for mc, mc_price in main_course.items():
    while(choice != 'N'):
        mc_order = input("Choose from Main Course \n ")
        order.append(mc_order)
        mc_quantity = eval(input("Enter Quantity: \n "))
        bill = int(main_course[mc_order]) * mc_quantity
        total_amount = total_amount + bill
        order_amount.append(bill)
        choice = input("Do You want to add another Item from Main Course?? Press Y for Yes and N for No\n ")

#order_amount.append(total_amount)


choice = input("Do You want to add from appetizer Press Y for Yes and N for No \n ")
if choice == 'Y':
    print("Appetizer: \n")
    for ap, price2 in appetizer.items():
        print(ap, int(price2))
    while(choice!= 'N'):
        ap_order = input("Choose from appetizer \n ")
        order.append(ap_order)
        ap_quantity = int(input("Enter Quantity: \n "))
        bill = int(appetizer[ap_order]) * ap_quantity
        total_amount = total_amount + bill
        total_appetizer = bill
        order_amount.append(total_appetizer)
        choice = input("Do You want to add another Item from Appetizers?? Press Y for Yes and N for No\n ")
#order_amount.append(total_appetizer)



choice = input("Do You want to add from Drinks Press Y for Yes and N for No \n ")
if choice == 'Y':
    print("Drink: \n")
    for dr, price3 in drinks.items():
        print(dr, price3)
    while(choice!= 'N'):
        dr_order = input("Choose from drinks \n ")
        order.append(dr_order)
        dr_quantity = int(input("Enter Quantity: \n "))
        bill = int(drinks[dr_order]) * dr_quantity
        total_amount = total_amount + bill
        total_drink = bill
        order_amount.append(total_drink)
        choice = input("Do You want to add another Item from Drink?? Press Y for Yes and N for No\n ")
#order_amount.append(total_drink)

print("your Chosen Items: ",order)
print("Your Chosen Items: ",order_amount)
print("Your Total Amount: ",total_amount)

df = pd.DataFrame({'Order':order,'Amount':order_amount})
print(df)
df.to_csv("Take_Away_Database.csv")
plt.bar(order, order_amount)
plt.xlabel("Food Items")
plt.ylabel("Sales (Price) ")
plt.show()




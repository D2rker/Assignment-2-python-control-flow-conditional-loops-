def task1():
    
    order_amount = int(input("amount $: "))
    if order_amount >= 2000:
        discount = 15
    elif order_amount >= 1500: 
        discount = 10
    elif order_amount >= 1000: 
        discount = 7
    else:
        discount = 0

    tax = 5
    discount_value = order_amount * discount / 100
    total_after_discount = order_amount - discount_value
    add_tax = total_after_discount * tax / 100
    final_amount = total_after_discount + add_tax

    print(f"You got {discount}% discount. After applying {tax}% tax, the final amount is ${final_amount}")





def task2():
    order_amounts = [1200, 2500, 800, 1750, 3000]
    tax_rate = 5
    total_revenue_after_discount = 0  # Initialize outside the loop

    for amount in order_amounts:
        if amount >= 2000:
            discount_percent = 15
        elif amount >= 1500: 
            discount_percent = 10
        elif amount >= 1000: 
            discount_percent = 7
        else:
            discount_percent = 0

        discount_value = amount * (discount_percent / 100)
        after_discount = amount - discount_value
        
        total_revenue_after_discount += after_discount

        print(f"${amount} | {discount_percent}% discount | Final: ${after_discount}")

    print("-----------------------------")
    print(f"Total Revenue after discount: ${total_revenue_after_discount:.2f}")
    




def task3():
    order_amounts = [1200, 2500, 800, 1750, 3000]

    while True:
        choice = input(f"\npress '1' to Add order amount\npress '2' to show all orders\npress 'q' to quit : ")

        if choice == 'q':
            print("Goodbye!")
            break
        
        if choice == '1':
            try:
                amount_str = input("Enter order amount: ")
                amount = int(amount_str) 
                order_amounts.append(amount)
                print(f"Added ${amount}")
            except ValueError:
                print("Error: Please enter a valid integer number.")
            continue

        elif choice == '2':
            if not order_amounts:
                print("No orders recorded yet.")
                continue

            total_revenue_after_discount = 0
            
            for amount in order_amounts:
                if amount >= 2000:
                    discount_percent = 15
                elif amount >= 1500: 
                    discount_percent = 10
                elif amount >= 1000: 
                    discount_percent = 7
                else:
                    discount_percent = 0

                discount_value = amount * (discount_percent / 100)
                after_discount = amount - discount_value
                total_revenue_after_discount += after_discount

                # Used :.2f to keep currency looking clean (2 decimal places)
                print(f"Amount: ${amount} | Discount: {discount_percent}% | Final: ${after_discount}")

            print("----------------------------------------")
            print(f"Total Revenue: ${total_revenue_after_discount}")
            continue

        else:
            print("Invalid choice. Please select 1, 2, or q.")
            continue





def task4():
    daily = [200, 150, 0, 400, 50, -1, 300]
    total_sales = 0

    for sale in daily:
        if sale == -1:
            print("Corrupted data found. Stopping process.")
            break  

        elif sale == 0:
            continue

        total_sales += sale
        print(f"daily sale ${sale}. total sales: ${total_sales}")

    print(f"Total sale is: ${total_sales}")



choice = input("press 1 for Task 1, press 2 to task 2, press 3 for Task 3, press 4 for Task 4: ")
if choice == "1":
    task1()
elif choice == "2":
    task2()
elif choice == "3":
    task3()
elif choice == "4":
    task4()
else:
    print("Invalid choice! Please enter 1, 2, 3, or 4.")

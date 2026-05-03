def main():
    product_names = []
    product_prices = []

    while True:
        print("\n[1] Add product")
        print("[2] Display all products")
        print("[3] Update a price")
        print("[4] Search for a product")
        print("[5] Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            try:
                price = float(input("Enter product price: "))
                if price <= 0:
                    print("Price cannot be less than or equal to 0!")
                else:
                    product_names.append(name)
                    product_prices.append(price)
            except ValueError:
                print("Invalid input! Please enter a numerical value for the price.")

        elif choice == '2':
            if not product_names:
                print("Add items first!")
            else:
                print("\nInventory List:")
                for i in range(len(product_names)):
                    print(f"{i + 1}. {product_names[i]} {product_prices[i]:.1f}")

        elif choice == '3':
            if not product_names:
                [span_9](start_span)print("Add items first!")[span_9](end_span)
            else:
                search_name = input("Enter item name to update price: ")
                if search_name in product_names:
                    index = product_names.index(search_name)
                    try:
                        new_price = float(input("Enter new price: "))
                        if new_price <= 0:
                            print("Price cannot be less than or equal to 0!")
                        else:
                            product_prices[index] = new_price
                            print("Price updated successfully!")
                    except ValueError:
                        print("Invalid price input.")
                else:
                    [span_11](start_span)print("Item not found!")[span_11](end_span)

        elif choice == '4':
            if not product_names:
                [span_12](start_span)print("Add items first!")[span_12](end_span)
            else:
                search_item = input("Enter item: ")
                if search_item in product_names:
                    idx = product_names.index(search_item)
                    [span_14](start_span)print(f"{product_names[idx]}\n{product_prices[idx]:.1f}")[span_14](end_span)
                else:
                    [span_15](start_span)print("Product not found!")[span_15](end_span)

        elif choice == '5':
            [span_16](start_span)print("Exiting program...")[span_16](end_span)
            break

        else:
            print("Invalid choice. Please try again")

if _name_ == "_main_":
    main()

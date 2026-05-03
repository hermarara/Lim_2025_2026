choices=["[1] Add product", "[2] Display all products", "[3] Update a price","[4] Search for a product","[5] Remove product", "[6] Exit"]
P=[]
Ps=[]
while True:
    for something in range (len(choices)):
        print(choices[something])

    Choice=int(input("Enter choice: "))

    if Choice<1 or Choice>6:
        print("Invalid choice. Please try again")

    elif Choice in [2, 3, 4, 5] and not P:
        print("Add items first!")
        continue

    if Choice==1:
        prod=input("Enter product name: ")
        while True:
            price=float(input("Enter product price: "))
            if price<=0:
                print("Price cannot be less than or equal to 0!")
            else:
                break
        P.append(prod)
        Ps.append(price)
        
    elif Choice==2:
        for l in range(len(P)):
            print(f"{l+1}. {P[l]} - {Ps[l]}")
            
    elif Choice==3:
        while True:
            name=input("Enter item name to update price: ")
            if name in P:
                np=float(input("Enter new price: "))
                position=P.index(name)
                Ps[position]=np
                break
            else:
                print("Item not found!")

    elif Choice==4:
        for e in range(len(P)):
            item=input("Enter item: ")
            if item in P:
                ind=P.index(item)
                print(f"{P[ind]} - {Ps[ind]}")
            else:
                print("Product not found!")
            break

    elif Choice==5:
        while True:
            remove=input("Enter item name to remove: ")
            if remove in P:
                indx=P.index(remove)
                P.pop(indx)
                Ps.pop(indx)
                print(remove, "has been remove succesfully")
            else:
                print("Item not found!")
            break

    elif Choice==6:
        break

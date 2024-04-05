from Mortgage import Mortgage

progress = input('#################################\n# ' + 
                     'ENTER THE FOLLOWING: \n# Enter\t: Start Game \n# l\t: Change Loan Amount '+
                     '\n# i\t: Change Loan Interest \n# y\t: Change Loan Years \n# q\t: Quit '+
                     '\n#################################\n')



name= input("Enter Your Name: ")
amount = input("Enter Your Loan Amount (in figures): ")
interest = input("Enter Your Loan Interest: ")
years = input("Enter Years to Pay Loan: ")

while(progress != "q"):
    mortgage = Mortgage(float(amount), float(interest), int(years))
    
    match progress:
        case "c":
            name = input("Enter Your Name: ")
            amount = input("Enter Your Loan Amount (in figures): ")
            interest = input("Enter Your Loan Interest: ")
            years = input("Enter Years to Pay Loan: ")
            mortgage = Mortgage(float(amount), float(interest), int(years))
            print("\n\tHello {name}, \n\tYour Monthly mortgage: {mortgage}\n".
                  format(name=name.split()[0],mortgage = format(mortgage.compute_mortgage(),".2f")))
        case "l":
            change_amount = input("Enter Your Loan Amount (in figures): ")
            mortgage.set_principal(float(change_amount))
            print("\n\tHello {name}, \n\tYour Monthly mortgage: {mortgage}\n".
                  format(name=name.split()[0],mortgage = format(mortgage.compute_mortgage(),".2f")))
        case "i":
            change_interest = input("Enter Your Loan Interest: ")
            mortgage.set_interest(float(change_interest))
            print("\n\tHello {name}, \n\tYour Monthly mortgage: {mortgage}\n".
                  format(name=name.split()[0],mortgage = format(mortgage.compute_mortgage(),".2f")))
        
        case "y":
            change_years = input("Enter Years to Pay Loan: ")
            mortgage.set_years(float(change_interest))
            print("\n\tHello {name}, \n\tYour Monthly mortgage: {mortgage}\n".
                  format(name=name.split()[0],mortgage = format(mortgage.compute_mortgage(),".2f")))
        
        case "q":
            progress = "q"
        
        case _:
            print("\n\tHello {name}, \n\tYour Monthly mortgage: {mortgage}\n".
                  format(name=name.split()[0],mortgage = format(mortgage.compute_mortgage(),".2f")))
    
    progress = input('#################################\n# ' + 
                     'ENTER THE FOLLOWING: \n# Enter\t: Continue Game \n# l\t: Change Loan Amount '+
                     '\n# i\t: Change Loan Interest \n# y\t: Change Loan Years \n# q\t: Quit '+
                     '\n#################################\n')
    


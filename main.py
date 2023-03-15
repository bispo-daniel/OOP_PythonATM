from Account import Account

#List that will receive all the instances of Account
accountsList = []

#Function to get user ID and test if the value entered is an integer
def getAccountId():
    try:
        print("Type the account's ID you want to do this operation...")
        accountId = int(input())
    except:
        print("\nYou probably typed a letter where a number is expected. Try again...\n")
        main()
    
    return accountId

#Function to insert an instance of Account inside the accounts List
def create():

    try:
        print("Type your account's number...")
        accountIdVALUE = int(input())

        print("Type your name...")
        nameVALUE = input()

        print("Type your initial balance...")
        balanceVALUE = float(input())

        #Insert into the list
        accountsList.append(Account(accountIdVALUE, nameVALUE, balanceVALUE))
    except:
        print("\nYou probably typed a letter where a number is expected. Try again...\n")
        create()

    main()

#Function to display every instance of Account previously created
def read():
    for x in range(len(accountsList)):
        print('\n', accountsList[x].accountId, accountsList[x].name, accountsList[x].balance)

    main()

#Function to update a value (Id, Name or Balance) from an instance of Account
def update():
    updateId = getAccountId()

    try:
        print("What do you want to change? 1) AccountId 2) Name 3) Balance")
        toBeChanged = input()

        print("Insert the new value...")
        newValue = input()

        if toBeChanged == '1':
            for x in range(len(accountsList)):
                if(accountsList[x].accountId == updateId):
                    accountsList[x].accountId = int(newValue)
        elif toBeChanged == '2':
            for x in range(len(accountsList)):
                if(accountsList[x].accountId == updateId):
                    accountsList[x].name = newValue
        elif toBeChanged == '3':
            for x in range(len(accountsList)):
                if(accountsList[x].accountId == updateId):
                    accountsList[x].balance = float(newValue)
    except:
        print("\nYou probably typed a letter where a number is expected. Try again...\n")
        update()

    main()

def delete():
    #A copy is created because as soon as we remove an item from the original list it shrinks it's length
    #And the for function wouldn't iterate properly
    listLengthNOW = accountsList.copy()

    deleteId = getAccountId()
    for x in range(len(listLengthNOW)):
        if(listLengthNOW[x].accountId == deleteId):
            accountsList.remove(accountsList[x])

    main()

#Function to get the lowest balance amongst all the Account's instances
def min():
    menorSaldo = accountsList[0].balance

    for x in range(len(accountsList)):
        if(accountsList[x].balance < menorSaldo):
            menorSaldo = accountsList[x].balance

    return menorSaldo

#Function to get the highest balance amongst all the Account's instances
def max():
    maiorSaldo = accountsList[0].balance

    for x in range(len(accountsList)):
        if accountsList[x].balance > maiorSaldo:
            maiorSaldo = accountsList[x].balance

    return maiorSaldo

#Function to get the average balance between all Account's instances
def avg():
    acumulador = 0
    divisor = 0

    for x in range(len(accountsList)):
        acumulador += accountsList[x].balance
        divisor = x+1

    return acumulador / divisor

#Function to display all the 3 previous functions
def statistics():
    print("\nThe lowest balance is: ", min())
    print("The greatest balance is:", max())
    print("The average balance is: ", avg(), "\n")

    main()

#Function to get a statement from a specific instance of Account
def statement():
    statementId = getAccountId()

    for x in range(len(accountsList)):
        if accountsList[x].accountId == statementId:
            print("Your account's balance: ", accountsList[x].balance)

    main()

#Function to make a deposit in a specific instance of Account
def deposit():
    depositId = getAccountId()

    try:
        print("Type the deposit value...")
        depositValue = float(input())
    except:
        print("\nYou probably typed a letter where a number is expected. Try again...\n")
        deposit()

    for x in range(len(accountsList)):
        if(accountsList[x].accountId == depositId):
            accountsList[x].balance += depositValue 

    main()

#Function to withdraw from a specific instance of Account
def withdraw():
    withdrawId = getAccountId()
    
    try:
        
        print("Type the withdraw value...")
        withdrawValue = float(input())
    except:
        print("\nYou probably typed a letter where a number is expected. Try again...\n")
        withdraw()

    for x in range(len(accountsList)):
        if(accountsList[x].accountId == withdrawId):
            if(accountsList[x].balance < withdrawValue):
                print("Transaction denied! Withdraw greater than balance...")
            else:
                accountsList[x].balance -= withdrawValue
    
    main()

#Function to transfer a balance amount from one instance to another 
def transfer():
    try:
        print("From which account do you want to transfer? Type it's ID...")
        originAccount = int(input())

        print("What is the transfer amount?")
        moneyAmount = float(input())

        print("To which account the money will be transfered? Type it's ID...")
        addressee = int(input())

    except:
        print("\nYou probably typed a letter where a number is expected. Try again...\n")
        transfer()

    for x in range(len(accountsList)):

        if accountsList[x].accountId == originAccount:
            if accountsList[x].balance < moneyAmount:
                print("Transaction denied! Transfer amount greater than balance...")
            else:
                accountsList[x].balance -= moneyAmount

                for i in range(len(accountsList)):
                    if accountsList[i].accountId == addressee:
                        accountsList[i].balance += moneyAmount
    
    main()

#Main function where the user choose what operation
def main():
    print("\nWhat do you want to do?" + 
        "\n1) Create account" + 
        "\n2) List accounts" +
        "\n3) Update account" +
        "\n4) Delete account" +
        "\n5) ATM Statistics" +
        "\n6) Account statement" +
        "\n7) Deposit" +
        "\n8) Withdraw" +
        "\n9) Transfer" +
        "\n0) Exit")
    
    option = input()

    if option == '1':
        create()
    elif option == '2':
        read()
    elif option == '3':
        update()
    elif option == '4':
        delete()
    elif option == '5':
        statistics()
    elif option == '6':
        statement()
    elif option == '7':
        deposit()
    elif option == '8':
        withdraw()
    elif option == '9':
        transfer()
    elif option == '0':
        SystemExit(0)
    
main() 
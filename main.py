from Account import Account

#Criar um else caso o número da conta não foi encontrado
#Try Except Caso o valor inserido não seja do tipo esperado

iterator = 0

accountsList = []

def create():

    print("Type your account's number...")
    accountIdVALUE = int(input())

    print("Type your name...")
    nameVALUE = input()

    print("Type your initial balance...")
    balanceVALUE = int(input())

    accountsList.append(Account(accountIdVALUE, nameVALUE, balanceVALUE))

    main()

def read():
    for x in range(len(accountsList)):
        print('\n', accountsList[x].accountId, accountsList[x].name, accountsList[x].balance)

    main()

def update():

    print("Type the account's number you want to update")
    accountId = int(input())
    print("What do you want to change? 1) AccountId 2) Name 3) Balance")
    toBeChanged = input()
    print("Insert the new value...")
    newValue = input()

    if toBeChanged == '1':
        for x in range(len(accountsList)):
            if(accountsList[x].accountId == accountId):
                accountsList[x].accountId = int(newValue)
    elif toBeChanged == '2':
        for x in range(len(accountsList)):
            if(accountsList[x].accountId == accountId):
                accountsList[x].name = newValue
    elif toBeChanged == '3':
        for x in range(len(accountsList)):
            if(accountsList[x].accountId == accountId):
                accountsList[x].balance = int(newValue)

    main()

def delete():
    print("Type the account's ID you want to delete...")
    accountId = int(input())

    #A copy is created because as soon as we remove an item from the original list we would shrink it's length
    #And the for function wouldn't iterate properly
    listLengthNOW = accountsList.copy()

    for x in range(len(listLengthNOW)):
        if(listLengthNOW[x].accountId == accountId):
            accountsList.remove(accountsList[x])

    main()

def min():
    menorSaldo = accountsList[0].balance

    for x in range(len(accountsList)):
        if(accountsList[x].balance < menorSaldo):
            menorSaldo = accountsList[x].balance

    return menorSaldo

def max():
    maiorSaldo = accountsList[0].balance

    for x in range(len(accountsList)):
        if accountsList[x].balance > maiorSaldo:
            maiorSaldo = accountsList[x].balance

    return maiorSaldo

def avg():
    acumulador = 0
    divisor = 0

    for x in range(len(accountsList)):
        acumulador += accountsList[x].balance
        divisor = x+1

    return acumulador / divisor

def statistics():
    print("\nThe lowest balance is: ", min())
    print("The greatest balance is:", max())
    print("The average balance is: ", avg(), "\n")

def statement():
    print("Type the account's ID you want to take a statement...")
    accountId = int(input())

    for x in range(len(accountsList)):
        if accountsList[x].accountId == accountId:
            print("Your account's balance: ", accountsList[x].balance)

    main()

def deposit():
    print("Type the account's ID you want to make a deposit...")
    accountId = int(input())

    print("Type the deposit value...")
    depositValue = int(input())

    for x in range(len(accountsList)):
        if(accountsList[x].accountId == accountId):
            accountsList[x].balance += depositValue 

    main()

def withdraw():
    print("Type the account's ID you want to make a withdraw...")
    accountId = int(input())

    print("Type the withdraw value...")
    withdrawValue = int(input())

    for x in range(len(accountsList)):
        if(accountsList[x].accountId == accountId):
            if(accountsList[x].balance < withdrawValue):
                print("Transaction denied! Withdraw greater than balance...")
            else:
                accountsList[x].balance -= withdrawValue
    
    main()

def transfer():
    print("From which account do you want to transfer? Type it's ID...")
    originAccount = int(input())

    print("What is the transfer amount?")
    moneyAmount = int(input())

    print("To which account the money will be transfered? Type it's ID...")
    addressee = int(input())

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

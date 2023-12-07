def show_menu():
    print("/n==== Currency Converter ====")
    print("1.Convert USD to EUR")
    print("2.Convert EUR to USD")
    print("3.Convert USD to GBP")
    print("4.Convert GBP to USD")
    print("5.Quit")

def convert_currency(amount, exchange_rate):
    return amount * exchange_rate

def currency_converter():
    usd_to_eur_rate = 0.85
    usd_to_gbp_rate = 0.75

    while True:
        show_menu()

        choice = input("Put your choice (1-5):")

        if choice == '1':
            amount = float(input("Put the amount in USD now!: "))
            result = convert_currency(amount, usd_to_eur_rate)
            print(f"{amount} USD is equal to {result:.2f} EUR")
        elif choice == '2':
            amount = float(input("Put the amount in EUR now!: "))
            result = convert_currency(amount, 1 / usd_to_eur_rate)
            print(f"{amount} EUR is equal to {result:.2f} USD")
        elif choice == '3':
            amount = float(input("Put the amount in USD now!: "))
            result = convert_currency(amount, usd_to_gbp_rate)
            print(f"{amount} USD is equal to {result:.2f} GBP")
        elif choice == '4':
            amount = float(input("Put the amount in GBP now!: "))
            result = convert_currency(amount, 1 / usd_to_gbp_rate)
            print(f"{amount} GBP is equal to {result:.2f} USD")
        elif choice == '5':
            print("Quitting Currency Converter. Go Away!!!:)")
            break
        else:
            print("Bad choice. Better enter a number between 1 and 5")

currency_converter()


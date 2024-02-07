"""
    Program Purpose: program to convert an amount in Malaysian Ringgit (MYR) to a selected target currencies
    for example: US Dollar (USD), Euro (EUR), or British Pound (GBP).
    Programmer: ManDan
    Date: 7 February 2024
"""
def get_exchange_rates():
    """Retrieves and returns the exchange rates for USD, EUR, and GBP."""
    rates = {
        "USD": 0.25,
        "EUR": 0.21,
        "GBP": 0.18,
    }
    return rates

def get_exchange_rates():
    """Retrieves and returns the exchange rates for USD, EUR, and GBP."""
    return {
        "USD": 0.25,
        "EUR": 0.21,
        "GBP": 0.18,
    }

def convert_currency(amount, from_currency, to_currency):
    """Converts the given amount from one currency to another."""
    rates = get_exchange_rates()
    return amount * rates[to_currency] / rates[from_currency]

def main():
    """The main function that runs the currency converter program."""
    print("Currency Conversion Program")

    print("Exchange Rates:")
    for currency, rate in get_exchange_rates().items():
        print(f"{currency}: {rate:.2f}")

    to_currency = input("Choose the target currency (USD, EUR, GBP): ").upper()
    while to_currency not in ("USD", "EUR", "GBP"):
        print("Invalid choice. Please enter USD, EUR, or GBP.")
        to_currency = input("Choose the target currency (USD, EUR, GBP): ").upper()

    amount = float(input("Enter the amount in Malaysian Ringgit (MYR): "))
    while amount <= 0:
        print("Please enter a positive amount.")
        amount = float(input("Enter the amount in Malaysian Ringgit (MYR): "))

    converted_amount = convert_currency(amount, "MYR", to_currency)
    print(f"Equivalent amount in {to_currency}: {converted_amount:.2f}")

if __name__ == "__main__":
    main()


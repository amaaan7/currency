def get_amount():
    while True:
        try:
            amount = float(input('Enter the amount: '))
            if amount <= 0:
                raise ValueError()
            return amount
        except ValueError:
            print('Invalid amount')

def get_currency(label):
    currencies = ('IND', 'USD', 'EUR')
    while True:
        currency = input(f'{label} currency (IND/USD/EUR): ').upper()
        if currency not in currencies:
            print('Invalid Currency')
        else:
            return currency

def convert_to_all(amount, source_currency):
    exchange_rate = {
        'IND': { 'USD': 0.011, 'EUR': 0.009 },
        'USD': { 'EUR': 0.85, 'IND': 89.24  },
        'EUR': { 'USD': 1.16, 'IND': 103.51},
    }
    
    print(f'\n{amount} {source_currency} is equal to:')
    print('-' * 35)
    
    for target_currency in exchange_rate:
        if target_currency == source_currency:
            continue  # Skip same currency
        
        converted = amount * exchange_rate[source_currency][target_currency]
        print(f'{converted:.2f} {target_currency}')

def main():
    amount = get_amount()
    source_currency = get_currency('Source')
    convert_to_all(amount, source_currency)


if __name__=="__main__":
    main()
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
    
    results = {}  # Store conversion results
    
    for target_currency in exchange_rate:
        if target_currency == source_currency:
            continue
        
        converted = amount * exchange_rate[source_currency][target_currency]
        print(f'{converted:.2f} {target_currency}')
        results[target_currency] = converted
    
    return results  # Return the results

def main():
    history = []  # Create empty history list
    
    while True:
        amount = get_amount()
        source_currency = get_currency('Source')
        results = convert_to_all(amount, source_currency)
        
        # Save to history
        history.append({
            'amount': amount,
            'source': source_currency,
            'conversions': results
        })
        
        # Ask if user wants to continue
        again = input('\nConvert again? (y/n): ').lower()
        if again != 'y':
            break
    
    # Display history at the end
    print('\n' + '=' * 40)
    print('CONVERSION HISTORY')
    print('=' * 40)
    
    for i, record in enumerate(history, 1):
        print(f'\nConversion {i}:')
        print(f'{record["amount"]} {record["source"]} converted to:')
        for currency, value in record['conversions'].items():
            print(f'  → {value:.2f} {currency}')


if __name__=="__main__":
    main()
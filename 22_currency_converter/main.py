import json
from typing import Final
import requests

# Constants
BASE_URL: Final[str] = 'http://api.exchangeratesapi.io/v1/latest'
API_KEY: Final[str] = 'YOUR_KEY' # requested to create an account. I'll skip it


def get_rates(mock: bool = False) -> dict:
    """Get the current rates from a currency api"""
    if mock:
        with open('rates.json', 'r') as file:
            return json.load(file)
        
    # Make a live request for data
    payload: dict = {'access_key': API_KEY}
    request = requests.get(url=BASE_URL, params=payload)
    data: dict = request.json()
    return data


def get_currency(currency: str, rates: dict) -> float:
    """Get the exchange rate for the specified currency if it exists."""
    currency: str = currency
    if currency in rates.keys():
        return rates.get(currency)
    else:
        raise ValueError(f'"{currency}" is not a valid currency.')


def convert_currency(amount: float, base: str, vs: str, rates: dict) -> float:
    """Convert the base currency to the vs currency at the given rate."""

    # Get the rates
    base_rate: float = get_currency(base, rates)
    vs_rate: float = get_currency(vs, rates)

    # Make the conversion and return it
    #print(type(base_rate),type(vs_rate),type(amount))
    conversion: float = round((vs_rate / base_rate) *amount, 2)
    print(f'{amount:,.2f} ({base}) is: {conversion:,.2f} ({vs})')
    return conversion


def main():
    data: dict = get_rates(mock=True)
    rates: dict = data.get('rates')
    

    base: str = input(f"Enter initial currency: ").upper()
    vs: str = input(f"Enter vs currency: ").upper()
    
    retry_amount = True
    while retry_amount:
        try:
            amount: float = float(input(f"Insert the amount: "))
            retry_amount = False
        except ValueError:
            print(" Please enter a valid number.")
            
    convert_currency(amount, base, vs, rates=rates)

if __name__ == '__main__':
    main()

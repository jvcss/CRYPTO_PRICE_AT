import os
from binance.spot import Spot as ClientSpot
from datetime import date, datetime, timedelta
os.system('cls' if os.name == 'nt' else 'clear')

def value_of_crypto_at(crypto, date_obj: datetime):
    """
    Returns the value of the crypto currency at the given date and time
    """
    # Convert date string to datetime object
    #date_obj = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

    # Initialize Binance client
    client = ClientSpot()

    # Convert the date to milliseconds
    starting = int((date_obj).timestamp() * 1000)
    ending = int((date_obj + timedelta(seconds=1)).timestamp() * 1000)

    # Get historical klines (candlestick data) for the crypto pair
    kline = client.klines(
                            symbol=f"{crypto.upper()}USDT", 
                            interval='1s', limit=1, 
                            startTime=starting, 
                            endTime=ending
                        )

    if kline:
        # Extract the closing price from the kline
        closing_price = float(kline[0][4])
        return closing_price
    else:
        return None  # Data not available

def amount_in_usdt(amount, price):
    return amount * price

def symbols():
    client = ClientSpot()
    exchange_info = client.exchange_info()
    return [symbol['baseAsset'] for symbol in exchange_info['symbols'] if symbol['quoteAsset'] == 'USDT']


# # Example usage
# crypto_symbol = "ETH"  # Change to the desired cryptocurrency symbol
# desired_date = "2024-04-19 22:15:05"  # Change to the desired date and time
# crypto_value = value_of_crypto_at(crypto_symbol, desired_date)

# amount = 0.04263593

# print(f"The value of {crypto_symbol.upper()} at {desired_date} was ${crypto_value:.2f}" if crypto_value is not None else "Data not available")

# print(f'You had USD ${amount * crypto_value:.2f} at {desired_date}')

from imports import *


load_dotenv()

def get_usd_to_brl_rate():
    """Obtém a taxa de câmbio USD-BRL."""
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    response = requests.get(url)
    data = response.json()
    return data['rates']['BRL']

def get_binance_data(symbol):
    """Obtém dados de criptomoedas da Binance."""
    try:
        url = f'https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}'
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Conversão para BRL
        usd_to_brl_rate = get_usd_to_brl_rate() or 1.0
        price_in_usd = float(data['lastPrice'])
        price_in_brl = price_in_usd * usd_to_brl_rate
        
        return {
            'symbol': symbol,
            'price_in_usd': price_in_usd,
            'price_in_brl': price_in_brl,
            'change_percent': float(data['priceChangePercent'])
        }
    except requests.RequestException as e:
        print(f"Erro ao buscar dados da Binance para {symbol}: {e}")
        return None

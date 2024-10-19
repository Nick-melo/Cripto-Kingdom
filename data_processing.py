from imports import *
from api import get_binance_data
from graph import create_graph

def simulate_price_data(base_price, variation=0.02, points=10):
    """Simula dados de preço com base em um preço base."""
    return [base_price * (1 + np.random.uniform(-variation, variation)) for _ in range(points)]

def format_currency(value):
    """Formata o valor como moeda brasileira."""
    return f"R${value:,.2f}"

def create_report(cryptos, icon_path):
    """Gera um DataFrame com dados de criptomoedas e gráficos."""
    data_list = []
    for symbol in cryptos:
        data = get_binance_data(symbol)
        if data:
            price_brl = data['price_in_brl']
            change_price = float(data['change_percent'])
            price_data = simulate_price_data(price_brl)  # Simulando dados de preço
            graph = create_graph(price_data, symbol[:-4])  # Criando gráfico
            
            # Gerando ícone da moeda
            icon_file = os.path.join(icon_path, f'{symbol[:-4]}.png')
            img = Image.open(icon_file).convert("RGBA").resize((40, 40)) if os.path.exists(icon_file) else Image.open('placeholder.png').convert("RGBA").resize((40, 40))
            
            data_list.append([symbol[:-4], price_brl, change_price, img, graph])

    # Criando DataFrame
    df = pd.DataFrame(data_list, columns=["Moeda", "Preço", "Variação", "Ícone", "Gráfico"])
    return df

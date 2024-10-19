from imports import *

def create_graph(price_data, symbol):
    """Cria um gráfico de variação de preço e retorna como um buffer."""
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(price_data, color='green' if price_data[-1] >= price_data[0] else 'red')
    ax.set_title(f'{symbol} - Variação de Preço', fontsize=20)
    ax.set_xlabel('Tempo', fontsize=15)
    ax.set_ylabel('Preço (R$)')
    ax.grid()

    img_buffer = BytesIO()
    fig.savefig(img_buffer, format='png')
    plt.close(fig)
    img_buffer.seek(0)
    return img_buffer
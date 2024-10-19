from imports import *
from pdf_report import create_pdf_report
from email_sender import send_email
from data_processing import create_report

def main():
    """Função principal do script."""
    cryptos = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'XRPUSDT']
    icon_path = './icons'

    df = create_report(cryptos, icon_path)  # Criando DataFrame com dados das criptomoedas
    pdf_path = 'relatorio_criptomoedas.pdf'
    create_pdf_report(df, pdf_path)  # Gerando relatório PDF

    receiver_email = 'Email@example.com' #coloque um email 
    send_email(receiver_email, pdf_path)  # Enviando o relatório por e-mail

    print(f"Relatório gerado em {pdf_path}")

if __name__ == '__main__':
    main()

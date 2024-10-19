from imports import *
from data_processing import format_currency

def create_pdf_report(df, pdf_path):
    """Cria um relatório PDF com os dados das criptomoedas."""
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4
    y_position = height - 50

    # Título do relatório
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, y_position, "Relatório de Criptomoedas")
    y_position -= 70

    # Cabeçalho da tabela
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, y_position, "Moeda")
    c.drawString(150, y_position, "Preço (R$)")
    c.drawString(250, y_position, "Variação (%)")
    y_position -= 30

    # Adicionando dados da tabela
    for index, row in df.iterrows():
        c.setFont("Helvetica", 12)
        if row['Ícone'] is not None:
            img_reader = ImageReader(row['Ícone'])
            c.drawImage(img_reader, 50, y_position - 10, width=30, height=30)

        c.drawString(100, y_position, row['Moeda'])
        c.drawString(150, y_position, format_currency(row['Preço']))
        
        # Variação de preço
        color = colors.green if row['Variação'] >= 0 else colors.red
        c.setFillColor(color)
        c.drawString(250, y_position, f"{row['Variação']:.2f}%")
        c.setFillColor(colors.black)

        # Gráfico
        graph_reader = ImageReader(row['Gráfico'])
        c.drawImage(graph_reader, 350, y_position - 25, width=200, height=100)

        y_position -= 90

        if y_position < 100:
            c.showPage()
            y_position = height - 50

    c.save()
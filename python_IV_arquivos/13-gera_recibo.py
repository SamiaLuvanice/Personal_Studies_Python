from fpdf import FPDF
from pathlib import Path
from num2words import num2words
from datetime import date
import re


cliente = input("Informe o nome do cliente:")
consulta = input("Informe o tipo de consulta:")
vlr = input("Informe o valor da consulta:")

vlr_normalizado = vlr.replace(".", "").replace(",", ".")

try:
    valor_float = float(vlr_normalizado)
except ValueError:
    raise ValueError("Valor inválido. Informe um número, por exemplo: 150 ou 150,50")

vlr_msg = f"{valor_float:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".") + " reais"
vlr_extenso = num2words(valor_float, lang='pt_BR')
vlr_extenso_msg = f"{vlr_extenso} reais"
data = date.today()
dia = data.day
mes = data.month
ano = data.year

base_dir = Path(__file__).resolve().parent
logo_path = base_dir / "logo.png"

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=20)
pdf.image(str(logo_path), x=0, y=0)
pdf.text(162, 45, vlr_msg)
pdf.text(80, 86, cliente)
pdf.text(80, 108, vlr_extenso_msg)
pdf.text(80, 135, consulta)
pdf.set_text_color(255, 255, 255)
pdf.text(30, 193, str(dia))
pdf.text(50, 193, str(mes))
pdf.text(70, 193, str(ano))
cliente_limpo = re.sub(r'[<>:"/\\|?*]', "_", cliente.strip())
nome_arquivo = f"{cliente_limpo}_{dia}_{mes}_{ano}"
pdf.output(f"{nome_arquivo}.pdf")
print("Recibo gerado com sucesso!")

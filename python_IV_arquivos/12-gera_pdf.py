from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', size=16)
pdf.cell(40, 10, txt='Hello World', ln=1, align='C')
pdf.output('hello_world.pdf')
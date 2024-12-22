from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 16)
# Header
pdf.cell(190, 10, "CS50 Shirtificate", align='C')
pdf.output("tuto1.pdf")

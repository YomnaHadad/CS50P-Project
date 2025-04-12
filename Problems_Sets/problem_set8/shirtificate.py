from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

name = input("Name: ")

pdf.set_font("helvetica", "B", size = 35)
pdf.cell(200, 10, text="CS50 Shirtificate", align='C')

pdf.image("shirtificate.png" , x=20, y=40, w=175)

pdf.set_text_color(255, 255, 255)
pdf.set_font("helvetica" , size = 23)
pdf.cell(-201,176, text=f"{name} took CS50", align='C')

pdf.output("shirtificate.pdf")

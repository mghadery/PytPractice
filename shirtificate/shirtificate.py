from fpdf import FPDF

def make_shirt_pdf(text, pdf_name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(False)
    pdf.add_page()

    title="CS50 Shirtificate"
    pdf.set_font("helvetica", style="B", size=22)
    width = pdf.get_string_width(title)
    pdf.set_x((210 - width) / 2)
    pdf.cell(width, 0, title)
    pdf.ln()

    pdf.set_x(10)
    y1 = pdf.get_y()
    pdf.image("./shirtificate.png", w = 190, keep_aspect_ratio = True)
    y2 = pdf.get_y()

    pdf.set_font("helvetica", style="B", size=16)
    pdf.set_y(int(2*y1/3 + y2/3))
    width = pdf.get_string_width(text)
    pdf.set_x((210 - width) / 2)
    pdf.set_text_color(250, 250, 250)
    pdf.cell(width, 0, text)

    pdf.output(pdf_name)


if __name__ == "__main__":
    name = input("Name: ")
    make_shirt_pdf(name.strip() + " took CS50", "shirtificate.pdf")

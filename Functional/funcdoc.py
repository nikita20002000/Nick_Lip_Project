from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT, WD_LINE_SPACING
import datetime
import pictures


def create_titul(name, surname, group):
    doc = Document()
    style = doc.styles['Normal']

    style.font.name = 'Times New Roman'
    style.font.size = Pt(14)
    style.font.bold = True
    WD_LINE_SPACING.EXACTLY = 1.5
    with open("MSU_LOGO.jpg", "rb") as img:
        p = doc.add_picture(img)

    last_p = doc.paragraphs[-1]
    last_p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

    p = doc.add_paragraph('МОСКОВСКИЙ ГОСУДАРСТВЕННЫЙ УНИВЕРСИТЕТ', style)
    p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    p.bold = True
    p.paragraph_format.line_spacing = WD_LINE_SPACING.EXACTLY

    p = doc.add_paragraph('имени М.В.ЛОМОНОСОВА', style)
    p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    p.bold = True
    p.paragraph_format.line_spacing = WD_LINE_SPACING.EXACTLY

    p = doc.add_paragraph("ФАКУЛЬТЕТ ГОСУДАРСТВЕННОГО УПРАВЛЕНИЯ", style)
    p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    p.bold = True
    p.paragraph_format.line_spacing = WD_LINE_SPACING.EXACTLY



    p = doc.add_paragraph("Тут будет кафедра", style)
    p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    p.bold = True
    p.paragraph_format.line_spacing = WD_LINE_SPACING.EXACTLY

    p = doc.add_paragraph("name_of_discipline", style)
    p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    p.bold = True
    p.paragraph_format.line_spacing = WD_LINE_SPACING.EXACTLY

    k = doc.add_paragraph()
    k.paragraph_format.line_spacing = WD_LINE_SPACING.EXACTLY
    k.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    k = doc.add_paragraph()
    k.paragraph_format.line_spacing = WD_LINE_SPACING.EXACTLY
    k.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
    k = doc.add_paragraph()
    k.paragraph_format.line_spacing = WD_LINE_SPACING.EXACTLY
    k.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER


    k = doc.add_paragraph("Выполнил:", style)
    k.bold = True
    k.paragraph_format.line_spacing = WD_LINE_SPACING.EXACTLY
    k.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

    p = doc.add_paragraph(f"Студент группы здесь будет группа", style)
    p.paragraph_format.line_spacing = WD_LINE_SPACING.EXACTLY
    p.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

    p = doc.add_paragraph("Новиков Никита Андреевич", style)
    p.paragraph_format.line_spacing = WD_LINE_SPACING.EXACTLY
    p.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

    p = doc.add_paragraph()
    p.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

    p = doc.add_paragraph("Проверила:", style)
    p.paragraph_format.line_spacing = WD_LINE_SPACING.EXACTLY
    p.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

    p = doc.add_paragraph("scientifique_degree", style)
    p.paragraph_format.line_spacing = WD_LINE_SPACING.EXACTLY
    p.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

    p = doc.add_paragraph("name_of_tutor", style)
    p.paragraph_format.line_spacing = WD_LINE_SPACING.EXACTLY
    p.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

    year = datetime.datetime.strftime(datetime.datetime.now(), '%Y')            #Добавил год в титульник
    p = doc.add_paragraph(f"{year}", style)
    p.paragraph_format.line_spacing = WD_LINE_SPACING.EXACTLY
    p.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER











    doc.save('your_doc).docx')


create_titul("Тыф", "вывндекс", "Группа")
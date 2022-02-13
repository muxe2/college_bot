import json
import urllib.request

import fitz
import pdfplumber

import main


def update_raspisanie():
    pdfs = ['1k.pdf', '2k.pdf', '3k.pdf', '4k.pdf']
    url = ['http://www.pl130.ru/doc/19/1k.pdf', 'http://www.pl130.ru/doc/19/2k.pdf',
           'http://www.pl130.ru/doc/19/3k.pdf', 'http://www.pl130.ru/doc/19/4k.pdf']

    with open("raspis.json", "rt", encoding="utf-8") as file:
        settings = json.load(file)

    for i in url:
        file = i.split('/')[5]
        urllib.request.urlretrieve(i, f'course_pdf/{file}')

    for pdffile in pdfs:
        course = list(pdffile)[0]
        pdffile = f'course_pdf/{pdffile}'
        with pdfplumber.open(pdffile) as pdf:
            totalpages = len(pdf.pages)
            doc = fitz.open(pdffile)
            for i in range(0, totalpages):
                pageobj = pdf.pages[i]
                group = pageobj.extract_text().split()[:5][2].replace("_", '')
                print(f'Обработка {group}' + '\r', end='')
                page = doc.load_page(i)
                pix = page.get_pixmap()
                output = f"courses/{course}/{group}"
                pix.save(f"{output}.png")
                photo = main.send(photo=output, render=True)
                settings["list"][group] = photo
                with open("raspis.json", "wt", encoding="utf-8") as f:
                    json.dump(settings, f, indent=4)
                    
    print('Расписание обнавлено')

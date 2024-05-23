from pypdf import PdfMerger

pdfs = ['pdf/pdf01.pdf', 'pdf/pdf02.pdf', 'pdf/pdf03.pdf', 'pdf/pdf04.pdf', 'pdf/pdf05.pdf', 'pdf/pdf06.pdf', 'pdf/pdf07.pdf', 'pdf/pdf08.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged/result.pdf")
merger.close()
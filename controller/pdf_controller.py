class PDFController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.controller = self

    def convert_pdf_to_excel(self, pdf_file, excel_file):
        return self.model.convert_pdf_to_excel(pdf_file, excel_file)

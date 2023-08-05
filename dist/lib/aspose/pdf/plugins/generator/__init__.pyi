import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class PdfGeneratorTableBuilder:
    '''Class represents builder for table in pdf page.'''
    
    def add_row(self) -> aspose.pdf.plugins.generator.PdfGeneratorTableRowBuidler:
        '''Add new row to table.
        
        :returns: Instance of current :class:`PdfGeneratorTableRowBuidler`.'''
        ...
    
    def add_table(self) -> aspose.pdf.plugins.generator.PdfGeneratorTableBuilder:
        '''Add new table to document.
        
        :returns: Instance of current :class:`PdfGeneratorTableBuilder`.'''
        ...
    
    def set_page(self, page: int) -> aspose.pdf.plugins.generator.PdfGeneratorTableBuilder:
        '''Set the page number to place the table.
        
        :param page: Page number to insert table.
        :returns: Instance of current :class:`aspose.pdf.plugins.PdfGeneratorTableOptions`.'''
        ...
    
    ...

class PdfGeneratorTableCellBuilder(aspose.pdf.plugins.generator.PdfGeneratorTableRowBuidler):
    '''Class represents builder for table cell.'''
    
    def add_cell(self) -> aspose.pdf.plugins.generator.PdfGeneratorTableCellBuilder:
        '''Add cell to table.
        
        :returns: Instance of current :class:`PdfGeneratorTableCellBuilder`.'''
        ...
    
    def add_paragraph(self, paragraph: list[aspose.pdf.BaseParagraph]) -> aspose.pdf.plugins.generator.PdfGeneratorTableCellBuilder:
        '''Add paragraphs to table cell.
        
        :param paragraph:
        :returns: Instance of current :class:`PdfGeneratorTableCellBuilder`.'''
        ...
    
    ...

class PdfGeneratorTableRowBuidler(aspose.pdf.plugins.generator.PdfGeneratorTableBuilder):
    '''Class represents builder for table row.'''
    
    def add_row(self) -> aspose.pdf.plugins.generator.PdfGeneratorTableRowBuidler:
        '''Overriding AddRow.
        
        :returns: Instance of current :class:`PdfGeneratorTableRowBuidler`.'''
        ...
    
    def add_cell(self) -> aspose.pdf.plugins.generator.PdfGeneratorTableCellBuilder:
        '''Add cell to table row.
        
        :returns: Instance of created :class:`PdfGeneratorTableCellBuilder`.'''
        ...
    
    ...


from aspose.pdf.plugins import generator
import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class CheckBoxFieldCreateOptions(aspose.pdf.plugins.FieldCreateOptions):
    '''Represents options for creating CheckBoxField.'''
    
    def __init__(self, page_num: int, rect: aspose.pdf.Rectangle):
        '''Initializes a new instance of the :class:`CheckBoxFieldCreateOptions` object, that containing parameters for created and added CheckBoxField.
        
        :param page_num: Page number on which the added CheckBoxField will be located.
        :param rect: Sets CheckBoxField rectangle.'''
        ...
    
    @property
    def checked(self) -> bool:
        '''Gets/sets the value to determine whether created CheckboxField is checked or not (if will be set).'''
        ...
    
    @checked.setter
    def checked(self, value: bool):
        ...
    
    @property
    def style(self) -> aspose.pdf.forms.BoxStyle:
        '''Gets/sets the value to determine property Style for created CheckboxField (if will be set).'''
        ...
    
    @style.setter
    def style(self, value: aspose.pdf.forms.BoxStyle):
        ...
    
    ...

class ComboBoxFieldCreateOptions(aspose.pdf.plugins.FieldCreateOptions):
    '''Represents options for creating ComboBoxField.'''
    
    def __init__(self, page_num: int, rect: aspose.pdf.Rectangle):
        '''Initializes a new instance of the :class:`ComboBoxFieldCreateOptions` object, that containing parameters for created and added ComboBoxField.
        
        :param page_num: Page number on which the added ComboBoxField will be located.
        :param rect: Sets ComboBoxField rectangle.'''
        ...
    
    @property
    def editable(self) -> bool:
        '''Gets/sets the value to determine whether created ComboBoxField is editable or not (if will be set).'''
        ...
    
    @editable.setter
    def editable(self, value: bool):
        ...
    
    @property
    def options(self) -> None:
        '''Gets/sets the value to determine property Options for created ComboBoxField (if will be set).'''
        ...
    
    @options.setter
    def options(self, value: None):
        ...
    
    @property
    def selected(self) -> int:
        '''Gets/sets the value to determine property Selected for created ComboBoxField (if will be set).'''
        ...
    
    @selected.setter
    def selected(self, value: int):
        ...
    
    ...

class FieldCreateOptions(aspose.pdf.plugins.FieldOptions):
    '''Represents options for creating Field.'''
    
    ...

class FieldOptions:
    '''Represents Field options. Base class for PdfFormFieldCreateOptions and PdfFormFillFieldOptions.'''
    
    @property
    def update_appearance_on_convert(self) -> bool:
        '''Gets/sets the value to determine whether created/modified field is update appearance on convert or not (if will be set).'''
        ...
    
    @update_appearance_on_convert.setter
    def update_appearance_on_convert(self, value: bool):
        ...
    
    @property
    def use_font_subset(self) -> bool:
        '''Gets/sets the value to determine whether created/modified field is use font subset or not (if will be set).'''
        ...
    
    @use_font_subset.setter
    def use_font_subset(self, value: bool):
        ...
    
    @property
    def flags(self) -> aspose.pdf.annotations.AnnotationFlags:
        '''Gets/sets the value to determine property Flags for created/modified field (if will be set).'''
        ...
    
    @flags.setter
    def flags(self, value: aspose.pdf.annotations.AnnotationFlags):
        ...
    
    @property
    def contents(self) -> str:
        '''Gets/sets the value to determine property Contents for created/modified field (if will be set).'''
        ...
    
    @contents.setter
    def contents(self, value: str):
        ...
    
    @property
    def name(self) -> str:
        '''Gets/sets the value to determine property Name for created/modified field (if will be set).'''
        ...
    
    @name.setter
    def name(self, value: str):
        ...
    
    @property
    def color(self) -> aspose.pdf.Color:
        '''Gets/sets the value to determine property Color for created/modified field (if will be set).'''
        ...
    
    @color.setter
    def color(self, value: aspose.pdf.Color):
        ...
    
    @property
    def text_horizontal_alignment(self) -> aspose.pdf.HorizontalAlignment:
        '''Gets/sets the value to determine property TextHorizontalAlignment for created/modified field (if will be set).'''
        ...
    
    @text_horizontal_alignment.setter
    def text_horizontal_alignment(self, value: aspose.pdf.HorizontalAlignment):
        ...
    
    @property
    def default_appearance(self) -> aspose.pdf.annotations.DefaultAppearance:
        '''Gets/sets the value to determine property DefaultAppearance for created/modified field (if will be set).'''
        ...
    
    @default_appearance.setter
    def default_appearance(self, value: aspose.pdf.annotations.DefaultAppearance):
        ...
    
    @property
    def read_only(self) -> bool:
        '''Gets/sets the value to determine whether created/modified field is read only or not (if will be set).'''
        ...
    
    @read_only.setter
    def read_only(self, value: bool):
        ...
    
    @property
    def required(self) -> bool:
        '''Gets/sets the value to determine whether created/modified field is required or not (if will be set).'''
        ...
    
    @required.setter
    def required(self, value: bool):
        ...
    
    @property
    def exportable(self) -> bool:
        '''Gets/sets the value to determine whether created/modified field is exportable or not (if will be set).'''
        ...
    
    @exportable.setter
    def exportable(self, value: bool):
        ...
    
    @property
    def partial_name(self) -> str:
        '''Gets/sets the value to determine property PartialName for created/modified field (if will be set).'''
        ...
    
    @partial_name.setter
    def partial_name(self, value: str):
        ...
    
    @property
    def alternate_name(self) -> str:
        '''Gets/sets the value to determine property AlternateName for created/modified field (if will be set).'''
        ...
    
    @alternate_name.setter
    def alternate_name(self, value: str):
        ...
    
    @property
    def mapping_name(self) -> str:
        '''Gets/sets the value to determine property MappingName for created/modified field (if will be set).'''
        ...
    
    @mapping_name.setter
    def mapping_name(self, value: str):
        ...
    
    @property
    def value(self) -> str:
        '''Gets/sets the value to determine property Value for created/modified field (if will be set).'''
        ...
    
    @value.setter
    def value(self, value: str):
        ...
    
    @property
    def is_shared_field(self) -> bool:
        '''Gets/sets the value to determine whether created/modified field is shared field or not (if will be set).'''
        ...
    
    @is_shared_field.setter
    def is_shared_field(self, value: bool):
        ...
    
    @property
    def fit_into_rectangle(self) -> bool:
        '''Gets/sets the value to determine whether created/modified field is fit into rectangle or not (if will be set).'''
        ...
    
    @fit_into_rectangle.setter
    def fit_into_rectangle(self, value: bool):
        ...
    
    @property
    def max_font_size(self) -> float:
        '''Gets/sets the value to determine property MaxFontSize for created/modified field (if will be set).'''
        ...
    
    @max_font_size.setter
    def max_font_size(self, value: float):
        ...
    
    @property
    def min_font_size(self) -> float:
        '''Gets/sets the value to determine property MinFontSize for created/modified field (if will be set).'''
        ...
    
    @min_font_size.setter
    def min_font_size(self, value: float):
        ...
    
    @property
    def highlighting(self) -> aspose.pdf.annotations.HighlightingMode:
        '''Gets/sets the value to determine property Highlighting for created/modified field (if will be set).'''
        ...
    
    @highlighting.setter
    def highlighting(self, value: aspose.pdf.annotations.HighlightingMode):
        ...
    
    ...

class FileDataSource:
    '''Represents file data source for load and save operations of a plugin.'''
    
    def __init__(self, path: str):
        '''Initializes new file data source with the specified path.
        
        :param path: A string representing the path to the source file.'''
        ...
    
    @property
    def data_type(self) -> None:
        '''Type of data source (file).'''
        ...
    
    @property
    def path(self) -> str:
        '''Gets the path to the file of the current data source.'''
        ...
    
    ...

class FileResult:
    '''Represents operation result in the form of string path to file.'''
    
    def to_file(self) -> str:
        '''Tries to convert the result to a file.
        
        :returns: A string representing the path to the output file if the result is file; otherwise ``None``.'''
        ...
    
    def to_stream(self) -> Any:
        '''Tries to convert the result to a stream object.
        
        :returns: A stream object representing the output data if the result is stream; otherwise ``None``.'''
        ...
    
    @property
    def is_file(self) -> bool:
        '''Indicates whether the result is a path to an output file.
        
        :returns: ``True`` if the result is a file; otherwise ``False``.'''
        ...
    
    @property
    def is_stream(self) -> bool:
        '''Indicates whether the result is an output stream.
        
        :returns: ``True`` if the result is a stream object; otherwise ``False``.'''
        ...
    
    @property
    def is_string(self) -> bool:
        '''Indicates whether the result is a text string.
        
        :returns: ``True`` if the result is a string; otherwise ``False``.'''
        ...
    
    @property
    def data(self) -> object:
        '''Gets raw data.
        
        :returns: An ``object`` representing output data.'''
        ...
    
    ...

class IDataSource:
    '''General data source interface that defines common members that concrete data sources should implement.'''
    
    @property
    def data_type(self) -> None:
        '''Type of data source (file or stream).'''
        ...
    
    ...

class IOperationResult:
    '''General operation result interface that defines common methods that concrete plugin operation result should implement.'''
    
    def to_file(self) -> str:
        '''Tries to convert the result to the file.
        
        :returns: A string representing the path to the output file if the result is file; otherwise ``None``.'''
        ...
    
    def to_stream(self) -> Any:
        '''Tries to convert the result to the stream object.
        
        :returns: A stream object representing the output data if the result is stream; otherwise ``None``.'''
        ...
    
    @property
    def is_file(self) -> bool:
        '''Indicates whether the result is a path to an output file.
        
        :returns: ``True`` if the result is a file; otherwise ``False``.'''
        ...
    
    @property
    def is_stream(self) -> bool:
        '''Indicates whether the result is an output stream.
        
        :returns: ``True`` if the result is a stream object; otherwise ``False``.'''
        ...
    
    @property
    def is_string(self) -> bool:
        '''Indicates whether the result is a text string.
        
        :returns: ``True`` if the result is a string; otherwise ``False``.'''
        ...
    
    @property
    def data(self) -> object:
        '''Gets raw data.
        
        :returns: An ``object`` representing output data.'''
        ...
    
    ...

class IPlugin:
    '''General plugin interface that defines common methods that concrete plugin should implement.'''
    
    def process(self, options: aspose.pdf.plugins.IPluginOptions) -> aspose.pdf.plugins.ResultContainer:
        '''Charges a plugin to process with defined options
        
        :param options: An options object containing instructions for the plugin
        :returns: An ResultContainer object containing the result of the processing'''
        ...
    
    ...

class IPluginOptions:
    '''General plugin option interface that defines common methods that concrete plugin option should implement.'''
    
    ...

class PdfConverter:
    '''Represents PdfConverter plugin.'''
    
    def __init__(self):
        ...
    
    def process(self, options: aspose.pdf.plugins.IPluginOptions) -> aspose.pdf.plugins.ResultContainer:
        '''Starts the PdfConverter processing with the specified parameters.
        
        :param options: An options object containing instructions for the PdfConverter.
        :returns: An ResultContainer object containing the result of the operation.
        
        :raises System.NotSupportedException:'''
        ...
    
    ...

class PdfConverterHtmlToPdfOptions(aspose.pdf.plugins.PdfConverterOptions):
    '''Represents HTML to PDF converter options for :class:`PdfConverter` plugin.'''
    
    def __init__(self):
        ...
    
    @property
    def is_render_to_single_page(self) -> bool:
        '''Gets or sets rendering all document to single page.'''
        ...
    
    @is_render_to_single_page.setter
    def is_render_to_single_page(self, value: bool):
        ...
    
    @property
    def base_path(self) -> str:
        '''The base path/url for the html file.'''
        ...
    
    @base_path.setter
    def base_path(self, value: str):
        ...
    
    @property
    def html_media_type(self) -> aspose.pdf.HtmlMediaType:
        '''Gets or sets possible media types used during rendering.'''
        ...
    
    @html_media_type.setter
    def html_media_type(self, value: aspose.pdf.HtmlMediaType):
        ...
    
    @property
    def page_layout_option(self) -> aspose.pdf.HtmlPageLayoutOption:
        '''Gets or sets layout option.'''
        ...
    
    @page_layout_option.setter
    def page_layout_option(self, value: aspose.pdf.HtmlPageLayoutOption):
        ...
    
    @property
    def page_info(self) -> aspose.pdf.PageInfo:
        '''Gets or sets document page info.'''
        ...
    
    @page_info.setter
    def page_info(self, value: aspose.pdf.PageInfo):
        ...
    
    ...

class PdfConverterOptions:
    '''Represents options for :class:`PdfConverter` plugin.'''
    
    def add_data_source(self, data_source: aspose.pdf.plugins.IDataSource) -> None:
        '''Adds new data source to the PdfConverter plugin data collection.
        
        :param data_source: Data source to add.'''
        ...
    
    def add_save_data_source(self, save_data_source: aspose.pdf.plugins.IDataSource) -> None:
        '''Adds new data source to the PdfToXLSXConverterOptions plugin data collection.
        
        :param save_data_source: Data source (file or stream) for saving operation results.
        :raises System.NotImplementedException:'''
        ...
    
    @property
    def data_collection(self) -> None:
        '''Returns PdfConverterOptions plugin data collection.'''
        ...
    
    @property
    def save_targets_collection(self) -> None:
        '''Gets collection of added targets for saving operation results.'''
        ...
    
    @property
    def operation_name(self) -> str:
        '''Returns operation name.'''
        ...
    
    ...

class PdfConverterToExcelOptions(aspose.pdf.plugins.PdfConverterOptions):
    '''Represents PDF to XLSX converter options for :class:`PdfConverter` plugin.'''
    
    def __init__(self):
        ...
    
    @property
    def minimize_the_number_of_worksheets(self) -> bool:
        '''Set true if you need to minimize the number of worksheets in resultant workbook.
        Default value is false; it means save of each PDF page as separated worksheet.'''
        ...
    
    @minimize_the_number_of_worksheets.setter
    def minimize_the_number_of_worksheets(self, value: bool):
        ...
    
    @property
    def insert_blank_column_at_first(self) -> bool:
        '''Set true if you need inserting of blank column as the first column of worksheet.
        Default value is false; it means that blank column will not be inserted.'''
        ...
    
    @insert_blank_column_at_first.setter
    def insert_blank_column_at_first(self, value: bool):
        ...
    
    @property
    def format(self) -> None:
        '''Output format.'''
        ...
    
    @format.setter
    def format(self, value: None):
        ...
    
    ...

class PdfConverterToHtmlOptions(aspose.pdf.plugins.PdfConverterOptions):
    '''Represents PDF to HTML converter options for :class:`PdfConverter` plugin.'''
    
    @overload
    def __init__(self):
        '''Initializes new instance of the :class:`PdfConverterToHtmlOptions` object with default options.'''
        ...
    
    @overload
    def __init__(self, output_data_type):
        '''Initializes a new instance of the :class:`PdfConverterToHtmlOptions` object for the specified output data type.
        
        :param output_data_type: Output data type.'''
        ...
    
    @property
    def operation_name(self) -> str:
        '''Gets name of the operation.'''
        ...
    
    @property
    def output_data_type(self) -> None:
        '''Gets output data type.'''
        ...
    
    ...

class PdfExtractor:
    '''Represents PdfExtractor plugin.
    
    The :class:`PdfExtractor` object is used to extract text, images, and other types of content that may occur on the pages of PDF documents.'''
    
    def __init__(self):
        ...
    
    def process(self, pdf_extractor_options: aspose.pdf.plugins.IPluginOptions) -> aspose.pdf.plugins.ResultContainer:
        '''Starts PdfExtractor processing with the specified parameters.
        
        :param pdf_extractor_options: An options object containing instructions for the PdfExtractor.
        :returns: A ResultContainer object containing the result of the extraction.'''
        ...
    
    ...

class PdfExtractorOptions:
    '''Represents options for the PdfExtractor plugin.
    
    The :class:`PdfExtractorOptions` contains base functions to add data (files, streams) representing input PDF documents.
    Please create :class:`PdfExtractorToTextOptions` or PdfExtractorToImageOptions instead of this.'''
    
    def add_data_source(self, data_source: aspose.pdf.plugins.IDataSource) -> None:
        '''Adds new data source to the PdfExtractor plugin data collection.
        
        :param data_source: Data source to add.'''
        ...
    
    @property
    def data_collection(self) -> None:
        '''Returns PdfExtractor plugin data collection.'''
        ...
    
    @property
    def operation_name(self) -> str:
        '''Returns operation name'''
        ...
    
    ...

class PdfExtractorToImageOptions(aspose.pdf.plugins.PdfExtractorOptions):
    '''Represents images extraction options for the PdfExtractor plugin.
    
    The :class:`PdfExtractorToImageOptions` object is used to set Aspose.Pdf.Plugins.PdfExtractorToImageOptions.ImageExtractionMode and another options for the images extraction operation.
    Also, it inherits functions to add data (files, streams) representing input PDF documents.'''
    
    def __init__(self):
        ...
    
    @property
    def operation_name(self) -> str:
        '''Returns name of the operation.'''
        ...
    
    @property
    def extraction_mode(self) -> None:
        '''Gets image extraction mode.'''
        ...
    
    ...

class PdfExtractorToTextOptions(aspose.pdf.plugins.PdfExtractorOptions):
    '''Represents text extraction options for the PdfExtractor plugin.
    
    The :class:`PdfExtractorToTextOptions` object is used to set Aspose.Pdf.Plugins.PdfExtractorToTextOptions.TextFormattingMode and another options for the text extraction operation.
    Also, it inherits functions to add data (files, streams) representing input PDF documents.'''
    
    @overload
    def __init__(self, formatting_mode):
        '''Initializes a new instance of the :class:`PdfExtractorToTextOptions` object for the specified text formatting mode.
        
        :param formatting_mode: Text formatting mode value.'''
        ...
    
    @overload
    def __init__(self):
        '''Initializes a new instance of the :class:`PdfExtractorToTextOptions` object with 'Raw' (default) text formatting mode.'''
        ...
    
    @property
    def operation_name(self) -> str:
        '''Returns name of the operation.'''
        ...
    
    @property
    def formatting_mode(self) -> None:
        '''Gets formatting mode.'''
        ...
    
    ...

class PdfForm:
    '''Represents PdfForm plugin.'''
    
    def __init__(self):
        ...
    
    def process(self, options: aspose.pdf.plugins.IPluginOptions) -> aspose.pdf.plugins.ResultContainer:
        '''Starts the PdfForm processing with the specified parameters.
        
        :param options: An options object containg instructions for the PdfForm.
        :returns: An ResultContainer object containg the result of the operation.
        
        :raises System.ArgumentException:'''
        ...
    
    ...

class PdfFormAddFieldsOptions(aspose.pdf.plugins.PdfFormOptions):
    '''Represents options for add Fields to document by PdfForm plugin.'''
    
    def __init__(self, fields_create_options):
        ...
    
    @property
    def get_fields_create_options(self) -> None:
        '''Gets List of FieldCreateOptions for creating Fields in method Process call.'''
        ...
    
    ...

class PdfFormCheckBoxFieldSetOptions(aspose.pdf.plugins.PdfFormFieldSetOptions):
    '''Represents options for set properties in CheckboxField.'''
    
    def __init__(self):
        ...
    
    @property
    def checked(self) -> bool:
        ...
    
    @checked.setter
    def checked(self, value: bool):
        ...
    
    @property
    def style(self) -> aspose.pdf.forms.BoxStyle:
        ...
    
    @style.setter
    def style(self, value: aspose.pdf.forms.BoxStyle):
        ...
    
    ...

class PdfFormComboBoxFieldSetOptions(aspose.pdf.plugins.PdfFormFieldSetOptions):
    '''Represents options for set properties in ComboBoxField.'''
    
    def __init__(self):
        ...
    
    @property
    def editable(self) -> bool:
        ...
    
    @editable.setter
    def editable(self, value: bool):
        ...
    
    @property
    def options(self) -> None:
        ...
    
    @options.setter
    def options(self, value: None):
        ...
    
    @property
    def selected(self) -> int:
        ...
    
    @selected.setter
    def selected(self, value: int):
        ...
    
    ...

class PdfFormExportValuesToCsvOptions(aspose.pdf.plugins.PdfFormOptions):
    '''Represents options for export Value property of specified fields (not annotations).'''
    
    @property
    def get_delimeter(self) -> str:
        '''Gets delimeter used for exported values.'''
        ...
    
    ...

class PdfFormFieldSetOptions(aspose.pdf.plugins.FieldOptions):
    '''Represents options for set properties in Field.'''
    
    def __init__(self):
        ...
    
    @property
    def rect(self) -> aspose.pdf.Rectangle:
        '''Rectangle that be setted to field(s).'''
        ...
    
    @rect.setter
    def rect(self, value: aspose.pdf.Rectangle):
        ...
    
    ...

class PdfFormFlattenFieldsOptions(aspose.pdf.plugins.PdfFormOptions):
    '''Represents options for flatten all Fields (not annotations) on specified pages of document by PdfForm plugin.'''
    
    @overload
    def __init__(self, page_number: int):
        '''Initializes a new instance of the :class:`PdfFormFlattenFieldsOptions` object by page number,
        on which ALL fields will be flatten.
        
        :param page_number: Page number on which fields should be flattened.'''
        ...
    
    @overload
    def __init__(self, page_from: int, page_to: int):
        '''Initializes a new instance of the :class:`PdfFormFlattenFieldsOptions` object by page interval from pageFrom to pageTo (inclusive for both),
        on which ALL fields will be flatten.
        
        :param page_from: Page number, starting from which the fields will be flattened on the pages.
        :param page_to: Page number up to which the fields will be flattened on the pages. The fields on the page with number pageTo will also be flattened.'''
        ...
    
    ...

class PdfFormOptions:
    '''Represents options for PdfForm plugin.'''
    
    def add_data_source(self, data_source: aspose.pdf.plugins.IDataSource) -> None:
        '''Adds new data source to the PdfForm plugin data collection.
        
        :param data_source: Data source to add.'''
        ...
    
    def add_save_data_source(self, save_data_source: aspose.pdf.plugins.IDataSource) -> None:
        '''Adds new data source to the PdfForm plugin data collection.
        
        :param save_data_source: Data source (file or stream) for saving operation results.
        :raises System.NotImplementedException:'''
        ...
    
    @property
    def data_collection(self) -> None:
        '''Returns FormOptions plugin data collection.'''
        ...
    
    @property
    def save_targets_collection(self) -> None:
        '''Gets collection of added targets for saving operation results.'''
        ...
    
    ...

class PdfFormRemoveFieldsOptions(aspose.pdf.plugins.PdfFormOptions):
    '''Represents options for remove all Fields from specified pages of document by PdfForm plugin.'''
    
    @overload
    def __init__(self, page_number: int):
        '''Initializes a new instance of the :class:`PdfFormRemoveFieldsOptions` object by page number,
        on which ALL fields will be removed.
        
        :param page_number: Page number on which fields should be removed.'''
        ...
    
    @overload
    def __init__(self, page_from: int, page_to: int):
        '''Initializes a new instance of the :class:`PdfFormRemoveFieldsOptions` object by page interval from pageFrom to pageTo (inclusive for both),
        on which ALL fields will be removed.
        
        :param page_from: Page number, starting from which the fields will be deleted on the pages.
        :param page_to: Page number up to which the fields will be deleted on the pages. The fields on the page with number pageTo will also be removed.'''
        ...
    
    ...

class PdfFormSetFieldOptions(aspose.pdf.plugins.PdfFormOptions):
    '''Represents options for set fields (not annotations) properties.'''
    
    @property
    def get_setted_options(self) -> aspose.pdf.plugins.PdfFormFieldSetOptions:
        '''Gets PdfFormFieldSetOptions object that specifying options (properties) for set to field(s).'''
        ...
    
    ...

class PdfFormTextBoxFieldSetOptions(aspose.pdf.plugins.PdfFormFieldSetOptions):
    '''Represents options for set properties in TextBoxField.'''
    
    def __init__(self):
        ...
    
    @property
    def multiline(self) -> bool:
        ...
    
    @multiline.setter
    def multiline(self, value: bool):
        ...
    
    @property
    def spell_check(self) -> bool:
        ...
    
    @spell_check.setter
    def spell_check(self, value: bool):
        ...
    
    @property
    def force_combs(self) -> bool:
        ...
    
    @force_combs.setter
    def force_combs(self, value: bool):
        ...
    
    @property
    def max_len(self) -> int:
        ...
    
    @max_len.setter
    def max_len(self, value: int):
        ...
    
    ...

class PdfGenerator:
    '''Represents PdfGenerator plugin.'''
    
    def __init__(self):
        ...
    
    def process(self, options: aspose.pdf.plugins.IPluginOptions) -> aspose.pdf.plugins.ResultContainer:
        '''Starts the PdfGenerator processing with the specified parameters.
        
        :param options: An options object containg instructions for the PdfGenerator.
        :returns: An ResultContainer object containg the result of the operation.
        
        :raises System.NotSupportedException:'''
        ...
    
    ...

class PdfGeneratorOptions:
    '''Represents options for :class:`PdfGenerator` plugin.'''
    
    def add_data_source(self, data_source: aspose.pdf.plugins.IDataSource) -> None:
        '''Adds new data source to the PdfGenerator plugin data collection.
        
        :param data_source: Data source to add.'''
        ...
    
    def add_save_data_source(self, save_data_source: aspose.pdf.plugins.IDataSource) -> None:
        '''Adds new data source to the PdfGenerator plugin data collection.
        
        :param save_data_source: Data source (file or stream) for saving operation results.'''
        ...
    
    @property
    def data_collection(self) -> None:
        '''Returns PdfGenerator plugin data collection.'''
        ...
    
    @property
    def save_targets_collection(self) -> None:
        '''Gets collection of added targets for saving operation results.'''
        ...
    
    ...

class PdfGeneratorTOCOptions(aspose.pdf.plugins.PdfGeneratorOptions):
    '''Represents options for add table of contents to document by :class:`PdfGenerator` plugin.'''
    
    def __init__(self):
        ...
    
    ...

class PdfGeneratorTableOptions(aspose.pdf.plugins.PdfGeneratorOptions):
    '''Represents options for add datatable to document by :class:`PdfGenerator` plugin.'''
    
    def __init__(self):
        ...
    
    def set_page(self, page: int) -> aspose.pdf.plugins.PdfGeneratorTableOptions:
        '''Set the page number to place the table.
        
        :param page: Page number to insert table.
        :returns: Instance of current :class:`PdfGeneratorTableOptions`.'''
        ...
    
    def add_table(self) -> aspose.pdf.plugins.generator.PdfGeneratorTableBuilder:
        '''Adding table to document.
        
        :returns: New instance of :class:`aspose.pdf.plugins.generator.PdfGeneratorTableBuilder`.'''
        ...
    
    @staticmethod
    def create(self) -> aspose.pdf.plugins.PdfGeneratorTableOptions:
        '''Create instance of :class:`PdfGeneratorTableOptions`.
        
        :returns: New instance of :class:`PdfGeneratorTableOptions`.'''
        ...
    
    ...

class PdfImage:
    '''Represents PdfImage plugin.
    
    The :class:`PdfImage` class is used to convert PDF document to images (Jpeg).'''
    
    def __init__(self):
        ...
    
    def process(self, pdf_image_options: aspose.pdf.plugins.IPluginOptions) -> aspose.pdf.plugins.ResultContainer:
        '''Starts PdfImage processing with the specified parameters.
        
        :param pdf_image_options: An options object containing instructions for the PdfImage.
        :returns: A ResultContainer object containing the result of the conversion.'''
        ...
    
    ...

class PdfImageOptions:
    '''Represents options for the PdfImage plugin.
    
    The PdfImageOptions class contains base functions to add data (files, streams) representing input PDF documents.
    Please create :class:`PdfImageToJpegOptions` or another inherited PdfImage option class instead of this.'''
    
    def add_data_source(self, data_source: aspose.pdf.plugins.IDataSource) -> None:
        '''Adds new data source to the PdfImage plugin data collection.
        
        :param data_source: Data source to add.'''
        ...
    
    @property
    def data_collection(self) -> None:
        '''Returns PdfImage plugin data collection.'''
        ...
    
    @property
    def operation_name(self) -> str:
        '''Returns operation name.'''
        ...
    
    ...

class PdfImageToJpegOptions(aspose.pdf.plugins.PdfImageOptions):
    '''Represents Pdf to Jpeg convertor options for the PdfImage plugin.'''
    
    def __init__(self):
        ...
    
    @property
    def operation_name(self) -> str:
        '''Returns name of the operation.'''
        ...
    
    @property
    def conversion_mode(self) -> None:
        '''Gets image conversion mode.'''
        ...
    
    @property
    def page_list(self) -> str:
        '''Gets or sets a list of pages for the process.'''
        ...
    
    @page_list.setter
    def page_list(self, value: str):
        ...
    
    @property
    def output_resolution(self) -> int:
        '''Gets or sets the resolution value of the resulting images.'''
        ...
    
    @output_resolution.setter
    def output_resolution(self, value: int):
        ...
    
    ...

class PdfOrganizer:
    '''Represents PdfOrganizer plugin.'''
    
    def __init__(self):
        ...
    
    def process(self, options: aspose.pdf.plugins.IPluginOptions) -> aspose.pdf.plugins.ResultContainer:
        '''Starts the PdfOrganizer processing with the specified parameters.
        
        :param options: An options object containg instructions for the PdfOrganizer.
        :returns: An ResultContainer object containg the result of the operation.
        
        :raises System.NotSupportedException:'''
        ...
    
    ...

class PdfOrganizerCompressOptions(aspose.pdf.plugins.PdfOrganizerOptions):
    '''Represents Compress options for :class:`PdfOrganizer` plugin.'''
    
    def __init__(self):
        ...
    
    ...

class PdfOrganizerMergeOptions(aspose.pdf.plugins.PdfOrganizerOptions):
    '''Represents Merge options for :class:`PdfOrganizer` plugin.'''
    
    def __init__(self):
        ...
    
    ...

class PdfOrganizerOptions:
    '''Represents options for :class:`PdfOrganizer` plugin.'''
    
    def add_data_source(self, data_source: aspose.pdf.plugins.IDataSource) -> None:
        '''Adds new data source to the PdfOrganizer plugin data collection.
        
        :param data_source: Data source to add.'''
        ...
    
    def add_save_data_source(self, save_data_source: aspose.pdf.plugins.IDataSource) -> None:
        '''Adds new data source to the PdfOrganizer plugin data collection.
        
        :param save_data_source: Data source (file or stream) for saving operation results.
        :raises System.NotImplementedException:'''
        ...
    
    @property
    def data_collection(self) -> None:
        '''Returns OrganizerOptions plugin data collection.'''
        ...
    
    @property
    def save_targets_collection(self) -> None:
        '''Gets collection of added targets for saving operation results.'''
        ...
    
    @property
    def close_input_streams(self) -> bool:
        '''Close input streams after operation completed.'''
        ...
    
    @close_input_streams.setter
    def close_input_streams(self, value: bool):
        ...
    
    @property
    def close_output_streams(self) -> bool:
        '''Close output streams after operation completed.'''
        ...
    
    @close_output_streams.setter
    def close_output_streams(self, value: bool):
        ...
    
    ...

class PdfOrganizerResizeOptions(aspose.pdf.plugins.PdfOrganizerOptions):
    '''Represents Resize options for :class:`PdfOrganizer` plugin.'''
    
    def __init__(self):
        ...
    
    @property
    def page_size(self) -> aspose.pdf.PageSize:
        '''Gets or sets new page size.'''
        ...
    
    @page_size.setter
    def page_size(self, value: aspose.pdf.PageSize):
        ...
    
    ...

class PdfOrganizerRotateOptions(aspose.pdf.plugins.PdfOrganizerOptions):
    '''Represents Rotate options for :class:`PdfOrganizer` plugin.'''
    
    def __init__(self):
        ...
    
    @property
    def rotation(self) -> aspose.pdf.Rotation:
        '''Gets or sets new pages rotation.'''
        ...
    
    @rotation.setter
    def rotation(self, value: aspose.pdf.Rotation):
        ...
    
    ...

class PdfOrganizerSplitOptions(aspose.pdf.plugins.PdfOrganizerOptions):
    '''Represents Split options for :class:`PdfOrganizer` plugin.'''
    
    def __init__(self):
        ...
    
    ...

class ResultContainer:
    '''Represents container that contains the result collection of processing the plugin.'''
    
    @property
    def result_collection(self) -> None:
        '''Gets collection of the operation results'''
        ...
    
    ...

class StreamDataSource:
    '''Represents stream data source for load and save operations of a plugin.'''
    
    def __init__(self, data: Any):
        '''Initializes new stream data source with the specified stream object.
        
        :param data: Stream object'''
        ...
    
    @property
    def data_type(self) -> None:
        '''Type of data source (stream).'''
        ...
    
    @property
    def data(self) -> Any:
        '''Gets the stream object of the current data source.'''
        ...
    
    ...

class StreamResult:
    '''Represents operation result in the form of Stream.'''
    
    def to_file(self) -> str:
        '''Tries to convert the result to a file.
        
        :returns: A string representing the path to the output file if the result is file; otherwise ``None``.'''
        ...
    
    def to_stream(self) -> Any:
        '''Tries to convert the result to a stream object.
        
        :returns: A stream object representing the output data if the result is stream; otherwise ``None``.'''
        ...
    
    @property
    def is_file(self) -> bool:
        '''Indicates whether the result is a path to an output file.
        
        :returns: ``True`` if the result is a file; otherwise ``False``.'''
        ...
    
    @property
    def is_stream(self) -> bool:
        '''Indicates whether the result is a path to an output file.
        
        :returns: ``True`` if the result is a stream object; otherwise ``False``.'''
        ...
    
    @property
    def is_string(self) -> bool:
        '''Indicates whether the result is a string.
        
        :returns: ``True`` if the result is a string; otherwise ``False``.'''
        ...
    
    @property
    def data(self) -> object:
        '''Gets raw data.
        
        :returns: An ``object`` representing output data.'''
        ...
    
    ...

class StringResult:
    '''Represents operation result in the form of string.'''
    
    def to_file(self) -> str:
        '''Tries to convert the result to a file.
        
        :returns: A string representing the path to the output file if the result is file; otherwise ``None``.'''
        ...
    
    def to_stream(self) -> Any:
        '''Tries to convert the result to a stream object.
        
        :returns: A stream object representing the output data if the result is stream; otherwise ``None``.'''
        ...
    
    @property
    def is_file(self) -> bool:
        '''Indicates whether the result is a path to an output file.
        
        :returns: ``True`` if the result is a file; otherwise ``False``.'''
        ...
    
    @property
    def is_stream(self) -> bool:
        '''Indicates whether the result is a path to an output file.
        
        :returns: ``True`` if the result is a stream object; otherwise ``False``.'''
        ...
    
    @property
    def is_string(self) -> bool:
        '''Indicates whether the result is a string.
        
        :returns: ``True`` if the result is a string; otherwise ``False``.'''
        ...
    
    @property
    def data(self) -> object:
        '''Gets raw data.
        
        :returns: An ``object`` representing output data.'''
        ...
    
    @property
    def text(self) -> str:
        '''Returns string representation of the result.'''
        ...
    
    ...

class TextBoxFieldCreateOptions(aspose.pdf.plugins.FieldCreateOptions):
    '''Represents options for creating TextBoxField.'''
    
    def __init__(self, page_num: int, rect: aspose.pdf.Rectangle):
        '''Initializes a new instance of the :class:`TextBoxFieldCreateOptions` object, that containing parameters for created and added TextBoxField.
        
        :param page_num: Page number on which the added TextBoxField will be located.
        :param rect: Sets TextBoxField rectangle.'''
        ...
    
    @property
    def multiline(self) -> bool:
        '''Gets/sets the value to determine whether created TextBoxField is multiline or not (if will be set).'''
        ...
    
    @multiline.setter
    def multiline(self, value: bool):
        ...
    
    @property
    def spell_check(self) -> bool:
        '''Gets/sets the value to determine whether created TextBoxField is spellcheck or not (if will be set).'''
        ...
    
    @spell_check.setter
    def spell_check(self, value: bool):
        ...
    
    @property
    def force_combs(self) -> bool:
        '''Gets/sets the value to determine whether created TextBoxField is forcecombs or not (if will be set).'''
        ...
    
    @force_combs.setter
    def force_combs(self, value: bool):
        ...
    
    @property
    def max_len(self) -> int:
        '''Gets/sets the value to determine property MaxLen for created TextBoxField (if will be set).'''
        ...
    
    @max_len.setter
    def max_len(self, value: int):
        ...
    
    ...

class DataType:
    '''Represents possible types of data for plugin processing.'''
    
    FILE: DataType
    STREAM: DataType


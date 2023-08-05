import aspose.pdf
import aspose.pydrawing
import datetime
import decimal
import io
import uuid
from typing import Iterable

class SubPath:
    '''Represents vector graphics object on the page.
    Basically, vector graphics objects are represented by two groups of SubPaths.
    One of them is represented by a set of lines and curves.
    Others are presented as rectangles and can sometimes be confused.
    Usually it is a rectangular area that has a color, but very often this rectangle
    is placed at the beginning of the page and defines the entire space of the page in white.
    So you get the SubPath, but visually you only see the text on the page.'''
    
    @property
    def sub_path_operators(self) -> None:
        '''Gets operator collection that represents SubPath.'''
        ...
    
    @property
    def position(self) -> aspose.pdf.Point:
        '''Gets or sets the position of the SubPaths in :class:`aspose.pdf.Point`.'''
        ...
    
    @position.setter
    def position(self, value: aspose.pdf.Point):
        ...
    
    @property
    def rectangle(self) -> aspose.pdf.Rectangle:
        '''Gets the bounding rectangle of the SubPath.'''
        ...
    
    ...

class SubPathCollection:
    '''Represents SubPaths collection.'''
    
    def __getitem__(self, index: int) -> aspose.pdf.vector.SubPath:
        '''Gets the SubPath element at the specified index.
        
        :param index: Index within the collection.
        :returns: SubPath object.'''
        ...
    
    ...

class VectorGraphicsAbsorber:
    '''Represents an absorber object of vector graphics elements.
    Performs vector graphics search and provides access to search results via :attr:`VectorGraphicsAbsorber.sub_paths` collection.'''
    
    def __init__(self):
        ...
    
    def visit(self, page: aspose.pdf.Page) -> None:
        '''Performs search on the specified page.
        
        :param page: PDF document page object.'''
        ...
    
    @property
    def sub_paths(self) -> aspose.pdf.vector.SubPathCollection:
        '''Gets collection of search occurrences that are presented with :class:`SubPath` objects.'''
        ...
    
    ...


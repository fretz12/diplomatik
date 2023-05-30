from enum import Enum

from pydantic import BaseModel


class SourceExtractionType(Enum):
    """
    The type of source extraction
    """
    select = 'select'
    aggregate = 'aggregate'


class SourceExtraction(BaseModel):
    """
    Data model defining how data should be extracted from a source
    """
    extraction_type: SourceExtractionType
    """The type of source extraction"""

from typing import Annotated

from pydantic import Field

from diplomatik.data_model.source_extraction.aggregation_extraction import AggregationExtraction
from diplomatik.data_model.source_extraction.select_extraction import SelectExtraction


SourceExtractionUnion = Annotated[AggregationExtraction | SelectExtraction, Field(discriminator='extraction_type')]
"""The declared datatype that is used in Pydantic models so it knows how to (de)serialize abstract Field types"""

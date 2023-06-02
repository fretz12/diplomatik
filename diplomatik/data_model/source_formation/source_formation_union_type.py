from typing import Annotated

from pydantic import Field

from diplomatik.data_model.source_formation.join_formation import JoinFormation
from diplomatik.data_model.source_formation.single_table_formation import SingleTableFormation

SourceFormationUnion = Annotated[SingleTableFormation | JoinFormation, Field(discriminator='formation_type')]
"""The declared datatype that is used in Pydantic models so it knows how to (de)serialize abstract Field types"""

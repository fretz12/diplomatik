from typing import Annotated

from pydantic import Field

from diplomatik.data_model.filter.bound_filter import BoundFilter
from diplomatik.data_model.filter.equals_filter import EqualsFilter
from diplomatik.data_model.filter.in_filter import InFilter
from diplomatik.data_model.filter.in_subselect_filter import InSubSelectFilter
from diplomatik.data_model.filter.like_filter import LikeFilter
from diplomatik.data_model.filter.null_check_filter import NullCheckFilter

FilterUnion = Annotated[EqualsFilter |
                        NullCheckFilter |
                        LikeFilter |
                        InFilter |
                        InSubSelectFilter |
                        BoundFilter, Field(discriminator='filter_type')]
"""
The declared datatype that is used in Pydantic models so it knows how to (de)serialize abstract Filter types. 
This excludes nesting filters like AND/OR because they need to be handled for self-referencing circular import 
issues.
"""

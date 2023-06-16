from typing import Annotated

from fastapi import Body

from diplomatik.data_model.query.aggregate_query import AggregateQuery
from diplomatik.data_model.query.batch_query import BatchQuery
from diplomatik.data_model.query.data_source_management_query import DataSourceManagementQuery
from diplomatik.data_model.query.delete_query import DeleteQuery
from diplomatik.data_model.query.insert_query import InsertQuery
from diplomatik.data_model.query.search_query import SearchQuery
from diplomatik.data_model.query.template_query import TemplateQuery
from diplomatik.data_model.query.union_query import UnionQuery
from diplomatik.data_model.query.update_query import UpdateQuery


QueryUnionBody = Annotated[AggregateQuery |
                           BatchQuery |
                           DataSourceManagementQuery |
                           DeleteQuery |
                           InsertQuery |
                           SearchQuery |
                           TemplateQuery |
                           UnionQuery |
                           UpdateQuery, Body(discriminator='query_type')]
"""The declared datatype that is used in Pydantic models so it knows how to (de)serialize abstract Query types"""

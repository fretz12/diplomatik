import json

import pytest
from jinja2 import Environment, PackageLoader

from diplomatik.data_model.query.data_source_management_query import DataSourceManagementQuery
from diplomatik.data_model.query.search_query import SearchQuery

query_template_env = Environment(
    loader=PackageLoader('diplomatik.tests', './test_data_engine/templates/'))


@pytest.fixture
def search_query_fixture():
    def __load_query(template_name: str, args: dict):
        template = query_template_env.get_template(template_name)

        query = json.loads(template.render(args))

        return SearchQuery.parse_obj(query)

    return __load_query


@pytest.fixture
def management_query_fixture():
    def __load_query(template_name: str, args: dict):
        template = query_template_env.get_template(template_name)

        query = json.loads(template.render(args))

        return DataSourceManagementQuery.parse_obj(query)

    return __load_query

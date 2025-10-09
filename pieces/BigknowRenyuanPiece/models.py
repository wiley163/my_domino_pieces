from pydantic import BaseModel, Field
from enum import Enum


class MethodTypes(str, Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class InputModel(BaseModel):
    url: str = Field(
        default="http://192.168.10.174:9520/api/renyuan",
        description="URL to make a request to."
    )
    method: MethodTypes = Field(
        default=MethodTypes.POST,
        description="HTTP method to use."
    )
    bearer_token: str = Field(
        default="123456",
        description="Bearer token to use for authentication."
    )
    ry_data: str = Field(
        default="",
        json_schema_extra={
            "from_upstream": "always"
        }
    )


class OutputModel(BaseModel):
    result: str = Field(
        description='Output data string.'
    )

from pydantic import BaseModel, Field
from typing import Union
from datetime import date as dt_date, datetime as dt_datetime, time as dt_time


class InputModel(BaseModel):
    """
    ToStringPiece Input Model
    """
    input_value: str = Field(
        description='Input value to be turned into string.',
        default="{{ dag_run.conf.get('user_id', 'default_user_if_not_found') }}"
    )


class OutputModel(BaseModel):
    """
    ToStringPiece Output Model
    """
    output_value: str = Field(
        description='Input value as a string.'
    )

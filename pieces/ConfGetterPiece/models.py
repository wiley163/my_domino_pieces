from pydantic import BaseModel, Field
from typing import List, Dict, Any

class InputModel(BaseModel):
    keys: List[str] = Field(
        description="需要提取的 dag_run.conf 中的 key 列表",
        example=["region", "bucket", "start_date", "end_date"]
    )

class OutputModel(BaseModel):
    conf_dict: Dict[str, Any] = Field(
        description="按 key 提取后的 conf 值字典"
    )
from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from airflow.models import TaskInstance
from typing import Dict, Any

class ConfGetterPiece(BasePiece):
    def piece_function(self, input_data: InputModel) -> OutputModel:
        ti: TaskInstance = self.context["ti"]
        conf: Dict[str, Any] = ti.dag_run.conf or {}
        extracted = {k: conf.get(k) for k in input_data.keys}
        self.logger.info("提取 conf 成功: %s", extracted)
        return OutputModel(conf_dict=extracted)
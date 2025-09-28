from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from typing import Dict, Any

class ConfGetterPiece(BasePiece):
    def piece_function(self, input_data: InputModel):
        # ti: TaskInstance = self.context["ti"]
        # conf: Dict[str, Any] = ti.dag_run.conf or {}
        # extracted = {k: conf.get(k) for k in input_data.keys}
        # self.logger.info("提取 conf 成功: %s", extracted)
        # return OutputModel(conf_dict=extracted)
        # Log inputs
        self.logger.info(f"""
        self.context:\n{self.context}\n
        """)
        self.logger.info(f"""
        Input Output args:\n{input_data.output_args}\n
        """)
        
        output_args: Dict[str, Any] = {"output_1":"para111111", "output_2":"para222222"}

        # Log output
        self.logger.info(output_args)

        # Return output
        return OutputModel(**output_args)
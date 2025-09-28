from domino.base_piece import BasePiece
from .models import InputModel, OutputModel
from typing import Dict, Any
import os, json

class ConfGetterPiece(BasePiece):
    def piece_function(self, input_data: InputModel, **kwargs):
        # ti: TaskInstance = self.context["ti"]
        # conf: Dict[str, Any] = ti.dag_run.conf or {}
        # extracted = {k: conf.get(k) for k in input_data.keys}
        # self.logger.info("提取 conf 成功: %s", extracted)
        # return OutputModel(conf_dict=extracted)
        # Log inputs
        try:
            self.logger.info(f"self.__dict__: {self.__dict__}")
        except Exception as e:
            self.logger.error(f"无法打印 self.__dict__: {e}")
        self.logger.info(f"""
        kwargs===>:\n{kwargs}\n
        """)
        # 1. 从kwargs中安全地获取dag_run对象
        dag_run = kwargs.get('dag_run')
        
        # 2. 从dag_run对象中获取conf字典
        # 最好进行一次检查，以防dag_run不存在（虽然在正常运行中它总是存在）
        dag_run_conf = {}
        if dag_run:
            dag_run_conf = dag_run.conf or {} # 如果conf为None，则使用空字典
            
        dag_run_conf = json.loads(os.getenv("AIRFLOW_DAG_RUN_CONF", "{}"))

            
        self.logger.info(f"""
        dag_run_conf2===>:\n{dag_run_conf}\n
        """)
        self.logger.info(f"""
        Input Output args:\n{input_data.output_args}\n
        """)
        extracted = {k.name: dag_run_conf.get(k.name) for k in input_data.output_args}
        output_args: Dict[str, Any] = extracted

        # Log output
        self.logger.info(output_args)

        # Return output
        return OutputModel(**output_args)
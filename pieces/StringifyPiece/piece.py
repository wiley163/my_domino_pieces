from domino.base_piece import BasePiece
from .models import InputModel, OutputModel


class StringifyPiece(BasePiece):

    def piece_function(self, input_data: InputModel):

        string_value = str(input_data.input_value)
        self.logger.info(f"Input23 value as string: {string_value}")

        # Return output
        return OutputModel(
            output_value=string_value,
        )

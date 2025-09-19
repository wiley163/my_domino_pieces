import pytest
from pieces.ConfGetterPiece.piece import ConfGetterPiece
from pieces.ConfGetterPiece.models import InputModel, OutputModel

def test_piece(mocker):
    # 伪造 context
    mock_ti = mocker.MagicMock()
    mock_ti.dag_run.conf = {"region": "us-east-1", "bucket": "my-bucket"}
    piece = ConfGetterPiece(context={"ti": mock_ti})
    inp = InputModel(keys=["region", "bucket"])
    out = piece.piece_function(inp)
    assert out.conf_dict == {"region": "us-east-1", "bucket": "my-bucket"}
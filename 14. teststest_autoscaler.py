import pandas as pd
from src.cloudops.autoscaler import aplicar_autoscaling

def test_autoscaling(capsys):
    df = pd.DataFrame({
        "instancia_id": ["vm-1"],
        "cpu_uso": [91],
        "mem_uso": [85],
        "storage_uso": [50]
    })
    aplicar_autoscaling(df)
    captured = capsys.readouterr()
    assert "Escalando CPU" in captured.out

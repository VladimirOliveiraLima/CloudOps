import pandas as pd
from src.cloudops.monitor import verificar_metricas

def test_alertas():
    df = pd.DataFrame({
        "instancia_id": ["vm-1"],
        "cpu_uso": [90],
        "mem_uso": [82],
        "storage_uso": [70]
    })
    alertas = verificar_metricas(df)
    assert len(alertas) == 3

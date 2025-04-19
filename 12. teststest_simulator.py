from src.cloudops.simulator import gerar_metricas

def test_gerar_metricas():
    df = gerar_metricas(3)
    assert len(df) == 3
    assert "cpu_uso" in df.columns

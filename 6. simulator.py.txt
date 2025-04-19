import pandas as pd
import random

def gerar_metricas(instancias=5):
    data = []
    for i in range(instancias):
        data.append({
            "instancia_id": f"vm-{i+1}",
            "cpu_uso": random.uniform(20, 95),
            "mem_uso": random.uniform(30, 90),
            "storage_uso": random.uniform(10, 70)
        })
    return pd.DataFrame(data)

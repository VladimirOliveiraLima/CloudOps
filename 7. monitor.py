def verificar_metricas(df):
    alertas = []
    for _, row in df.iterrows():
        if row["cpu_uso"] > 85:
            alertas.append(f"[ALERTA] Alta CPU - {row['instancia_id']} ({row['cpu_uso']:.2f}%)")
        if row["mem_uso"] > 80:
            alertas.append(f"[ALERTA] Alta Memória - {row['instancia_id']} ({row['mem_uso']:.2f}%)")
        if row["storage_uso"] > 65:
            alertas.append(f"[ALERTA] Storage Quase Cheio - {row['instancia_id']} ({row['storage_uso']:.2f}%)")
    return alertas

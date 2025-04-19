def aplicar_autoscaling(df):
    for _, row in df.iterrows():
        if row["cpu_uso"] > 85:
            print(f"[AUTO-SCALING] Escalando CPU para {row['instancia_id']}")
        if row["mem_uso"] > 80:
            print(f"[AUTO-SCALING] Adicionando memória à {row['instancia_id']}")

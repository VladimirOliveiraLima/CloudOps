from src.cloudops.simulator import gerar_metricas
from src.cloudops.monitor import verificar_metricas
from src.cloudops.autoscaler import aplicar_autoscaling
from src.cloudops.visualizer import plotar_metricas

def main():
    print("Iniciando CloudOps Monitoring...")

    df = gerar_metricas(instancias=10)
    df.to_csv("data/metrics.csv", index=False)

    alertas = verificar_metricas(df)
    aplicar_autoscaling(df)

    with open("data/alerts.log", "w") as f:
        for alerta in alertas:
            f.write(alerta + "\n")

    plotar_metricas(df)

if __name__ == "__main__":
    main()

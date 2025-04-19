import matplotlib.pyplot as plt
import seaborn as sns

def plotar_metricas(df):
    df = df.sort_values("instancia_id")
    plt.figure(figsize=(12, 6))
    sns.barplot(x="instancia_id", y="cpu_uso", data=df, label="CPU")
    plt.title("Uso de CPU por Instância")
    plt.xlabel("Instância")
    plt.ylabel("CPU (%)")
    plt.tight_layout()
    plt.show()

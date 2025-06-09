import pandas as pd
import matplotlib.pyplot as plt
import os

# Garante que o diretório existe
os.makedirs("docs", exist_ok=True)

df = pd.read_csv("leituras_siap.csv")

plt.figure(figsize=(10, 5))
plt.plot(df["temperatura"], label="Temperatura (°C)")
plt.plot(df["umidade"], label="Umidade (%)")
plt.plot(df["vibracao"], label="Vibração (ADC)")
plt.legend()
plt.title("Leituras simuladas dos sensores - SIAP")
plt.xlabel("Leitura")
plt.ylabel("Valor")
plt.grid()
plt.tight_layout()

# Agora funciona:
plt.savefig("docs/grafico_leituras.png")
plt.show()

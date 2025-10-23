import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ============================================
# Top 10 jogos mais jogados (exemplo de dados)
# ============================================

jogos = [
    "Minecraft", "Fortnite", "Roblox", "League of Legends", "CS:GO",
    "GTA V", "PUBG", "Apex Legends", "Among Us", "Call of Duty"
]

# Tempo total jogado (em milhões de horas)
horas_jogadas = [420, 360, 300, 280, 240, 220, 200, 180, 150, 140]

# Criar DataFrame
df = pd.DataFrame({
    "Jogo": jogos,
    "Horas Jogadas (milhões)": horas_jogadas
}).sort_values("Horas Jogadas (milhões)", ascending=True)

# ============================================
# Criar o gráfico
# ============================================

plt.figure(figsize=(10, 6))
plt.barh(df["Jogo"], df["Horas Jogadas (milhões)"])
plt.title("Top 10 Jogos Mais Jogados do Mundo", fontsize=14, weight='bold')
plt.xlabel("Horas Jogadas (milhões)")
plt.ylabel("Jogo")

# Adicionar valores no final das barras
for i, v in enumerate(df["Horas Jogadas (milhões)"]):
    plt.text(v + 5, i, f"{v}", va='center')

plt.tight_layout()
plt.show()

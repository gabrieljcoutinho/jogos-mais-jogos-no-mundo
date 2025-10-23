import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Dados atualizados
jogos = [
    "Roblox", "Free Fire", "Counter-Strike 2", "Fortnite", "League of Legends",
    "Minecraft", "PUBG Mobile", "Valorant", "Apex Legends", "Call of Duty"
]

# Jogadores ativos mensais (em milhões) — substituir None por estimativas
jogadores_ativos = [111.8, 100, 0.935, 44.7, 115, 350, 85, 15, 20, 30]

# Criar DataFrame
df = pd.DataFrame({
    "Jogo": jogos,
    "Jogadores Ativos (milhões)": jogadores_ativos
}).sort_values("Jogadores Ativos (milhões)", ascending=True)

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.barh(df["Jogo"], df["Jogadores Ativos (milhões)"], color=plt.cm.Paired(np.linspace(0, 1, len(df))))
plt.title("Top 10 Jogos Mais Jogados do Mundo em 2025", fontsize=14, weight='bold')
plt.xlabel("Jogadores Ativos (milhões)")
plt.ylabel("Jogo")

# Adicionar valores no final das barras
for i, v in enumerate(df["Jogadores Ativos (milhões)"]):
    plt.text(v + 2, i, f"{v:.1f}M", va='center')

plt.tight_layout()
plt.show()

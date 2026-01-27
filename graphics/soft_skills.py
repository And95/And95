import matplotlib.pyplot as plt

soft_skills = {
    "Resolução de problemas": 90,
    "Comunicação": 85,
    "Trabalho em equipe": 88,
    "Pensamento crítico": 86,
    "Aprendizado contínuo": 94
}

plt.figure(figsize=(6, 4))
plt.barh(list(soft_skills.keys()), list(soft_skills.values()))
plt.xlim(0, 100)
plt.title("Soft Skills")
plt.xlabel("Nível (%)")
plt.tight_layout()

plt.savefig("assets/soft_skills.png", dpi=150)
plt.close()
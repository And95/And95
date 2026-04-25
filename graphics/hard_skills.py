import matplotlib.pyplot as plt

hard_skills = {
    "JavaScript": 90,
    "TypeScript": 82,
    "React": 86,
    "Node.js": 88,
    "SQL / PL-SQL (Oracle)": 94
}

plt.figure(figsize=(6, 4))
plt.barh(list(hard_skills.keys()), list(hard_skills.values()))
plt.xlim(0, 100)
plt.title("Hard Skills")
plt.xlabel("Nível (%)")
plt.tight_layout()

plt.savefig("assets/hard_skills.png", dpi=150)
plt.close()
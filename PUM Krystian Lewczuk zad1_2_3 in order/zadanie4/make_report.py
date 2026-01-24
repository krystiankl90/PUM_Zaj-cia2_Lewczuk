import json
from pathlib import Path


models_path = Path("../zadanie3/models")
screenshots_path = Path("../zadanie3/screenshots")
output_path = Path("report.md")


results = []
for file in models_path.glob("*.json"):
    with open(file, "r", encoding="utf-8") as f:
        metrics = json.load(f)
        results.append((file.stem, metrics))

results.sort(key=lambda x: x[1].get("f1", 0), reverse=True)


with open(output_path, "w", encoding="utf-8") as f:
    f.write("# Raport końcowy (zadanie 4)\n\n")
    f.write("## TOP modele:\n")
    for name, metryki in results:
        f.write(f"### {name}\n")
        for k, v in metryki.items():
            f.write(f"- **{k}**: {v}\n")
        f.write("\n")

    f.write("## Wykresy:\n")
    for img in screenshots_path.glob("*.png"):
        rel_path = img.relative_to(Path.cwd())
        f.write(f"### {img.stem}\n")
        f.write(f"![{img.stem}]({rel_path})\n\n")

print(f"✅ Wygenerowano raport: {output_path.resolve()}")

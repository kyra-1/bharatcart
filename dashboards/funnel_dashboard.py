# dashboards/funnel_dashboard.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 📥 Load CSV
df = pd.read_csv("pyspark_jobs/output/funnel_analysis/funnel_metrics.csv")

# 📊 Funnel Plot
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="event_type", y="count", palette="Blues_d")

plt.title("User Drop-off Funnel")
plt.xlabel("Funnel Stage")
plt.ylabel("Event Count")
plt.tight_layout()

# 💾 Save
os.makedirs("output/visuals", exist_ok=True)
plt.savefig("output/visuals/funnel_analysis.png")
plt.close()

print("✅ Funnel dashboard saved to output/visuals/funnel_analysis.png")

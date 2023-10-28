import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
orthogroups_data = pd.read_csv("Orthogroups.GeneCount_I4.4.tsv", sep="\t", index_col=0)
orthogroups_data.columns = [col.replace('_tr_cds_output', '') for col in orthogroups_data.columns]

# Create the heatmap using the logarithmic scale for color representation
plt.figure(figsize=(15, 10))
sns.heatmap(np.log2(orthogroups_data + 1), cmap="YlGnBu", cbar_kws={'label': 'Log2 Gene Count'}, xticklabels=True, yticklabels=False)
plt.title("Gene Counts for Orthogroups across Genomes (Log2 Scaled)", fontsize=16)
plt.ylabel("Orthogroups")
plt.xlabel("Genomes")
plt.tight_layout()
plt.savefig("orthogroups_heatmap_log2_scaled.png", dpi=300)
plt.show()


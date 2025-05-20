"""
analysis.py
Performs repeated measures ANOVA on participant ratings of 5 different voice conditions (V1–V5).
"""

# ----------------------------- #
# Import Libraries
# ----------------------------- #
import pandas as pd
from statsmodels.stats.anova import AnovaRM
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------- #
# Clean CSV Format (if needed)
# ----------------------------- #
"""
import csv
with open('mean_of_voices.csv', 'r') as file:
    content = file.read()
updated_content = content.replace(';', ',')
with open('mean_of_voices.csv', 'w') as file:
    file.write(updated_content)
"""

# ----------------------------- #
#  Load Data
# ----------------------------- #
data = pd.read_csv('mean_of_voices.csv')  #  columns: Participant, V1, V2, V3, V4, V5

# ----------------------------- #
#  Reshape Data for ANOVA
# ----------------------------- #
long_data = pd.melt(data, 
                    id_vars=['Participant'], 
                    value_vars=['V1', 'V2', 'V3', 'V4', 'V5'], 
                    var_name='Voice', 
                    value_name='Score')

# ----------------------------- #
#  Repeated Measures ANOVA
# ----------------------------- #
print("📈 Repeated Measures ANOVA Results:")
anova_model = AnovaRM(long_data, 'Score', 'Participant', within=['Voice']).fit()
print(anova_model.summary())

# ----------------------------- #
#  Boxplot Visualization
# ----------------------------- #
plt.figure(figsize=(8, 6))
sns.boxplot(x='Voice', y='Score', data=long_data)
plt.title('Voice Ratings by Condition (V1–V5)')
plt.xlabel('Voice Condition')
plt.ylabel('Rating Score')
plt.grid(True)
plt.tight_layout()
plt.show()

# import csv
# with open('mean_of_voices.csv', 'r') as file:
#     content = file.read()
# updated_content = content.replace(';', ',')
# with open('mean_of_voices.csv', 'w') as file:
#     file.write(updated_content)

# with open('mean_of_voices.csv', 'r') as file:
#     content = file.read()
# rows = content.split('\n')

import pandas as pd
from statsmodels.stats.anova import AnovaRM
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
data = pd.read_csv('mean_of_voices.csv')

# Melt the DataFrame to long format for repeated measures ANOVA
long_data = pd.melt(data, id_vars=['Participant'], 
                    value_vars=['V1', 'V2', 'V3', 'V4', 'V5'], var_name='Variable')

# Perform repeated measures ANOVA considering 'Variable'
model = AnovaRM(long_data, 'value', 'Participant', within=['Variable']).fit()

print("General ANOVA results:")
print(model.summary())

# Plot the data
plt.figure(figsize=(10, 6))
sns.boxplot(x='Variable', y='value', data=long_data)
plt.title('Value by Variable')
plt.show()

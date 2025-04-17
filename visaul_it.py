import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# Step 1: Connect to the database
engine = create_engine('sqlite:///medical_cabinet.db')  # Update with your database URL
query = "SELECT * FROM patients"
df = pd.read_sql(query, engine)

# Step 2: Preprocess the medical_history column
# Replace NULL or empty values with "None"
df['medical_history'] = df['medical_history'].fillna('None')
df['medical_history'] = df['medical_history'].replace('', 'None')

# Strip leading/trailing spaces
df['medical_history'] = df['medical_history'].str.strip()

# Step 3: Create a list of (patient_id, condition) pairs
condition_list = []
for _, row in df.iterrows():
    patient_id = row['patient_id']
    conditions = row['medical_history'].split(', ')
    for condition in conditions:
        condition = condition.strip()  # Remove extra spaces
        if condition:  # Ignore empty conditions
            condition_list.append((patient_id, condition))

# Convert to a DataFrame
condition_df = pd.DataFrame(condition_list, columns=['patient_id', 'condition'])

# Count unique patients per condition
unique_condition_counts = condition_df.groupby('condition')['patient_id'].nunique()

# Step 4: Visualize as a line chart
plt.figure(figsize=(12, 6))

# Set the window title
manager = plt.get_current_fig_manager()
manager.set_window_title("Visual_it")  # Corrected typo in "Visual_it"

sns.lineplot(x=unique_condition_counts.index, y=unique_condition_counts.values, marker='o', color='blue')
plt.title('Frequency of Medical Conditions (Unique Patients)', fontsize=16)
plt.xlabel('Medical Condition', fontsize=14)
plt.ylabel('Number of Unique Patients', fontsize=14)
plt.xticks(rotation=100, ha='right')  # Rotate x-axis labels for readability
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add gridlines for better readability
plt.show()
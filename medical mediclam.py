import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import xlabel, ylabel

# DATA FROM CSV FILE
df= pd.read_csv(r"C:\Users\bhara\Desktop\project on aiml\AKASH BHAR_AI-ML INTRENSHIP\project figure.csv")

# Display the dataframe
print("Medical Mediclaim Data:")
print(df)

#  # Visualization using matplotlib
plt.figure(figsize=(8, 5))
plt.bar(df['id'], df['claim_amount'], color='skyblue')
plt.title('Claim Amount by Patient')
plt.xlabel('Patient ID')
plt.ylabel('Claim Amount (INR)')
plt.grid(axis='y')
plt.tight_layout()
plt.show()
# claim  graph
claim_status_counts = df['status'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(claim_status_counts, labels=claim_status_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Claim Status Distribution')
plt.show()
#male female percentage
claim_status_counts = df['gender'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(claim_status_counts, labels=claim_status_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Gender variable chart')
plt.show()
#patient age and age graph
plt.figure(figsize=(10,5),edgecolor='orange')
plt.plot(df['id'],df['age'])
xlabel("patient id")
ylabel("age")
plt.grid(axis='y')
plt.title("patient id and age graph")
plt.legend()
plt.show()


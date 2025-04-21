import pandas as pd
df = pd.read_csv('C:\Users\Rishabh Singh\Desktop\Intership') 
print("Initial data shape:", df.shape)
print(df.head())
print("\nMissing values:\n", df.isnull().sum())
if 'Revenue' in df.columns:
    df['Revenue'].fillna(df['Revenue'].median(), inplace=True)
df.dropna(thresh=len(df.columns) - 2, inplace=True)
df.drop_duplicates(inplace=True)
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].str.lower().str.strip()
    df['Gender'].replace({'m': 'male', 'f': 'female'}, inplace=True)

if 'Country' in df.columns:
    df['Country'] = df['Country'].str.title().str.strip()
for col in df.columns:
    if 'date' in col.lower():
        df[col] = pd.to_datetime(df[col], errors='coerce')
df.columns = [col.lower().strip().replace(' ', '_') for col in df.columns]
if 'age' in df.columns:
    df['age'] = pd.to_numeric(df['age'], errors='coerce').astype('Int64')
print("\nCleaned data shape:", df.shape)
print(df.head())
df.to_csv('sales_data_cleaned.csv', index=False)
print("\nCleaned dataset saved as 'sales_data_cleaned.csv'")

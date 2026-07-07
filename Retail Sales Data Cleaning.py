import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("\n==========================================================")
print("RETAIL SALES DATA CLEANING PROJECT")
print("==========================================================")


'Step 1: Load Dataset'

data = pd.read_csv("Retail_Sales_Messy_1230_Rows.csv")


print("\n----------------------------------------------------------")
print("Step 2: Basic Data Inspection")
print("----------------------------------------------------------")

print("\nFirst 5 Rows")
print(data.head(), "\n")

print("\nLast 5 Rows")
print(data.tail(), "\n")

print("\nDataset Shape")
print(data.shape, "\n")

print("\nColumn Names")
print(data.columns, "\n")

print("\nData Types")
print(data.dtypes, "\n")

print("\nComplete Information")
print(data.info(), "\n")

print("\nStatistical Summary")
print(data.describe(), "\n")

print("\nMissing Values")
print(data.isnull().sum(), "\n")

print("\nDuplicate Records")
print(data.duplicated().sum(), "\n")

print("\nUnique Values")
print(data.nunique(), "\n")

print("\nRandom Sample")
print(data.sample(10), "\n")


print("\n----------------------------------------------------------")
print("Step 3: Remove Duplicate Records")
print("----------------------------------------------------------")

data = data.drop_duplicates()

print("Shape After Removing Duplicates:")
print(data.shape)


print("\n----------------------------------------------------------")
print("Step 4: Handle Missing Values - Age")
print("----------------------------------------------------------")

data["Age"] = data["Age"].fillna(data["Age"].median())

print(data["Age"].isnull().sum())


print("\n----------------------------------------------------------")
print("Step 5: Handle Missing Values - City")
print("----------------------------------------------------------")

print(data["City"].mode())

data["City"] = data["City"].fillna(data["City"].mode()[0])

print(data["City"].isnull().sum())


print("\n----------------------------------------------------------")
print("Step 6: Clean Price Column")
print("----------------------------------------------------------")

print(data["Price"].unique())

# Remove Extra Spaces
data["Price"] = data["Price"].astype(str).str.strip()

# Replace "unknown" with Missing Value
data["Price"] = data["Price"].replace("unknown", pd.NA)

# Convert to Numeric
data["Price"] = pd.to_numeric(data["Price"])

# Fill Missing Price with Median
data["Price"] = data["Price"].fillna(data["Price"].median())

print(data["Price"].dtype)
print(data["Price"].isnull().sum())


print("\n----------------------------------------------------------")
print("Step 7: Remove Invalid Quantity")
print("----------------------------------------------------------")

print((data["Quantity"] < 0).sum())

print(data[data["Quantity"] < 0])

data = data[data["Quantity"] > 0]

print((data["Quantity"] < 0).sum())

print(data.shape)


print("\n----------------------------------------------------------")
print("Step 8: Handle Missing Values - Discount")
print("----------------------------------------------------------")

print(data["Discount"].isnull().sum())

data["Discount"] = data["Discount"].fillna(0)

print(data["Discount"].isnull().sum())

print(data["Discount"].value_counts())


print("\n----------------------------------------------------------")
print("Step 9: Handle Missing Values - Rating")
print("----------------------------------------------------------")

print(data["Rating"].median())

data["Rating"] = data["Rating"].fillna(data["Rating"].median())

print(data["Rating"].isnull().sum())


print("\n----------------------------------------------------------")
print("Step 10: Convert Order Date to Datetime")
print("----------------------------------------------------------")

data["Order_Date"] = pd.to_datetime(
    data["Order_Date"],
    errors="coerce",
    dayfirst=True
)

print(data["Order_Date"].isnull().sum())
print(data[data["Order_Date"].isnull()])

data["Order_Date"] = pd.to_datetime(data["Order_Date"])

print(data["Order_Date"].dtype)


print("\n----------------------------------------------------------")
print("Step 11: Final Data Validation")
print("----------------------------------------------------------")

print(data.info())

print(data.isnull().sum())

print(data.describe())


print("\n----------------------------------------------------------")
print("Step 12: Save Clean Dataset")
print("----------------------------------------------------------")

data.to_csv("Retail_Sales_Cleaned.csv", index=False)

print("Data Cleaning Completed Successfully!")



print("\n\nStep : Insights Likhna\n")

print("Electronics generated the highest revenue.")
print("Furniture contributed the lowest sales.")
print("Fashion and Home categories performed consistently.")

print("Fashion category generated the highest revenue.")
print("Electronics was the second-best performing category.")
print("Home category contributed the lowest sales.")
print("Fashion and Electronics together account for a major share of total revenue.")

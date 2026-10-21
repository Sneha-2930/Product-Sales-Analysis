
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the Excel file
df = pd.read_excel("wellness_data.xlsx")

# Step 2: Display the data
print("First 5 rows:")
print(df.head())

print("Shape:", df.shape)
print("Columns:", df.columns.tolist())

# Step 3: Calculate total revenue
df["total"] = df["Quantity"] * df["Price"]

# Step 4: Display sales analysis
print("\nSales Calculation")
print("Total Quantity Sold:", df["Quantity"].sum())
print("Total Revenue:", df["total"].sum())
print("Highest Revenue:", df["total"].max())

highest_product = df.loc[df["total"].idxmax(), "Product"]
print("Best Selling Product:", highest_product)

print("\nComplete Data:")
print(df)

# Step 5: Create bar chart
plt.figure(figsize=(8, 5))
plt.bar(df["Product"], df["total"])
plt.title("Total Revenue by Product")
plt.xlabel("Products")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("revenue_chart.png")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv("books_dataset.csv")

# 2. Clean the Price column (remove currency symbols, keep only numbers)
df["Price"] = (
    df["Price"]
    .astype(str)                              # ensure string
    .str.extract(r"([\d\.]+)", expand=False)  # extract numbers & dots
    .astype(float)                             # convert to float
)

# -----------------------------
# 1️⃣ BAR CHART – Top 10 Expensive Books
# -----------------------------
plt.figure(figsize=(12, 6))
top10 = df.sort_values(by="Price", ascending=False).head(10)

sns.barplot(x="Price", y="Book Title", data=top10)
plt.title("Top 10 Most Expensive Books")
plt.xlabel("Price")
plt.ylabel("Book Title")
plt.tight_layout()
plt.savefig("top10_books.png")
plt.show()

# -----------------------------
# 2️⃣ HISTOGRAM – Price Distribution
# -----------------------------
plt.figure(figsize=(10, 5))
sns.histplot(df["Price"], bins=10, kde=True)
plt.title("Book Price Distribution")
plt.xlabel("Price")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

# -----------------------------
# 3️⃣ PIE CHART – Price Range Categories
# -----------------------------
df["Price Range"] = pd.cut(
    df["Price"],
    bins=[0, 20, 40, 60, 80, 100],
    labels=["0-20", "20-40", "40-60", "60-80", "80-100"]
)

plt.figure(figsize=(7, 7))
df["Price Range"].value_counts().plot.pie(autopct="%1.1f%%")
plt.title("Book Price Range Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("price_range_pie.png")
plt.show()

print("All charts created and saved successfully.")

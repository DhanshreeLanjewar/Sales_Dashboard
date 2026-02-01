# IMPORT REQUIRED LIBRARIES

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# LOAD DATASET
df = pd.read_csv(r"C:\Users\dhans\Downloads\sales_data (2).csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])


# GLOBAL STYLING (Professional Look)

sns.set_theme(style="whitegrid", palette="Set2")
plt.rcParams["figure.figsize"] = (10, 6)


# 1. LINE PLOT – SALES TREND

sns.lineplot(data=df, x="Date", y="Total_Sales")
plt.title("Sales Trend Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 2. BAR PLOT – PRODUCT PERFORMANCE
sns.barplot(data=df, x="Product", y="Total_Sales")
plt.title("Total Sales by Product")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# 3. BOX PLOT – SALES DISTRIBUTION
sns.boxplot(data=df, x="Region", y="Total_Sales")
plt.title("Sales Distribution by Region")
plt.tight_layout()
plt.show()

# ================================
# 4. HEATMAP – CORRELATION ANALYSIS
# ================================
corr = df[["Quantity", "Price", "Total_Sales"]].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# 5. MULTI-PLOT DASHBOARD (2×2)
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.lineplot(ax=axes[0, 0], data=df, x="Date", y="Total_Sales")
axes[0, 0].set_title("Sales Trend")

sns.barplot(ax=axes[0, 1], data=df, x="Region", y="Total_Sales")
axes[0, 1].set_title("Region-wise Sales")

sns.boxplot(ax=axes[1, 0], data=df, x="Product", y="Total_Sales")
axes[1, 0].set_title("Product Sales Distribution")
axes[1, 0].tick_params(axis='x', rotation=45)

sns.scatterplot(
    ax=axes[1, 1],
    data=df,
    x="Price",
    y="Total_Sales"
)
axes[1, 1].set_title("Price vs Total Sales")

plt.suptitle("Sales Dashboard Overview", fontsize=16)
plt.tight_layout()
plt.show()

# 6. INTERACTIVE BAR CHART (PLOTLY)
fig = px.bar(
    df,
    x="Product",
    y="Total_Sales",
    color="Region",
    hover_data=["Quantity", "Price"],
    title="Interactive Sales by Product"
)
fig.show()

# 7. INTERACTIVE LINE CHART (PLOTLY)

fig = px.line(
    df,
    x="Date",
    y="Total_Sales",
    color="Region",
    markers=True,
    title="Interactive Sales Trend"
)
fig.show()
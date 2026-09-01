import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load Data
df1 = pd.read_csv('index_1.csv')
df2 = pd.read_csv('index_2.csv')
if 'card' not in df2.columns:
    df2['card'] = np.nan

df = pd.concat([df1, df2], ignore_index=True)
df['datetime'] = pd.to_datetime(df['datetime'], format='mixed')
df['hour'] = df['datetime'].dt.hour
df['day_name'] = df['datetime'].dt.day_name()
df['coffee_name'] = df['coffee_name'].str.strip().str.title()
df['coffee_name'] = df['coffee_name'].replace({
    'Americano With Milk': 'Americano with Milk',
    'Chocolate With Milk': 'Chocolate with Milk',
    'Irish Whiskey With Milk': 'Irish Whiskey with Milk',
    'Coffee With Irish Whiskey': 'Coffee with Irish Whiskey',
    'Caramel With Irish Whiskey': 'Caramel with Irish Whiskey',
    'Vanilla With Irish Whiskey': 'Vanilla with Irish Whiskey',
    'Caramel With Chocolate': 'Caramel with Chocolate',
    'Irish With Chocolate': 'Irish with Chocolate',
    'Chocolate With Coffee': 'Chocolate with Coffee',
    'Coffee With Chocolate': 'Coffee with Chocolate',
    'Caramel With Milk': 'Caramel with Milk',
    'Double Espresso With Milk': 'Double Espresso with Milk'
})

# 2. Setup Canvas
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Panel 1: Top 5 Menu
top_menu = df.groupby('coffee_name')['money'].sum().sort_values(ascending=False).head(5)
sns.barplot(x=top_menu.values, y=top_menu.index, ax=axes[0, 0], palette="crest")
axes[0, 0].set_title("Top 5 Menu Contributors by Total Revenue ($)", fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel("Revenue ($)")
axes[0, 0].set_ylabel("")

# Panel 2: Hourly Demand
hourly_orders = df.groupby('hour')['datetime'].count()
sns.lineplot(x=hourly_orders.index, y=hourly_orders.values, ax=axes[0, 1], marker="o", color="#2b5c8f", linewidth=2.5)
axes[0, 1].fill_between(hourly_orders.index, hourly_orders.values, color="#2b5c8f", alpha=0.15)
axes[0, 1].set_title("Hourly Order Volume Profile (Peak Hours)", fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel("Hour of Day (24h)")
axes[0, 1].set_ylabel("Order Count")
axes[0, 1].set_xticks(range(6, 24))

# Panel 3: Revenue by Day
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_orders = df.groupby('day_name')['money'].sum().reindex(days_order)
sns.barplot(x=day_orders.index, y=day_orders.values, ax=axes[1, 0], palette="Blues_d")
axes[1, 0].set_title("Revenue by Day of Week", fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel("")
axes[1, 0].set_ylabel("Total Revenue ($)")
axes[1, 0].tick_params(axis='x', rotation=30)

# Panel 4: Payment Method
payment_counts = df['cash_type'].value_counts()
axes[1, 1].pie(payment_counts, labels=['Card (Cashless)', 'Cash'], autopct='%1.1f%%', colors=['#2ca02c', '#d62728'], explode=(0.08, 0), startangle=140)
axes[1, 1].set_title("Payment Method Share", fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('coffee_business_dashboard.png', dpi=300)
print("Dashboard visual berhasil disimpan sebagai 'coffee_business_dashboard.png'!")

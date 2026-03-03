import pandas as pd
import hashlib

def mask_email(email):
    if pd.isna(email): return "Unknown"
    return hashlib.sha256(str(email).encode()).hexdigest()[:10]

def process_retail_data():
    print("🚀 Starting Retail Analytics Pipeline...")
    df = pd.read_csv('raw_sales_data.csv')

    # 1. Cleaning: Drop rows with missing emails
    initial_count = len(df)
    df = df.dropna(subset=['customer_email'])
    print(f"🧹 Cleaned {initial_count - len(df)} incomplete records.")

    # 2. Privacy: Mask Emails
    df['customer_id'] = df['customer_email'].apply(mask_email)

    # 3. Calculation: Revenue
    df['total_revenue'] = df['quantity'] * df['unit_price']

    # 4. Aggregation: Sum up spending PER CUSTOMER
    customer_stats = df.groupby('customer_id')['total_revenue'].sum().reset_index()

    # 5. Business Logic: Loyalty Tiers
    def assign_tier(spend):
        if spend > 50000: return 'Gold (VIP)'
        if spend > 20000: return 'Silver'
        return 'Bronze'

    customer_stats['tier'] = customer_stats['total_revenue'].apply(assign_tier)
    
    customer_stats.to_csv('customer_segments.csv', index=False)
    print("✅ Customer Segmentation Complete! Saved to 'customer_segments.csv'")
    print(customer_stats['tier'].value_counts())

if __name__ == "__main__":
    process_retail_data()
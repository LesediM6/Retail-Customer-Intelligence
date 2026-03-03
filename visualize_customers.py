import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def create_segment_chart():
    print("📊 Generating Customer Segmentation Chart...")
    df = pd.read_csv('customer_segments.csv')

    plt.figure(figsize=(10, 6))
    # Count how many customers are in each tier
    sns.countplot(data=df, x='tier', order=['Gold (VIP)', 'Silver', 'Bronze'], palette='viridis')
    
    plt.title('Retail Customer Tier Distribution', fontsize=15)
    plt.xlabel('Loyalty Tier', fontsize=12)
    plt.ylabel('Number of Customers', fontsize=12)
    
    plt.savefig('customer_segments_report.png')
    print("✅ Chart saved as 'customer_segments_report.png'")

if __name__ == "__main__":
    create_segment_chart()
import pandas as pd
import numpy as np
import random

def generate_mock_data(records=50000):
    print(f"🏗️ Generating {records} messy retail records...")
    
    products = {
        'Laptop': 15000, 'Smartphone': 8000, 'Headphones': 1500, 
        'Monitor': 3000, 'Keyboard': 500, 'Mouse': 300
    }
    
    data = []
    for i in range(records):
        prod = random.choice(list(products.keys()))
        qty = random.randint(1, 2)
        # Randomly leave some emails empty (None) to simulate human error
        email = f"user_{random.randint(100, 999)}@example.com" if random.random() > 0.05 else None
        
        data.append({
            'transaction_id': f"TRX-{1000 + i}",
            'customer_email': email,
            'product': prod,
            'quantity': qty,
            'unit_price': products[prod],
            'timestamp': pd.Timestamp.now() - pd.to_timedelta(random.randint(0, 30), unit='d')
        })
    
    df = pd.DataFrame(data)
    df.to_csv('raw_sales_data.csv', index=False)
    print("✅ Created 'raw_sales_data.csv'!")

if __name__ == "__main__":
    generate_mock_data()
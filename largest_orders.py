import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
     # Count the number of orders per customer
    df = orders.groupby('customer_number').size().reset_index(name='count')
    
    # Sort by count in descending order
    df = df.sort_values(by='count', ascending=False)
    
    # Select the customer with the largest number of orders
    return df[['customer_number']].head(1)

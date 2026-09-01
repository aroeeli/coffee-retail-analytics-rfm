import pandas as pd
import numpy as np
import pymysql
from sqlalchemy import create_engine

def run_coffee_etl():
    print("1. Membaca dataset index_1.csv dan index_2.csv...")
    df1 = pd.read_csv('index_1.csv')
    df2 = pd.read_csv('index_2.csv')

    df1['source_dataset'] = 'batch_1'
    df2['source_dataset'] = 'batch_2'
    if 'card' not in df2.columns:
        df2['card'] = np.nan

    print("2. Menggabungkan dan membersihkan data...")
    df = pd.concat([df1, df2], ignore_index=True)

    # Standardisasi waktu
    df['datetime'] = pd.to_datetime(df['datetime'], format='mixed')
    df['date'] = pd.to_datetime(df['date']).dt.date
    
    # Feature Engineering
    df['hour'] = df['datetime'].dt.hour
    df['day_name'] = df['datetime'].dt.day_name()
    df['month_year'] = df['datetime'].dt.to_period('M').astype(str)
    df['is_weekend'] = df['datetime'].dt.weekday.apply(lambda x: 1 if x >= 5 else 0)

    # Standardisasi Nama Menu
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

    df['customer_id'] = df['card'].fillna('CASH_GUEST_USER')
    df = df.drop_duplicates().reset_index(drop=True)
    df['transaction_id'] = df.index + 1

    clean_df = df[[
        'transaction_id', 'datetime', 'date', 'month_year', 'day_name', 'hour', 'is_weekend',
        'coffee_name', 'money', 'cash_type', 'customer_id', 'source_dataset'
    ]]

    print("3. Memeriksa & membuat database di MySQL (Port 3307)...")
    # Buat database via raw connection terlebih dahulu
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', port=3307)
    with conn.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS coffee_analytics_db;")
    conn.close()

    print("4. Mengunggah tabel 'coffee_transactions'...")
    engine = create_engine('mysql+pymysql://root:@127.0.0.1:3307/coffee_analytics_db')
    clean_df.to_sql(name='coffee_transactions', con=engine, if_exists='replace', index=False)
    print(f"Sukses! {len(clean_df)} baris data berhasil tersimpan di tabel 'coffee_transactions'.")

if __name__ == '__main__':
    run_coffee_etl()

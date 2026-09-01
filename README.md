# Smart Coffee Retail Analytics & Customer Behavior

![Python](https://img.shields.io/badge/Python-ETL%20%26%20Viz-blue.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-green.svg)

## Executive Dashboard
![Coffee Analytics Dashboard](coffee_business_dashboard.png)

---

## Executive Summary
Analisis komprehensif terhadap **3.890+ transaksi ritel kopi** dari data operasional mesin kopi cerdas (*smart coffee kiosk*). Proyek ini mencakup alur data end-to-end: pembersihan dan rekayasa fitur waktu menggunakan **Python ETL**, pemodelan basis data di **MySQL**, visualisasi data menggunakan **Matplotlib & Seaborn**, hingga analisis bisnis mendalam meliputi **Segmentasi RFM Pelanggan**, **Pola Jam Sibuk Operasional**, dan **Optimasi Menu Berbasis Pareto**.

---

## Business Problem & Core Objectives
1. **Peak-Hour Demand:** Mengidentifikasi jam beban transaksi tertinggi untuk optimalisasi jadwal stok bahan baku (biji kopi, susu, cup) dan perawatan mesin.
2. **Customer RFM Segmentation:** Mengelompokkan lebih dari 1.300 pelanggan unik kartu menjadi segmen nilai bisnis (*Champions*, *At-Risk*, *Potential Loyalists*).
3. **Menu Optimization (Pareto 80/20):** Memetakan kontribusi pendapatan setiap varian kopi.
4. **Payment Dynamics:** Evaluasi tren adopsi pembayaran *cardless/contactless* vs *cash*.

---

## Key Findings & Business Insights
* **Pola Jam Sibuk:** Lonjakan transaksi utama terjadi pada pukul **10:00 - 11:00** (>670 pesanan) dan sore hari pukul **16:00** (307 pesanan dengan rata-rata belanja tertinggi $32.07). Rekomendasi operasional: lakukan *restock* bahan baku sebelum pukul 09:30 dan 15:30.
* **Segmentasi RFM:** Terpetakan 1.316 pelanggan kartu unik, memisahkan *Loyal Champions* dari segmen *At-Risk* (>150 hari tidak bertransaksi) untuk target re-engagement campaign.
* **Pareto Menu Kopi:** 4 Varian teratas (*Latte, Americano with Milk, Cappuccino, Americano*) menyumbang lebih dari **72% total pendapatan**.
* **Adopsi Cashless:** **95.66% transaksi** menggunakan kartu (*card*) dengan volume perputaran mencapai **$117,114.58**.

---

## Repository Structure
```text
├── index_1.csv
├── index_2.csv
├── coffee_business_dashboard.png
├── scripts/
│   ├── etl_coffee.py
│   └── generate_charts.py
├── sql/
│   └── coffee_advanced_analysis.sql
└── README.md

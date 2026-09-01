# ☕ End-to-End Coffee Retail Analytics & Customer Behavior

![Python](https://img.shields.io/badge/Python-ETL-blue.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0+-orange.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-green.svg)

## 📌 Executive Summary
Proyek ini menyajikan analisis komprehensif terhadap **3.890+ transaksi ritel kopi** dari dua batch data operasional mesin kopi cerdas (*smart coffee vending/kiosk*). Proyek ini dirancang dari pembersihan data mentah dan rekayasa fitur (*Feature Engineering*) menggunakan **Python ETL**, pemodelan basis data relasional di **MySQL**, hingga analisis bisnis tingkat lanjut meliputi **Segmentasi RFM Pelanggan**, **Pola Jam Sibuk Operasional**, dan **Optimasi Menu Berbasis Pareto**.

---

## 🎯 Business Problem & Core Objectives
1. **Pola Permintaan Jam Sibuk (*Peak-Hour Demand*):** Mengidentifikasi jam beban transaksi tertinggi untuk optimalisasi jadwal pengisian bahan baku (biji kopi, susu, cup) dan perawatan mesin.
2. **Segmentasi Pelanggan (RFM Analysis):** Mengelompokkan lebih dari 1.300 pelanggan unik kartu menjadi segmen nilai bisnis (*Champions*, *At-Risk*, *Potential Loyalists*) guna merancang strategi retensi yang tepat sasaran.
3. **Optimasi Menu (*Pareto Product Mix*):** Memetakan kontribusi pendapatan setiap varian kopi untuk mengidentifikasi menu *core driver* versus menu musiman yang berkinerja rendah.
4. **Dinamika Pembayaran:** Menganalisis adopsi sistem pembayaran non-tunai (*card vs. cash*) dan dampaknya terhadap rata-rata nilai transaksi (*Average Basket Size*).

---

## 🛠️ Data Pipeline & Technical Workflow
* **Extraction & Harmonization (Python / Pandas):** 
  * Penggabungan multi-sumber dataset (`index_1.csv` & `index_2.csv`).
  * Penanganan format waktu campuran (*mixed timestamp parsing*) dan ekstraksi dimensi waktu (*hour, day name, is_weekend*).
  * Standardisasi penamaan varian menu (*title casing & variation mapping*).
* **Database Staging & Querying (MySQL):**
  * Desain skema basis data relasional `coffee_analytics_db` pada tabel `coffee_transactions`.
  * Pemanfaatan *Common Table Expressions (CTEs)* dan *Window Functions (`NTILE`, `DENSE_RANK`, `SUM() OVER()`)* untuk segmentasi RFM dan distribusi kumulatif.

---

## 📊 Key Findings & Business Insights

### 1. Pola Jam Sibuk (Operational Peak Demand)
* **Puncak Pagi (10:00 - 11:00):** Mencatat total lebih dari **670 pesanan** dengan volume penjualan tertinggi dalam sehari.
* **Puncak Sore (16:00):** Mengalami lonjakan kedua dengan **307 pesanan** dan rata-rata belanja lebih tinggi (**$32.07** per transaksi).
* *Rekomendasi Operasional:* Jadwal inspeksi dan *refill* bahan baku harus dilakukan tepat sebelum pukul 09:30 dan pukul 15:30 untuk menghindari *out-of-stock* pada jam sibuk.

### 2. Segmentasi Pelanggan (RFM Matrix)
* Teridentifikasi **1.316 pelanggan kartu unik** dengan segmentasi kuartil:
  * **Champions / Loyal Regulars:** Pelanggan dengan frekuensi tinggi dan transaksi terbaru, menyumbang porsi pendapatan terbesar.
  * **At Risk / Need Re-activation:** Pelanggan dengan nilai belanja tinggi di masa lalu namun tidak bertransaksi dalam >150 hari terakhir (target prioritas promo re-engagement).

### 3. Analisis Menu (Prinsip Pareto 80/20)
* **4 Menu Utama** (*Latte, Americano with Milk, Cappuccino, Americano*) menyumbang lebih dari **72% total pendapatan keseluruhan**.
* Menu *specialty* seperti seri *Irish Whiskey* memiliki volume rendah namun mencatat margin harga stabil.

### 4. Adopsi Pembayaran Non-Tunai
* **95.66% transaksi** dilakukan secara non-tunai (*card*) dengan total perputaran volume mencapai **$117,114.58**, membuktikan preferensi pelanggan modern terhadap transaksi *contactless*.

---

## 📂 Project Structure
```text
├── index_1.csv
├── index_2.csv
├── scripts/
│   └── etl_coffee.py
├── sql/
│   └── coffee_advanced_analysis.sql
└── README.md

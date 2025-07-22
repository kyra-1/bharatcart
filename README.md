
# 🛒 BharatCart: E-Commerce Analytics with PySpark

`bharatcart` is a simulated e-commerce analytics engine designed to showcase real-world Business Analyst and Data Engineering workflows using **PySpark**.

It provides dashboards and insights for:
- Funnel drop-offs
- Seller performance
- City/category-wise conversions
- Refund trends and potential fraud patterns *(coming soon)*

---

## 📁 Project Structure

```

bharatcart/
├── pyspark\_jobs/
│   ├── funnel\_analysis.py          # Tracks stage-wise conversion
│   ├── seller\_metrics.py           # Revenue, orders, return rates
├── dashboards/
│   └── seller\_dashboard.py         # Visualizes top sellers & returns
├── generator/
│   └── data/events.csv             # Simulated events data
├── output/
│   ├── seller\_metrics/             # Seller-level CSV output
│   └── visuals/                    # PNG visualizations
├── utils/
│   └── spark\_session.py            # Spark config helper
└── README.md

````

---

## 📊 Dashboards & Metrics

### 🔹 Funnel Analysis
Using event logs (`view`, `cart`, `buy`, `return`), the pipeline tracks:
- Drop-off rates from view → cart → buy
- Return rates post-purchase
- Conversion performance per **category** and **city**

### 🔹 Seller Metrics
Calculates:
- 🏆 **Top Sellers** by revenue
- 📦 Total Orders and Returns
- 🔁 **Return Rate** insights (used for potential refund fraud detection)

Visualized with **Matplotlib + Seaborn** in `seller_dashboard.py`

---

## 🛠️ Setup Instructions

1. Clone this repo:
```bash
git clone https://github.com/kyra-1/bharatcart.git
cd bharatcart
````

2. Setup virtual environment & install dependencies:

```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

3. Run jobs:

```bash
# PySpark jobs
python pyspark_jobs/funnel_analysis.py
# Optional: if Hadoop setup fixed
# python pyspark_jobs/seller_metrics.py

# Generate visual dashboards
python dashboards/seller_dashboard.py
```

---

## 🔮 Future Enhancements

* ✅ Fraud Detection:

  * Flag sellers abusing return policies using **z-score** or **percentile-based** methods
* ✅ Funnel Drop-off Heatmaps by Time-of-Day
* ✅ Interactive Dashboards using Streamlit / Dash
* ✅ Data Ingestion pipeline with Kafka or real API simulation
* ✅ Deploy on AWS EMR for real-time scalability

---

## 📌 Author

**Yashika Aggarwal**
🚀 Aspiring Business Analyst / Data Engineer
🔗 [GitHub](https://github.com/kyra-1) | [LinkedIn](https://linkedin.com/in/yashika-aggarwal)

---

## 🧠 Motivation

This project was built to:

* Simulate real-world e-commerce pipelines using big data tools
* Showcase data storytelling using Spark + Python visualizations
* Strengthen portfolio for Business Analyst / Data Engineering roles



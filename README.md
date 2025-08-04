# 🛒 BharatCart: E-Commerce Analytics with PySpark

`bharatcart` is a simulated e-commerce analytics engine designed to showcase real-world Business Analyst and Data Engineering workflows using **PySpark**.

It provides dashboards and insights for:
- Funnel drop-offs
- Seller performance
- City/category-wise conversions
- Refund trends and potential fraud patterns *(coming soon)*

---

## 📁 Project Structure

The project is organized into data generation, PySpark processing jobs, and dashboard visualization scripts.

```
kyra-1-bharatcart/
├── README.md
├── dashboards/               # Scripts to generate visual dashboards
│   ├── funnel_dashboard.py
│   └── seller_dashboard.py
├── generator/                # Scripts to generate simulated data
│   ├── generate_data.py
│   └── data/                 # Raw CSV data is generated here
│       └── ...
├── pyspark_jobs/             # PySpark ETL jobs
│   ├── funnel_analysis.py
│   ├── seller_metrics.py
│   └── output/               # Intermediate data from Spark jobs
│       ├── funnel_analysis/
│       └── seller_metrics/
├── output/                   # Final visual outputs (dashboards)
│   └── visuals/
│       ├── funnel_analysis.png
│       └── ...
└── utils/                    # Helper modules
└── spark_session.py

```
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

Visualized with **Matplotlib + Seaborn** in `seller_dashboard.py` and `funnel_dashboard.py`.

---

## 🛠️ Setup Instructions

1.  Clone this repo:
    ```bash
    git clone [https://github.com/kyra-1/bharatcart.git](https://github.com/kyra-1/bharatcart.git)
    cd bharatcart
    ```

2.  Setup virtual environment & install dependencies:
    ```bash
    python -m venv .venv
    # On Windows
    .\.venv\Scripts\activate
    # On macOS/Linux
    # source .venv/bin/activate
    pip install -r requirements.txt
    ```

3.  Generate the data:
    ```bash
    python generator/generate_data.py
    ```

4.  Run the analytics jobs and create dashboards:
    ```bash
    # Run PySpark jobs to process the data
    python pyspark_jobs/funnel_analysis.py
    python pyspark_jobs/seller_metrics.py

    # Generate visual dashboards from the processed data
    python dashboards/funnel_dashboard.py
    python dashboards/seller_dashboard.py
    ```
    *Note: For Windows users, you may need to configure a `HADOOP_HOME` environment variable and install `winutils.exe` for PySpark to run without issues.*

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


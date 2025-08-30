# 🌍 Eco-Tourism Vulne## 🎯 Objectives
- Perform EDA to explore climate and tourism risk factors.
- Preprocess and clean the dataset.
- Train supervised ML models (Regression/Classification) for risk prediction.
- Apply unsupervised ML for anomaly detection (high-risk sites).
- Use explainable AI (SHAP, LIME) to understand model decisions.
- Build visualizations & geospatial maps of vulnerable sites.y Assessment using## 📊 Expected Outcomes
Trained ML models for predicting eco tourism vulnerability.
Risk classification system for "Low, Medium, High" vulnerability sites.
Anomaly detection for unusual eco site risks.
Geospatial visualization dashboard.
Policy level insights for sustainable eco tourism.

---

## 🌱 Applications
Governments & Policymakers → prioritize conservation funding.
Tourism Industry → sustainable tourism planning.
Researchers → analyze climate impact on biodiversity.
Communities → early warning system for high risk eco sites.ing

## 📌 Project Overview
This project applies **AI/ML techniques** to assess the **vulnerability of eco-tourism sites** under climate risks. Using the [Ecotourism Climate Risk Dataset (Kaggle)](https://www.kaggle.com/datasets/programmer3/ecotourism-climate-risk-dataset/data), the model analyzes factors like **biodiversity, air quality, flood risk, elevation, and human activity** to predict vulnerability scores and identify high-risk sites.

The aim is to support **sustainable tourism planning, conservation strategies, and climate risk management**.

---

## 🎯 Objectives
Perform EDA to explore climate and tourism risk factors.
• Preprocess and clean the dataset.
• Train supervised ML models (Regression/Classification) for risk prediction.
• Apply unsupervised ML for anomaly detection (high•risk sites).
• Use explainable AI (SHAP, LIME) to understand model decisions.
• Build visualizations & geospatial maps of vulnerable sites.

---

## 🗂️ Dataset
- Source: Kaggle – Ecotourism Climate Risk Dataset (~5,000 records).
- Features: Biodiversity index, AQI, Elevation, Flood Risk, Temperature, Soil erosion, Tourist activity, Vulnerability Score.
- Type: Tabular CSV dataset with structured environmental + socio-economic attributes.

---

## ⚙️ Methodology
1. Data Preprocessing: Handle missing values, normalization, and encoding.
2. Exploratory Data Analysis: Correlations, outlier detection, feature importance.
3. Model Training:
   - Regression: Random Forest, XGBoost.
   - Classification: Logistic Regression, Decision Trees, Gradient Boosting.
   - Clustering/Anomaly Detection: KMeans, Isolation Forest.
4. Evaluation Metrics: RMSE, MAE, R² (Regression), Accuracy, F1, ROC-AUC (Classification).
5. Explainability: SHAP to analyze key features driving vulnerability.
6. Visualization: Interactive risk maps (GeoPandas, Folium, Plotly).

---

## 🛠️ Tech Stack
- **Languages**: Python
- **Libraries**: pandas, numpy, scikit-learn, XGBoost, LightGBM, matplotlib, seaborn, geopandas, folium, shap
- **Dashboard**: Streamlit / Plotly Dash
- **Version Control**: GitHub

---

## 📊 Expected Outcomes
- Trained ML models for predicting eco-tourism vulnerability.
- Risk classification system for “Low, Medium, High” vulnerability sites.
- Anomaly detection for unusual eco-site risks.
- Geospatial visualization dashboard.
- Policy-level insights for sustainable eco-tourism.

---

## 🌱 Applications
- **Governments & Policymakers** → prioritize conservation funding.
- **Tourism Industry** → sustainable tourism planning.
- **Researchers** → analyze climate impact on biodiversity.
- **Communities** → early-warning system for high-risk eco-sites.

---

## 🔮 Future Scope
Integration with satellite imagery (Sentinel/Landsat).
Time series forecasting using LSTMs for dynamic vulnerability trends.
Multi modal ML combining text reports + environmental data.
Real time monitoring with IoT & sensors.

---

## 🚀 How to Run
1. Clone repo:
   ```bash
   git clone https://github.com/vishnuvadhan7/Eco-tourism-Climate-Risk-Prediction.git
   cd eco-tourism-vulnerability
   ```
2. Run the notebook or script for training:
   ```bash
   jupyter notebook
   ```
3. For dashboard (if implemented):
   ```bash
   streamlit run app.py
   ```

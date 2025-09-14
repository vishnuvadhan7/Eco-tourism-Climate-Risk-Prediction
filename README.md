# 🌿 Eco-Tourism Climate Risk Prediction Web Interface

A comprehensive web application for predicting climate risk and vulnerability scores for eco-tourism sites. This project combines machine learning models with an intuitive user interface to help assess environmental risks for tourism planning.

## 🚀 Features

### 📊 **Dual Prediction Models**
- **Climate Risk Score**: Continuous numerical prediction (0.0 - 1.0)
- **Flood Risk Category**: Classification into Low, Moderate, or High risk levels

### 🖥️ **User-Friendly Interface**
- Modern, responsive web design with gradient backgrounds
- Interactive form with sliders, dropdowns, and tooltips
- Real-time input validation and user feedback
- Visual risk indicators with color-coded results
- Animated gauge displays and probability bars

### 🧠 **Advanced ML Backend**
- Pre-trained Linear Regression model for climate risk scoring
- Logistic Regression classifier for flood risk assessment
- Automatic feature scaling and categorical encoding
- Comprehensive data preprocessing pipeline

## 📋 Input Parameters

### 🌍 **Geospatial Information**
- **Latitude**: Geographic coordinates (-90° to 90°)
- **Longitude**: Geographic coordinates (-180° to 180°)

### 🌱 **Environmental Factors**
- **Vegetation Type**: Forest, Mountain, Wetland, Grassland
- **Biodiversity Index**: Species richness scale (0.0 - 1.0)
- **Protected Area Status**: Conservation protection (Yes/No)
- **Elevation**: Height above sea level (meters)
- **Slope**: Terrain steepness (0° - 90°)
- **Soil Type**: Sandy, Clay, Loam, Rocky
- **Air Quality Index**: Pollution level (0 - 500)
- **Average Temperature**: Climate data (°C)

### 🏖️ **Tourism Information**
- **Tourist Attractions**: Number of major attractions
- **Accessibility Score**: Site accessibility rating (1-10)
- **Tourist Capacity Limit**: Maximum visitor capacity

## 🛠️ Technical Architecture

### **Backend (Flask API)**
```
app.py
├── Model Loading & Management
├── Data Preprocessing Pipeline
├── Prediction Endpoints (/api/predict)
├── Health Check (/api/health)
└── Static File Serving
```

### **Frontend (HTML/CSS/JavaScript)**
```
templates/index.html    # Main UI structure
static/styles.css       # Modern responsive styling
static/script.js        # Interactive functionality
```

### **ML Models & Data**
```
├── best_regression_model_linear.pkl      # Climate risk prediction
├── best_classification_model_logistic.pkl # Flood risk classification
├── regression_scaler.pkl                 # Feature scaling
├── classification_scaler.pkl             # Feature scaling
├── regression_encoders.pkl               # Categorical encoding
├── classification_encoders.pkl           # Categorical encoding
├── feature_names.json                    # Model feature mapping
└── sample_data.json                      # Test data examples
```

## 🚀 Quick Start

### **Prerequisites**
- Python 3.8+
- Dependencies listed in `requirements.txt`

### **Installation & Setup**

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Generate ML Models** (if not already done)
   ```bash
   python generate_models.py
   ```

3. **Start the Web Application**
   ```bash
   python app.py
   ```

4. **Access the Interface**
   - Open your browser to `http://localhost:5000`
   - Fill in the site information form
   - Click "Predict Climate Risk" to get results

### **Sample Data Testing**
The interface includes a "Fill Sample Data" button that populates the form with realistic test values for quick demonstration.

## 📊 Results Display

### **Climate Risk Score**
- Numerical score with visual gauge
- Color-coded risk levels:
  - 🟢 **Green**: Low Risk (0.0 - 0.33)
  - 🟡 **Yellow**: Medium Risk (0.33 - 0.67)
  - 🔴 **Red**: High Risk (0.67 - 1.0)

### **Flood Risk Assessment**
- Categorical prediction with confidence levels
- Probability distribution bars for all risk categories
- Color-coded category display

## 🔧 API Endpoints

### **POST /api/predict**
Main prediction endpoint accepting JSON data with site parameters.

**Request Format:**
```json
{
  "Latitude": 25.7617,
  "Longitude": -80.1918,
  "Vegetation_Type": "Wetland",
  "Biodiversity_Index": 0.75,
  "Protected_Area_Status": true,
  "Elevation_m": 2,
  "Slope_Degree": 5,
  "Soil_Type": "Sandy",
  "Air_Quality_Index": 85,
  "Average_Temperature_C": 24.5,
  "Tourist_Attractions": 6,
  "Accessibility_Score": 8,
  "Tourist_Capacity_Limit": 500
}
```

**Response Format:**
```json
{
  "success": true,
  "climate_risk_score": 0.423,
  "flood_risk_category": "Medium",
  "risk_probabilities": {
    "Low": 0.23,
    "Medium": 0.54,
    "High": 0.23
  },
  "risk_level": "Medium"
}
```

### **GET /api/health**
Health check endpoint to verify model loading status.

## 🎨 UI Components

### **Interactive Elements**
- Range sliders with real-time value display
- Dropdown menus for categorical selections
- Radio buttons for boolean choices
- Tooltip information icons
- Loading animations and error handling

### **Visual Feedback**
- Gradient backgrounds and modern styling
- Smooth animations and transitions
- Responsive design for mobile/desktop
- Color-coded results and indicators

## 🔬 Model Performance

### **Regression Model (Climate Risk)**
- **Algorithm**: Linear Regression
- **Test R² Score**: 0.8179
- **RMSE**: 0.0516
- **Features**: 20 engineered features

### **Classification Model (Flood Risk)**
- **Algorithm**: Logistic Regression  
- **Test Accuracy**: 90.40%
- **Classes**: Low, Medium, High
- **Features**: 20 engineered features

## 📂 Project Structure

```
d:\Eco-Tourism Climate Risk Prediction\
├── app.py                              # Flask web application
├── generate_models.py                  # Model training script
├── requirements.txt                    # Python dependencies
├── README.md                          # Project documentation
├── templates/
│   └── index.html                     # Main web interface
├── static/
│   ├── styles.css                     # CSS styling
│   └── script.js                      # JavaScript functionality
└── *.pkl, *.json                     # ML models and configuration
```

## 🌟 Key Benefits

1. **Accessibility**: Web-based interface requiring no technical expertise
2. **Accuracy**: Scientifically-trained ML models with high performance
3. **Speed**: Real-time predictions in seconds
4. **Visualization**: Clear, intuitive result displays
5. **Scalability**: RESTful API design for integration potential

## 🔮 Future Enhancements

- **Advanced Models**: Integration of XGBoost, Random Forest variants
- **Geographic Visualization**: Interactive maps with risk overlays  
- **Historical Data**: Time-series analysis and trend prediction
- **Batch Processing**: Multiple site analysis capabilities
- **Export Features**: PDF reports and data download options

## 📞 Support

This web interface demonstrates the complete workflow from data input to risk assessment, providing a practical tool for eco-tourism planning and environmental risk evaluation.

---
*Built with Python, Flask, scikit-learn, and modern web technologies.*
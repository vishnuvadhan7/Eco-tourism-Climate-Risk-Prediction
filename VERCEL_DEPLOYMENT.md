# 🚀 Vercel Deployment Guide

## Complete Step-by-Step Instructions for Deploying Eco-Tourism Climate Risk Prediction to Vercel

### Prerequisites

1. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
2. **Git Repository**: Your code should be in a Git repository (GitHub, GitLab, or Bitbucket)
3. **Vercel CLI** (optional): `npm install -g vercel`

---

## 📁 Project Structure for Vercel

Your project should have this structure:

```
eco-tourism-climate-risk-prediction/
├── api/
│   ├── predict.py              # Serverless function for predictions
│   └── health.py               # Serverless function for health check
├── public/
│   ├── index.html              # Main web interface
│   └── static/
│       ├── styles.css          # CSS styling
│       └── script.js           # JavaScript functionality
├── vercel.json                 # Vercel configuration
├── requirements.txt            # Python dependencies
├── package.json                # Node.js configuration
├── .vercelignore              # Files to ignore during deployment
├── setup_models.py            # Script to generate lightweight models
└── *.pkl files                # ML model files (generated)
```

---

## 🛠️ Deployment Steps

### Step 1: Prepare Your Repository

1. **Initialize Git Repository** (if not already done):
```bash
git init
git add .
git commit -m "Initial commit"
```

2. **Push to GitHub/GitLab/Bitbucket**:
```bash
git remote add origin <your-repository-url>
git push -u origin main
```

### Step 2: Generate Lightweight Models

Run the model setup script to create deployment-ready models:

```bash
python setup_models.py
```

This creates compressed model files suitable for Vercel's size limits.

### Step 3: Deploy via Vercel Dashboard

#### Option A: Web Interface (Recommended)

1. **Login to Vercel**:
   - Go to [vercel.com](https://vercel.com)
   - Sign in with your Git provider

2. **Import Project**:
   - Click "New Project"
   - Select your repository
   - Click "Import"

3. **Configure Settings**:
   - **Framework Preset**: Other
   - **Root Directory**: `./` (leave default)
   - **Build Command**: Leave empty
   - **Output Directory**: `public`
   - **Install Command**: `pip install -r requirements.txt`

4. **Environment Variables** (if needed):
   - Add any environment variables in the Environment Variables section

5. **Deploy**:
   - Click "Deploy"
   - Wait for deployment to complete

#### Option B: Vercel CLI

1. **Install Vercel CLI**:
```bash
npm install -g vercel
```

2. **Login**:
```bash
vercel login
```

3. **Deploy**:
```bash
vercel --prod
```

### Step 4: Configure Custom Domain (Optional)

1. In Vercel Dashboard, go to your project
2. Click on "Domains" tab
3. Add your custom domain
4. Follow DNS configuration instructions

---

## ⚙️ Configuration Files Explained

### `vercel.json`
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/predict.py",
      "use": "@vercel/python"
    },
    {
      "src": "api/health.py", 
      "use": "@vercel/python"
    },
    {
      "src": "public/**/*",
      "use": "@vercel/static"
    }
  ],
  "routes": [
    {
      "src": "/api/(.*)",
      "dest": "/api/$1"
    },
    {
      "src": "/(.*)",
      "dest": "/public/$1"
    }
  ]
}
```

### `requirements.txt`
```
pandas==2.2.2
numpy==1.26.4
scikit-learn==1.5.1
joblib==1.4.2
flask==3.0.3
```

### `.vercelignore`
```
# Ignore original Flask files
app.py
templates/
static/

# Ignore development files  
generate_models.py
eco_tourism_climate_risk_prediction_.py
README.md

# Ignore large data files
ecotourism_dataset.csv
```

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. **Large File Size Error**
- **Problem**: Model files too large for Vercel
- **Solution**: Use the `setup_models.py` script to create compressed models
- **Alternative**: Store models in external storage (AWS S3, Google Cloud Storage)

#### 2. **Import Errors**
- **Problem**: Missing Python packages
- **Solution**: Ensure all dependencies are in `requirements.txt`
- **Check**: Verify Python version compatibility

#### 3. **API Endpoint Not Working**
- **Problem**: 404 errors on `/api/predict`
- **Solution**: Check `vercel.json` routing configuration
- **Verify**: Serverless functions are in the `api/` directory

#### 4. **Cold Start Issues**
- **Problem**: First request takes long time
- **Solution**: This is normal for serverless functions
- **Optimization**: Consider upgrading to Vercel Pro for better performance

#### 5. **Model Loading Errors**
- **Problem**: Models not found or corrupted
- **Solution**: 
  - Regenerate models using `setup_models.py`
  - Check file paths in serverless functions
  - Verify models are not in `.vercelignore`

---

## 📊 Performance Optimization

### 1. **Model Size Optimization**
```python
# Use compression when saving models
joblib.dump(model, 'model.pkl', compress=3)
```

### 2. **Caching Strategy**
```python
# Cache loaded models in serverless functions
@app.before_first_request
def load_models():
    global models
    # Load models once
```

### 3. **Request Timeout**
```json
{
  "functions": {
    "api/predict.py": {
      "maxDuration": 30
    }
  }
}
```

---

## 🧪 Testing Your Deployment

### 1. **Test Health Endpoint**
```bash
curl https://your-app.vercel.app/api/health
```

### 2. **Test Prediction Endpoint**
```bash
curl -X POST https://your-app.vercel.app/api/predict \
  -H "Content-Type: application/json" \
  -d '{
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
  }'
```

### 3. **Test Web Interface**
- Open `https://your-app.vercel.app` in browser
- Fill out the form and test predictions

---

## 🔒 Security Considerations

### 1. **API Rate Limiting**
- Vercel automatically provides some rate limiting
- Consider implementing additional limits for production

### 2. **Input Validation**
- Always validate input data
- Sanitize user inputs
- Handle edge cases gracefully

### 3. **Error Handling**
- Don't expose internal errors to users
- Log errors for debugging
- Provide user-friendly error messages

---

## 📈 Monitoring and Analytics

### 1. **Vercel Analytics**
- Enable analytics in Vercel dashboard
- Monitor page views and performance

### 2. **Function Logs**
- View serverless function logs in Vercel dashboard
- Use for debugging and monitoring

### 3. **Performance Metrics**
- Monitor response times
- Track error rates
- Set up alerts for issues

---

## 🚀 Going Live Checklist

- [ ] All model files generated and compressed
- [ ] `vercel.json` configuration complete
- [ ] `requirements.txt` updated with correct versions
- [ ] Frontend files moved to `public/` directory
- [ ] API endpoints tested locally
- [ ] Repository pushed to Git provider
- [ ] Deployed to Vercel successfully
- [ ] Custom domain configured (optional)
- [ ] Health check endpoint working
- [ ] Prediction endpoint working
- [ ] Web interface fully functional
- [ ] Error handling tested
- [ ] Performance optimized

---

## 📞 Support Resources

- **Vercel Documentation**: [vercel.com/docs](https://vercel.com/docs)
- **Vercel Community**: [github.com/vercel/vercel/discussions](https://github.com/vercel/vercel/discussions)
- **Python on Vercel**: [vercel.com/docs/functions/serverless-functions/runtimes/python](https://vercel.com/docs/functions/serverless-functions/runtimes/python)

---

**🎉 Your Eco-Tourism Climate Risk Prediction app is now live on Vercel!**
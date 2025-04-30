# FORECASTING - CRYPTO - PRICE - PEAKS
FORECASTING CRYPTO PRICE  PEAKS:  REGRESSION – BASED  TIME – UNTIL – NEW - HIGH  PREDICTIONS

# Crypto TUNH Prediction & Generalization

A comprehensive framework for modeling **Time-Until-Next-High (TUNH)** across multiple cryptocurrencies using regime-aware feature engineering, ensemble stacking, and cross-crypto transfer learning.

---

## 📖 Introduction

Time-Until-Next-High (TUNH) measures the number of days until an asset reaches its next local peak. Accurate forecasts of TUNH help traders optimize their entry and exit timing, and inform risk management strategies. This project explores:

- **Regime-aware feature engineering** to capture bull vs. bear/neutral dynamics  
- Extraction of thousands of time-series features via **tsfresh**  
- Comparison of base learners (SVR, Random Forest, XGBoost, LSTM, MLP) under a **regime-split** evaluation framework  
- Construction of **stacked** and **mixture-of-experts** ensembles with CatBoost meta-learners  
- Evaluation of **cross-crypto generalization** by pre-training on BTC and few-shot fine-tuning on other coins  
- Analysis of **feature importance** via SHAP across regimes and coins  

---

## 🎯 Research Questions

1. **RQ1 – Model Comparison (BTC):**  
   Which machine and deep learning model forecasts BTC TUNH most accurately?

2. **RQ2 – Feature Importance:**  
   What are the most predictive features (and regimes) driving TUNH across coins?

3. **RQ3 – Cross-Crypto Generalization:**  
   Can a model trained on BTC data generalize to predict TUNH for other cryptocurrencies?

---

## 🛠️ Methods

### 1. Data Preparation  
- **Rolling window:** transform daily TUNH into overlapping windows (lags 5–20 days)  
- **Feature extraction:** compute ~1,500 statistical, frequency, and trend features per window via tsfresh  
- **Imputation & scaling:** fill missing values and standardize features  

### 2. Regime Engineering  
- **Define regimes:** label each day as “bull” (next-day faster TUNH) vs. “bear/neutral”  
- **Feature augmentation:** create bull-only and bear-only versions of each feature  

### 3. Base Models & Hyperparameter Tuning  
- **Algorithms:**  
  - SVR (polynomial kernel)  
  - Random Forest  
  - XGBoost  
  - LSTM (KerasTuner for architecture search)  
  - MLP (dense neural network)  
- **Validation:** 80% train / 10% walk-forward validation / 10% test  
- **Hyperparameter search:** RandomizedSearchCV, Optuna, KerasTuner  

### 4. Ensembling Strategies  
- **Stacked ensemble:** out-of-fold predictions from base learners → CatBoost meta-learner  
- **Mixture-of-Experts:** learnable soft weights blending specialist base models  

### 5. Feature Importance (RQ2)  
- **Compute SHAP values** for the chosen “best” model  
- **Aggregate mean absolute contributions** → percentage importance  
- **Visualize:** top-10 features per regime, summary table of top-5 across coins  

### 6. Cross-Crypto Transfer (RQ3)  
- **Pre-train** on BTC (first 80% of its history)  
- **Validate** on next 10% (few-shot fine-tuning) of target coin (e.g. PAXG, ETH)  
- **Test** on remaining 90% of target coin  
- **Metrics:** MAE, RMSE, MAPE, Directional Accuracy (DA)  

---

## 📈 Results Overview

- **RQ1:** Random Forest and XGBoost achieve lowest MAE/RMSE; MLP & XGBoost highest DA on BTC  
- **RQ2:** Regime-specific SHAP analysis identifies linear trend slopes, volatility, and autocorrelation features as top drivers  
- **RQ3:** Few-shot fine-tuned MLP generalizes with ~16–18% MAPE and ~90% DA across coins  

---

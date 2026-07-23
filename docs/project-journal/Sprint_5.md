# Sprint 5 – AI & Machine Learning Integration

## Sprint Goal

Integrate machine learning into the iGaming Analytics Platform by developing AI models for customer segmentation, VIP prediction, and churn prediction, and visualize the results in Power BI.

---

## Objectives Completed

### 1. Machine Learning Environment

- Created the `ml` project structure.
- Added source, models, and outputs folders.
- Configured Python environment and required libraries.

---

### 2. Customer Segmentation

- Performed feature engineering on player activity data.
- Applied K-Means clustering.
- Classified players into four business segments:
  - Casual Players
  - Regular Players
  - VIP Players
  - Dormant Players
- Exported results to `player_segments.csv`.

---

### 3. VIP Prediction

- Built a Random Forest classification model.
- Predicted high-value VIP players.
- Generated prediction probabilities.
- Exported results to `vip_predictions.csv`.

---

### 4. Churn Prediction

- Created a Random Forest churn prediction model.
- Predicted players likely to become inactive.
- Generated churn probability scores.
- Exported results to `churn_predictions.csv`.

---

### 5. AI Output Integration

- Combined segmentation, VIP prediction, and churn prediction into a single dataset.
- Created `ai_predictions.csv` for Power BI integration.

---

### 6. Power BI Integration

- Imported AI prediction data.
- Created relationships with existing player data.
- Developed a dedicated **AI Insights** dashboard page.

Dashboard includes:

- Total VIP Players KPI
- High Churn Players KPI
- Average VIP Probability
- Average Churn Probability
- Customer Segmentation Analysis
- VIP Players by Country
- Churn Risk by Country
- AI Prediction Results Table

---

## Skills Applied

- Python
- Pandas
- Scikit-Learn
- Machine Learning
- Random Forest
- K-Means Clustering
- Feature Engineering
- Model Evaluation
- CSV Export
- Power BI
- Data Modeling
- DAX
- Git
- GitHub

---

## Sprint Outcome

Successfully integrated machine learning into the analytics platform and visualized AI-driven business insights within Power BI.

Sprint Status: ✅ Completed
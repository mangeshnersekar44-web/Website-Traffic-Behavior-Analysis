# ==========================================
# WEBSITE TRAFFIC BEHAVIOR ANALYSIS + ML
# Professional End-to-End Project
# ==========================================

# ================================
# 1. IMPORT LIBRARIES
# ================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score
from sklearn.ensemble import RandomForestClassifier

# ================================
# 2. LOAD DATA
# ================================
df = pd.read_csv("website_traffic_dataset.csv")

print("\nDataset Shape:", df.shape)
print("\nFirst 5 Rows:\n", df.head())

# ================================
# 3. DATA CLEANING
# ================================
df['Bounce'] = df['Bounce'].map({'Yes': 1, 'No': 0})
df['Conversion'] = df['Conversion'].map({'Yes': 1, 'No': 0})

# ================================
# 4. EXPLORATORY DATA ANALYSIS (EDA)
# ================================

# ---- . Traffic Source Distribution ----
plt.figure()
sns.countplot(x='Traffic_Source', data=df)
plt.title("Traffic Source Distribution")
plt.xticks(rotation=45)
plt.show()


# ---- . Device Type Analysis ----
plt.figure()
sns.countplot(x='Device_Type', data=df)
plt.title("Device Type Distribution")
plt.show()

# ---- . Conversion by Device ----
plt.figure()
sns.barplot(x='Device_Type', y='Conversion', data=df)
plt.title("Conversion Rate by Device")
plt.show()



# ---- . Bounce vs Conversion ----
plt.figure()
sns.barplot(x='Bounce', y='Conversion', data=df)
plt.title("Bounce vs Conversion")
plt.show()

# ---- . Correlation Heatmap ----
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Matrix")
plt.show()

# ================================
# 5. ENCODING
# ================================
le = LabelEncoder()
categorical_cols = ['Page_Visited', 'Traffic_Source', 'Device_Type', 'Country']

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

# ================================
# 6. FEATURE & TARGET
# ================================
X = df.drop(['Conversion', 'User_ID', 'Session_ID'], axis=1)
y = df['Conversion']

# ================================
# 7. TRAIN-TEST SPLIT
# ================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ================================
# 8. MODEL BUILDING
# ================================
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# ================================
# 9. PREDICTION
# ================================
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]

# ================================
# 10. MODEL EVALUATION
# ================================
print("\nModel Performance:")
print("Accuracy:", accuracy_score(y_test, y_pred))
print("ROC-AUC:", roc_auc_score(y_test, y_prob))

print("\nClassification Report:\n", classification_report(y_test, y_pred))

# ---- Confusion Matrix ----
cm = confusion_matrix(y_test, y_pred)
plt.figure()
sns.heatmap(cm, annot=True, fmt='d')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# ================================
# 11. FEATURE IMPORTANCE
# ================================
importance = pd.Series(model.feature_importances_, index=X.columns)
importance = importance.sort_values(ascending=False)

plt.figure()
importance.plot(kind='bar')
plt.title("Feature Importance")
plt.show()

# ================================
# 12. ADVANCED VISUALS
# ================================

# ---- Time Spent vs Conversion ----
plt.figure()
sns.boxplot(x='Conversion', y='Time_Spent_Seconds', data=df)
plt.title("Time Spent vs Conversion")
plt.show()

# ---- Country vs Conversion ----
plt.figure()
sns.barplot(x='Country', y='Conversion', data=df)
plt.title("Conversion by Country")
plt.xticks(rotation=45)
plt.show()

# ================================
# 13. SAMPLE PREDICTION
# ================================
sample = X_test.iloc[0:1]
prediction = model.predict(sample)

print("\nSample Prediction (0=No, 1=Yes):", prediction)
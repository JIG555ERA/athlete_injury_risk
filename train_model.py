import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import roc_auc_score


# Load data
data = pd.read_csv('data/raw/athlete_health_data.csv')


X = data.drop('injury_risk', axis=1)
y = data['injury_risk']


X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, stratify=y, random_state=42
)


model = XGBClassifier(
n_estimators=300,
max_depth=5,
learning_rate=0.05,
subsample=0.8,
colsample_bytree=0.8,
eval_metric='logloss'
)


model.fit(X_train, y_train)


auc = roc_auc_score(y_test, model.predict_proba(X_test)[:,1])
print('ROC-AUC:', auc)


joblib.dump(model, 'models/injury_risk_model.pkl')
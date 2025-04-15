import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
df=pd.read_csv('dummy_dataset.csv')
X=df[['file_size','hash_diff_ratio']]
Y=df['Label']
label_enoder=LabelEncoder()
y_encoded=label_enoder.fit_transform(Y)
X_test,X_train,y_test,y_train=train_test_split(X,y_encoded,test_size=0.2,random_state=42)
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print(classification_report(y_test,y_pred,target_names=label_enoder.classes_))
joblib.dump(model,'ransomware_model.pkl')
joblib.dump(LabelEncoder,'label_encoder.pkl')

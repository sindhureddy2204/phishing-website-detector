import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("phishing_dataset.csv")

# Show dataset preview and info
print("\n Preview of Dataset:")
print(df.head())
print("\n Dataset Info:")
print(df.info())

# Drop 'id' column (not useful for training)
df = df.drop(columns=['id'])

# Define features and target
X = df.drop(['Result'], axis=1)
y = df['Result']

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\n Model Accuracy: {accuracy * 100:.2f}%")

# Predict on a new sample (must have 30 features)
print("\n Check a New URL")

#  This dummy input has 30 features. Replace with actual input if needed.
new_url_features = [[1, -1, 1, -1, 1, -1, 1, -1, 1, -1,
                     1, -1, 1, -1, 1, -1, 1, -1, 1, -1,
                     1, -1, 1, -1, 1, -1, 1, -1, 1, -1]]

prediction = model.predict(new_url_features)
print(" This URL is predicted to be:", "PHISHING" if prediction[0] == 1 else "LEGITIMATE")

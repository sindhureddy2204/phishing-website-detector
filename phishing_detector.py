import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Step 1: Load the dataset
data = pd.read_csv('phishing_dataset.csv')

# Step 2: Show first 5 rows of the data
print(" Preview of Dataset:")
print(data.head())

# Step 3: Show basic info about columns and data types
print("\n Dataset Info:")
print(data.info())

# Step 4: Prepare input and output
X = data[['Have_IP_Address', 'Have_HTTPS', 'URL_Length']]  # Features
y = data['Is_Phishing']  # Target

# Step 5: Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 6: Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 7: Predict on test set
y_pred = model.predict(X_test)

# Step 8: Show accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\n Model Accuracy: {accuracy * 100:.2f}%")

# Step 9: Predict phishing for a new custom URL

print("\n Check a New URL")

# Example input: pretend we extracted features from a new URL
custom_data = [[1, 0, 45]]  # IP present, no HTTPS, length 45

prediction = model.predict(custom_data)

if prediction[0] == 1:
    print(" This URL is predicted to be: PHISHING")
else:
    print("✅ This URL is predicted to be: SAFE")

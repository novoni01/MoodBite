import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Step 1: Read the CSV file
file_path = "C:/Users/saach/Downloads/merged/merged_data.csv"  # Adjust file path as needed
df = pd.read_csv(file_path, low_memory=False)  # Fix DtypeWarning

# Step 2: Preprocessing
# Replace 'none' (or other non-numeric values) with NaN
df.replace('none', np.nan, inplace=True)

# Step 3: Handle missing values
# Fill missing values in numeric columns with the median
numeric_columns = df.select_dtypes(include=['number']).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())

# For non-numeric columns, fill with the most frequent value (mode)
non_numeric_columns = df.select_dtypes(exclude=['number']).columns
for col in non_numeric_columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Create a binary feature for 'breakfast' (1 for breakfast, 0 for non-breakfast)
df['is_breakfast'] = df['breakfast'].apply(lambda x: 1 if x == 1 else 0)

# Select relevant columns for features
features = df[['is_breakfast', 'moodRange']]  # Use only these 2 features for training

# Scaling the features
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)
features_scaled = pd.DataFrame(features_scaled, columns=features.columns)  # Preserve feature names

# Step 4: K-Means Clustering
# Applying K-Means clustering
kmeans = KMeans(n_clusters=5, random_state=42)  # Adjust n_clusters based on your data
df['cluster'] = kmeans.fit_predict(features_scaled)

# Check the first few rows to confirm cluster assignments
print("Data with clusters:\n", df.head())

# Step 5: Train a Classifier (Random Forest Classifier)
# Feature columns and target
X = features_scaled  # Use the scaled features for training
y = df['cluster']  # Target is the cluster label

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the classifier (Random Forest in this case)
classifier = RandomForestClassifier(random_state=42)

# Train the classifier
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Evaluate the model's accuracy
print("Accuracy: ", accuracy_score(y_test, y_pred))

# Step 6: Define Food Recommendations for Each Cluster
# Map each cluster to specific food recommendations
cluster_recommendations = {
    0: "Healthy options: Salads, grilled chicken, and fresh fruits.",
    1: "Comfort foods: Pasta, pizza, and ice cream.",
    2: "Energy boosters: Nuts, yogurt, and smoothies.",
    3: "Light snacks: Crackers, cheese, and fruits.",
    4: "High-protein meals: Steak, eggs, and beans."
}

# Step 7: Get User Input
# Prompt the user to input their preferences
try:
    is_breakfast = int(input("Is it breakfast? (Enter 1 for yes, 0 for no): "))
    mood_range = int(input("What is your mood range? (Enter a number between 1 and 5): "))

    # Validate user input
    if is_breakfast not in [0, 1]:
        raise ValueError("Invalid input for breakfast. Please enter 0 or 1.")
    if mood_range < 1 or mood_range > 5:
        raise ValueError("Invalid input for mood range. Please enter a number between 1 and 5.")

    # Create a new input DataFrame
    new_input = [[is_breakfast, mood_range]]
    new_input_df = pd.DataFrame(new_input, columns=['is_breakfast', 'moodRange'])

    # Scale the new input using the same scaler
    new_input_scaled = scaler.transform(new_input_df)
    new_input_scaled = pd.DataFrame(new_input_scaled, columns=new_input_df.columns)  # Preserve feature names

    # Predict the cluster for the new input
    predicted_cluster = classifier.predict(new_input_scaled)[0]

    # Get the food recommendation for the predicted cluster
    recommendation = cluster_recommendations.get(predicted_cluster, "No recommendation available.")

    # Output the predicted cluster and food recommendation
    print(f"Recommended Food Cluster: {predicted_cluster}")
    print(f"Food Recommendation: {recommendation}")

except ValueError as e:
    print(f"Error: {e}")
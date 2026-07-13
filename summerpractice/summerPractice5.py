import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv(r'C:\Users\Durun\OneDrive\Documents\term 1 freshman\c++ projects\PYTHONGOLDER\summerpractice\fifa_world_cup_2026_player_performance.csv')

# features — stats that might predict scoring
features = [
    'minutes_played', 'shots', 'shots_on_target',
    'expected_goals_xg', 'dribbles_attempted',
    'key_passes', 'successful_dribbles',
    'offensive_contribution', 'creativity_score',
    'player_rating', 'performance_score',
    'goals'  # goals in individual matches
]
X = df[features].fillna(0)  # fillna replaces missing values with 0

# label — did they score more than 1 goals total
y = (df['total_goals_tournament'] > 1).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



#model = DecisionTreeClassifier(class_weight='balanced')
#model = RandomForestClassifier(class_weight='balanced', n_estimators=100, random_state=42)
model = RandomForestClassifier(
    class_weight='balanced', 
    n_estimators=200,      # more trees
    max_depth=10,          # limits how deep each tree grows
    min_samples_split=5,   # requires 5 samples to split a node
    random_state=42
)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(y.value_counts())
print(f"% scored 2+ goals: {y.mean()*100:.2f}%")
predictions = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, predictions):.2f}")
print(classification_report(y_test, predictions)) 
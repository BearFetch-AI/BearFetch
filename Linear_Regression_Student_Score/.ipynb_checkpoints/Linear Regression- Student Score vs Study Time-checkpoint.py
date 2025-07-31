#Import required libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#Load your data into a DataFrame and split into features (x) and target variable(y)
data = {'Hours Studied' : [1.5, 2, 3.0, 4.5, 6.0, 7.5, 8.5], 'Test Score' : [55, 60, 65, 75, 85, 95, 98]}
df = pd.DataFrame(data)

X = df[['Hours Studied']]
y = df['Test Score']

#Plot your Data
df.plot(x='Hours Studied', y= 'Test Score', kind='line', title='Hours Studied Vs Test Score', marker='o')

#Split your data iunto Training and Testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#Create a Linear Regression Model and train it
model = LinearRegression()
model.fit(X_train, y_train)

#Use the model to predict the Test scores of Testing data
y_pred = model.predict(X_test)

#Plot your Training data
plt.scatter(X_train.values.ravel(), y_train, color='blue')
plt.plot(X_train.values.ravel(), model.predict(X_train), color='red')
plt.title('Hours Studied vs Test Score')
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.show()

#Plot your Testing data and Predicted data outputs
plt.scatter(X_test.values.ravel(), y_test, color='green')
plt.plot(X_train.values.ravel(), model.predict(X_train), color='red')
plt.title('Hours Studied vs Test Score')
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.show()

plt.scatter(X_test.values.ravel(), y_test, color='green')
plt.plot(X_train.values.ravel(), model.predict(X_train), color='red')
plt.title('Hours Studied vs Test Score')
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.show()

#Calculate accuracy metrics
from sklearn.metrics import mean_squared_error, r2_score

r2 = r2_score(y_test, y_pred) # R - squared
mse = mean_squared_error(y_test, y_pred) # Mean Squared Error

print(f"R-squared: {r2:.2f}")
print(f"Mean Squared Error: {mse:.2f}")

#Create a script to predict the Test Scores based on the Hours of Study input
hr=float(input("Enter the number of hours(0-8):"))
y1=model.predict(np.array([hr]).reshape(-1, 1))
print("Predicted Test Score:",int(y1),"/100")

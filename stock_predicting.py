import numpy as np
import pandas as pd
from sklearn.svm import SVR
import matplotlib.pyplot as plt

def predict_prices(dates, prices, x):
    dates = np.reshape(dates, (len(dates), 1))

    svr_lin = SVR(kernel='linear', C=1e3)
    svr_poly = SVR(kernel='poly', C=1e3, degree=2)
    svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.1)
    svr_lin.fit(dates, prices)
    svr_poly.fit(dates, prices)
    svr_rbf.fit(dates, prices)

    plt.scatter(dates, prices, color='black', label='Data')
    plt.plot(dates, svr_rbf.predict(dates), color='red', label='RBF model')
    plt.plot(dates, svr_lin.predict(dates), color='green', label='Linear model')
    plt.plot(dates, svr_poly.predict(dates), color='blue', label='Polynomial model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support Vector Regression 6M Data')
    plt.legend()
    plt.show()

    return svr_rbf.predict(x)[0], svr_lin.predict(x)[0], svr_poly.predict(x)[0]



# data = pd.read_csv('dataset/NASDAQ-APPL_history.csv')
data = pd.read_csv('dataset/NASDAQ-APPL_history6M.csv')

dates = data['Date'].values
prices = data['Close/Last'].replace('[\$,]', '', regex=True).astype(float)
dates = np.array([i for i in range(len(dates))])
prices = np.array(prices)

# Predict the price for the next 20 days
predicted_price = predict_prices(dates, prices, 20)
print(f"Predicted price: {predicted_price}")


import numpy as np
# y-yprediction ka whole square
# (y-(intercept+mx))^2
def gradient_descent(x,y):
    m_curr=b_curr=0
    iteration=700
    n=len(x)
    learning_rate=0.001
    for i in range (iteration):
        y_pred =m_curr*x+ b_curr
        cost=(1/n)*sum([val**2 for val in(y-y_pred)]) 
        md=(-2/n)*sum(x*(y-y_pred))
        bd=(-2/n)*sum((y - y_pred ))
        m_curr=m_curr-learning_rate *md
        b_curr=b_curr -(learning_rate )*bd
        print("m b iteration cost respectively ",m_curr,b_curr,i,cost)

x=np.array([1,2,3,4,5])
y=np.array([5,8,11,14,17])
gradient_descent(x,y)
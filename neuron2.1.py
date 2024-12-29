import pandas as pd
import math
import random

#loading training file

data = {
    "x1": [0, 0, 1, 1],  # First input
    "x2": [0, 1, 0, 1],  # Second input
    "y": [0, 1, 1, 1]    # Output (AND of x1 and x2)
}

# Create a DataFrame from the data
truth_table = pd.DataFrame(data)

# Save the DataFrame to an Excel file
file_name = "truths.xlsx"
truth_table.to_excel(file_name, index=False)

print(f"Truth table saved to {file_name}")


data =pd.read_excel(file_name)

print(data.head())


x1= data['x1']
x2= data['x2']
y = data['y']



Epoch =0
w01=0.1
w02=0.1
w012=0.1
w021=0.1
w11=0.1
w12=0.1
b01=0.1
b02=0.1
b11=0.1
cost =10
lr=0.9999
momentum=0.9
v_w01=0
v_b01=0
while cost>0.00001:
    N =0
    sum_cost=0
    sum_dcost_dw01=0
    sum_dcost_dw02=0
    sum_dcost_dw012=0
    sum_dcost_dw021=0
    sum_dcost_dw11=0
    sum_dcost_dw12=0
    sum_dcost_db01=0
    sum_dcost_db02=0
    sum_dcost_db11=0
    for i, row in data.iterrows():
        x1_i=row['x1']
        x2_i=row['x2']
        y_i=row['y']
        z11=(x1_i*w01 + x2_i*w021)+b01
        a11=(1/(1+math.exp(-z11)))
        z12=(x2_i*w02 + x1_i*w012)+b02
        a12=(1/(1+math.exp(-z12)))
        z21=(a11*w11 + a12*w12)+b11
        a21=(1/(1+math.exp(-z21)))
        N +=1
        sum_cost +=((y_i-a21)**2)
        sum_dcost_dw01+=(-2*(y_i-a21)*a21*(1-a21)*w11*a11*(1-a11)*x1_i)
        sum_dcost_dw021+=(-2*(y_i-a21)*a21*(1-a21)*w11*a11*(1-a11)*x2_i)
        sum_dcost_dw02+=(-2*(y_i-a21)*a21*(1-a21)*w12*a12*(1-a12)*x2_i)
        sum_dcost_dw012+=(-2*(y_i-a21)*a21*(1-a21)*w12*a12*(1-a12)*x1_i)
        sum_dcost_dw11+=(-2*(y_i-a21)*a21*(1-a21)*a11)
        sum_dcost_dw12+=(-2*(y_i-a21)*a21*(1-a21)*a12)
        sum_dcost_db01+=(-2*(y_i-a21)*a21*(1-a21)*w11*a11*(1-a11)*1)
        sum_dcost_db02+=(-2*(y_i-a21)*a21*(1-a21)*w12*a12*(1-a12)*1)
        sum_dcost_db11+=(-2*(y_i-a21)*a21*(1-a21)*1)
        
    cost =(1/N)*sum_cost
    v_w01 = momentum * v_w01 + lr * sum_dcost_dw01
    w01-=v_w01
    w02-=(lr*sum_dcost_dw02)
    w012-=(lr*sum_dcost_dw012)
    w021-=(lr*sum_dcost_dw021)
    w11-=(lr*sum_dcost_dw11)
    w12-=(lr*sum_dcost_dw12)
    v_b01 = momentum * v_b01 + lr * sum_dcost_db01
    b01-=v_b01
    b02-=(lr*sum_dcost_db02)
    b11-=(lr*sum_dcost_db11)
    Epoch+=1
    print(f"Epoch: {Epoch}, cost: {cost}, lr: {lr}")


X1_ask= 0
X2_ask= 1
z11ask=(X1_ask*w01 + X2_ask*w021)+b01
a11ask=(1/(1+math.exp(-z11ask)))
z12ask=(X2_ask*w02 + X1_ask*w012)+b02
a12ask=(1/(1+math.exp(-z12ask)))
z21ask=(a11ask*w11 + a12ask*w12)+b11
a21ask=(1/(1+math.exp(-z21ask)))
print(f"given {X1_ask} and {X2_ask}\n")
print(f"The output is: {a21ask:.2f}")

    



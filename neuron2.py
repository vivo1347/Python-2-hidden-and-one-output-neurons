import pandas as pd
import math

#loading training file

data = {
    "x1": [0, 0, 1, 1],  # First input
    "x2": [0, 1, 0, 1],  # Second input
    "y": [0, 0, 0, 1]    # Output (AND of x1 and x2)
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



Epoch = 0
w1=1
w2=1
b1=1
b2=1
w11=1
cost =10
lr=7.5
while cost>0.00001:
    N =0
    sum_cost=0
    sum_dcost_dw1=0
    sum_dcost_dw2=0
    sum_dcost_b1=0
    sum_dcost_b2=0
    sum_dcost_dw11=0
    for i, row in data.iterrows():
        x1_i=row['x1']
        x2_i=row['x2']
        y_i=row['y']
        z11=(x1_i*w1)+(x2_i*w2)+b1
        a11=(1/(1+math.exp(-z11)))
        z21=(a11*w11)+b2
        a21=(1/(1+math.exp(-z21)))
        N +=1
        sum_cost +=((y_i-a21)**2)
        sum_dcost_dw1 +=(-2*(y_i-a21)*a21*(1-a21)*a11*(1-a11)*x1_i)
        sum_dcost_dw2 +=(-2*(y_i-a21)*a21*(1-a21)*a11*(1-a11)*x2_i)
        sum_dcost_b1+=(-2*(y_i-a21)*a21*(1-a21)*a11*(1-a11)*1)
        sum_dcost_b2+=(-2*(y_i-a21)*a21*(1-a21)*a11*(1-a11)*1)
        sum_dcost_dw11+= (-2*(y_i-a21)*a21*(1-a21)*a11)
    cost =(1/N)*sum_cost
    w1 -=(lr*sum_dcost_dw1)
    w2-=(lr*sum_dcost_dw2)
    b1-=(lr*sum_dcost_b1)
    b2-=(lr*sum_dcost_b2)
    w11 -=(lr*sum_dcost_dw11)
    Epoch+=1
    print(f"Epoch: {Epoch}, cost: {cost}, w1: {w1},w2: {w2},b1: {b1}, b2: {b2}, w11: {w11}")


X1_ask= 0
X2_ask= 1
z_ask11=(X1_ask*w1)+(X2_ask*w2)+b1
a_ask11= (1/(1+math.exp(-z_ask11)))
z_ask21=(a_ask11*w11)+b2
a_ask21= (1/(1+math.exp(-z_ask21)))
print(f"given {X1_ask} and {X2_ask}\n")
print(f"The output is: {a_ask21:.2f}")

    


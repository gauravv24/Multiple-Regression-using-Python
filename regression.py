columns = input("Enter the number of variables \n")
columns = int(columns)
total_values = input("\nEnter total values: \n")
total_values = int(total_values)

dependent_variables = 1 
independent_variables = int(columns)-1

column = {}
for i in range(columns):
  column[i+1] = []


print("\nEnter the values of dependent variable \n")
for i in  range(total_values):
  inputvalue = (int)(input("Enter the value of dependent variable " +str(i+1)+ ": "))
  column[1].append(inputvalue)

for i in range(independent_variables):
    print("\n")
    for j in range(total_values):
        value = input("Enter the "+str(j+1)+" value of "+ str(i+1)+ " column: ")
        column[i+2].append(value)
  


print("\nColumn Values: \n")
print(column)


rows, cols = (columns, total_values)

matrix=[[] for i in range(cols)]
transpose=[[] for i in range(rows)]
matrix_mul = [[] for i in range(rows)]

i=1
for i in range(cols):  
  valu = 1
  matrix[i].append(valu)
  
print("\nEmpty Matrix Model: \n")
print(matrix)
i=0

dependent_matrix = [[] for i in range(total_values)]

#loop for storing values of dependent variable:

for i in range(total_values):
        temp_value = column[1][i];
        dependent_matrix[i].append(temp_value)
    
print("\nDependent Matrix Values: \n")
print(dependent_matrix)

for i in range(total_values):
  for j in range(independent_variables):
      val = int(column[j+2][i])
      matrix[i].append(val)

print("\nColumn Values: \n")

print(matrix)

for i in range(cols):
   # iterate through columns
   for j in range(len(matrix[0])):
     temp = matrix[i][j]
     transpose[j].append(temp)

       
print("\nTranspose Values: \n")
print(transpose)

for i in range(len(transpose)):
   # iterate through columns of Y
   for j in range(len(matrix[0])):
     temp1=0

     for k in range(len(matrix)):
         temp1 += transpose[i][k] * matrix[k][j]

     matrix_mul[i].append(temp1)
       
print("\nMatrix Multiplication with transpose Values: \n")

print(matrix_mul)

def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                print("MATRIX NOT INVERTIBLE")
                return -1
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret

inverse_matrix =inverse(matrix_mul)

print("\nInverse Matrix Values: \n")

print(inverse_matrix)

#inverse_matrix into transpose matrix
final1 = [[] for i in range(len(inverse_matrix))]


for i in range(len(inverse_matrix)):
   # iterate through columns of Y
   for j in range(len(transpose[0])):
     temp1=0

     for k in range(len(transpose)):
         temp1 += inverse_matrix[i][k] * transpose[k][j]

     final1[i].append(temp1)


print("\nMultiplication of Inverse Matrix with Transpose: \n")

print(final1)

#finalMatrix into final1 matrix
finalMatrix = [[] for i in range(len(final1))]


for i in range(len(final1)):
   # iterate through columns of Y
   for j in range(len(dependent_matrix[0])):
     temp1=0

     for k in range(len(dependent_matrix)):
         temp1 += final1[i][k] * dependent_matrix[k][j]

     finalMatrix[i].append(temp1)


print("\nFinal Values: \n")

final_values = []

for i in range(len(finalMatrix)):
      for j in range(1):
            
            temp = round(finalMatrix[i][j],2)
            final_values.append(temp)
            
print(final_values)


stra = "Equation: y = "
equation = []
equation.append(stra)
for i in range(len(final_values)):
    if(i==0):
        var = str(final_values[i])
        equation.append(var)
    else:
        var = " + "+ str(final_values[i]) + " x"+str(i);
        equation.append(var)
    
print("\n")
for i in range(len(equation)):
    print(equation[i],end='')
    
print("\n")
print("Enter the values for prediction \n")

predic = []
predic.append(1)
for i in range(columns-1):
    preval = int(input("-> Enter the value of " + str(i+1) +" independent variable \n"))
    predic.append(preval)
    
print(predic)

predvalue = 0
count=0

for i in range(columns):
    tempval = final_values[count]*predic[count]
    predvalue += tempval
    count+=1

print("\n")
print("Prediction Value: ", predvalue)

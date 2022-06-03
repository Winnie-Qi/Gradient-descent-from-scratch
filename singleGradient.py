'''随机梯度下降法 SGD（stochastic gradient descent）'''
#Training data set
#each element in x represents (x0,x1,x2)
x = [(1,0.,3) , (1,1.,3) ,(1,2.,3), (1,3.,2) , (1,4.,4)]
#y[i] is the output of y = theta0 * x[0] + theta1 * x[1] +theta2 * x[2]
y = [95.364,97.217205,75.195834,60.105519,49.342380]

 
epsilon = 0.0001
#learning rate
alpha = 0.01
diff = [0,0]
error1 = 0
error0 =0
m = len(x)

 
#init the parameters to zero
theta0 = 0
theta1 = 0
theta2 = 0
 
while True:
   #calculate the parameter
    for i in range(m): #这个循环是遍历所有采样点
     
         diff[0] = y[i]-( theta0 + theta1 * x[i][1] + theta2 * x[i][2] ) #因为损失函数用的LMS算法，所以前面那条已经是(h(x)-y)了，再乘上x就是梯度了
         
         theta0 = theta0 + alpha * diff[0]* x[i][0] #已经开始更新了
         theta1 = theta1 + alpha * diff[0]* x[i][1]
         theta2 = theta2 + alpha * diff[0]* x[i][2]
     
    #calculate the cost function
         error1=0 # 为什么不在前面定义？？？
    for lp in range(len(x)):
         error1 += ( y[i]-( theta0 + theta1 * x[i][1] + theta2 * x[i][2] ) )**2/2
     
    if abs(error1-error0) < epsilon:
         break
    else:
         error0 = error1
     
    print (' theta0 : %f, theta1 : %f, theta2 : %f, error1 : %f ' )
 
print( 'Done: theta0 : %f, theta1 : %f, theta2 : %f')



'''随机梯度下降法 SGD（stochastic gradient descent）'''
#Training data set
#each element in x represents (x0,x1,x2)
x = [(1,0.,3) , (1,1.,3) ,(1,2.,3), (1,3.,2) , (1,4.,4)]
#y[i] is the output of y = theta0 * x[0] + theta1 * x[1] +theta2 * x[2]
y = [95.364,97.217205,75.195834,60.105519,49.342380]
 
epsilon = 0.000001
#learning rate
alpha = 0.001
diff = [0,0]
error1 = 0
error0 =0
m = len(x)
 
#init the parameters to zero
theta0 = 0
theta1 = 0
theta2 = 0
sum0 = 0
sum1 = 0
sum2 = 0
while True:
   
     #calculate the parameters
     for i in range(m):
         #begin batch gradient descent
         diff[0] = y[i]-( theta0 + theta1 * x[i][1] + theta2 * x[i][2] )
         sum0 = sum0 + alpha * diff[0]* x[i][0]
         sum1 = sum1 + alpha * diff[0]* x[i][1]
         sum2 = sum2 + alpha * diff[0]* x[i][2]
         #end  batch gradient descent
     theta0 = sum0;
     theta1 = sum1;
     theta2 = sum2;  # 批梯度下降算法在迭代的时候，是完成所有样本的迭代后才会去更新一次theta参数.为啥我觉得其实没区别？？？
     #calculate the cost function
     error1 = 0
     for lp in range(len(x)):
         error1 += ( y[i]-( theta0 + theta1 * x[i][1] + theta2 * x[i][2] ) )**2/2
     
     if abs(error1-error0) < epsilon:
         break
     else:
         error0 = error1
     
     print (' theta0 : %f, theta1 : %f, theta2 : %f, error1 : %f')
 
print ('Done: theta0 : %f, theta1 : %f, theta2 : %f')


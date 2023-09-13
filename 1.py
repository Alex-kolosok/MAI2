#Свеженцева,Сивцов, Михайловский 1 двойка
import matplotlib.pyplot as plt
import pulp
import time
start = time.time()
x = pulp.LpVariable("x", lowBound=0)
y = pulp.LpVariable("y", lowBound=0)
problem = pulp.LpProblem('0',pulp.LpMaximize)
problem += x - 2*y, "Функция цели"
problem += 5*x + 3*y >= 30, "1"
problem += x - y <= 3, "2"
problem += -3*x + 5*y <= 15, "3"
problem += x >= 0, "4"
problem += y >= 0, "5"
problem.solve()
s = []
print ("Результат:")
for variable in problem.variables():
 s.append(variable.varValue)
 print (variable.name, "=", variable.varValue)

problem = pulp.LpProblem('0',pulp.LpMinimize)
problem += x - 2*y, "Функция цели"
problem += 5*x + 3*y >= 30, "1"
problem += x - y <= 3, "2"
problem += -3*x + 5*y <= 15, "3"
problem += x >= 0, "4"
problem += y >= 0, "5"
problem.solve()
a = []
print ("Результат:")
for variable in problem.variables():
 a.append(variable.varValue)
 print (variable.name, "=", variable.varValue)


plt.title('Задание 1')
plt.xlabel('значение y')
plt.ylabel('значение y')
plt.xlim(0,20)
plt.ylim(0,20)

plt.scatter(x=a[0],y=a[1],c='black')
plt.scatter(x=s[0],y=s[1],c='black')
plt.plot([4.875, 1.875], [15,12], c='green')
plt.plot([0, 40], [19,19], c='orange')
#plt.plot([28.2, 0],[0,35.25],c='blue')
#plt.plot([12,0],[0,7],c='red')
plt.grid()
plt.show()
print ("Прибыль:")
print (problem.objective)
stop = time.time()
print ("Время :")
print(stop- start)
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import argparse
import os
import csv

parser = argparse.ArgumentParser(description="Bring all data together")
parser.add_argument("--function",  required=True, help="name of function", type=str)
parser.add_argument("--path",  required=True, help="name of file", type=str)
args = parser.parse_args() 
function_name = args.function
file_name = args.path

if function_name == "Rosenbrock":
    ww_min = -2
    ww_max = 2
    wh_min = -1.0
    wh_max = 3.0
elif function_name == "Booth":
    ww_min = -10
    ww_max = 10
    wh_min = -10
    wh_max = 10
    #bnd = [[-10, 10]]*2
elif function_name == "Ackley":
    ww_min = -5
    ww_max = 5
    wh_min = -5
    wh_max = 5
    #bnd = [[-5, 5]]*2
elif function_name == "Beale":
    ww_min = -4.5
    ww_max = 4.5
    wh_min = -4.5
    wh_max = 4.5
    #bnd = [[-4.5, 4.5]]*2
elif function_name == "Goldstein_Price":
    ww_min = -2
    ww_max = 2
    wh_min = -3
    wh_max = 1
    #bnd = [[-2, 2]]*2
elif function_name == "Bukin":
    ww_min = -15
    ww_max = -7
    wh_min = -4
    wh_max = 6
    #bnd = [[-15, -5], [-3, 3]]
elif function_name == "Matyas":
    ww_min = -10
    ww_max = 10
    wh_min = -10
    wh_max = 10
    #bnd = [[-10, 10]]*2
elif function_name == "Levi":
    ww_min = -10
    ww_max = 10
    wh_min = -10
    wh_max = 10
    #bnd = [[-10, 10]]*2
elif function_name == "Himmelblau":
    ww_min = -5
    ww_max = 5
    wh_min = -5
    wh_max = 5
    #bnd = [[-5, 5]]*2
elif function_name == "Three_hump_camel":
    ww_min = -5
    ww_max = 5
    wh_min = -5
    wh_max = 5
    #bnd = [[-5, 5]]*2
elif function_name == "Easom":
    ww_min = -1
    ww_max = 7
    wh_min = -1
    wh_max = 7
    #bnd = [[-100, 100]]*2
elif function_name == "Cross_in_tray":
    ww_min = -10
    ww_max = 10
    wh_min = -10
    wh_max = 10
    #bnd = [[-10, 10]]*2
elif function_name == "Eggholder":
    ww_min = -750
    ww_max = 750
    wh_min = -750
    wh_max = 750
    #bnd = [[-512, 512]]*2
elif function_name == "Holder":
    ww_min = -10
    ww_max = 10
    wh_min = -10
    wh_max = 10
    #bnd = [[-10, 10]]*2
elif function_name == "McCormick":
    ww_min = -3
    ww_max = 4
    wh_min = -3
    wh_max = 4
    #bnd = [[-1.5, 4], [-3, 4]]
elif function_name == "Schaffer_N2":
    ww_min = -100
    ww_max = 100
    wh_min = -100
    wh_max = 100
    #bnd = [[-100, 100]]*2
elif function_name == "Schaffer_N4":
    ww_min = -100
    ww_max = 100
    wh_min = -100
    wh_max = 100
    #bnd = [[-100, 100]]*2
else:
    print('Bounds not right')
    exit()    

#feature_x = np.arange(ww_min, ww_max, 500)
#feature_y = np.arange(wh_min, wh_max, 500)
  
# Creating 2-D grid of features
#[x, y] = np.meshgrid(feature_x, feature_y)
  
fig, ax = plt.subplots(1, 1)

if function_name == "Rosenbrock":
    # Rosenbrock (banana) function
    def f(x1, y1): return (1-x1)**2+100*(y1-x1**2)**2
    global_x = [1]
    global_y = [1]
    x1 = np.linspace(ww_min, ww_max)
    y1 = np.linspace(wh_min, wh_max)
elif function_name == "Booth":
    # Booth function
    def f(x1, y1): return (x1+2*y1-7)**2 + (2*x1+y1-5)**2
    global_x = [1]
    global_y = [3]
    x1 = np.linspace(ww_min, ww_max)
    y1 = np.linspace(wh_min, wh_max)
elif function_name == "Ackley":
    def f(x1, y1): return -20 * np.exp(-0.2 * np.sqrt(0.5 * (x1**2 + y1**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x1) + np.cos(2*np.pi*y1))) + np.e + 20
    global_x = [0]
    global_y = [0]
    x1 = np.linspace(ww_min, ww_max)
    y1 = np.linspace(wh_min, wh_max)
elif function_name == "Beale":
    global_x = [3]
    global_y = [0.5]
    x1 = np.linspace(ww_min, ww_max)
    y1 = np.linspace(wh_min, wh_max)
    def f(x1, y1): return (1.5 - x1 + x1 * y1)**2 + (2.25 - x1 + x1*y1**2)**2 + (2.625 - x1 + x1 * y1**3)**2
elif function_name == "Goldstein_Price":
    global_x = [0]
    global_y = [-1]
    x1 = np.linspace(ww_min, ww_max)
    y1 = np.linspace(wh_min, wh_max)
    function_name == "Goldstein-Price"
    def f(x1, y1): return (1 + (x1+y1+1)**2 * (19 - 14*x1 + 3*x1**2 - 14*y1 + 6*x1*y1 + 3*y1**2)) * (30 + (2*x1 - 3*y1)**2 * (18 - 32*x1 + 12*x1**2 + 48*y1 -36*x1*y1 + 27*y1**2))
elif function_name == "Bukin":
    global_x = [-10]
    global_y = [1]
    x1 = np.linspace(ww_min, ww_max)
    y1 = np.linspace(wh_min, wh_max)
    def f(x1, y1): return 100 * np.sqrt(np.abs(y1 - 0.01*x1**2)) + 0.01 * np.abs(x1 + 10)
elif function_name == "Matyas":
    global_x = [0]
    global_y = [0]
    x1 = np.linspace(ww_min, ww_max)
    y1 = np.linspace(wh_min, wh_max)
    def f(x1, y1): return 0.26 * (x1**2 + y1**2) - 0.48*x1*y1
elif function_name == "Levi":
    global_x = [1]
    global_y = [1]
    x1 = np.linspace(ww_min, ww_max)
    y1 = np.linspace(wh_min, wh_max)
    def f(x1, y1): return np.sin(3*np.pi*x1)**2 + (x1 - 1)**2 * (1+np.sin(3*np.pi*y1)**2) + (y1-1)**2 *(1+np.sin(2*np.pi*y1)**2)
elif function_name == "Himmelblau":
    global_x = [3.0, -2.805118, -3.779310,  3.584428]
    global_y = [2.0,  3.131312, -3.283186, -1.848126]
    x1 = np.linspace(ww_min, ww_max)
    y1 = np.linspace(wh_min, wh_max)
    def f(x1, y1): return (x1**2 + y1 - 11)**2 + (x1 + y1**2 - 7)**2
elif function_name == "Three_hump_camel":
    global_x = [0]
    global_y = [0]
    x1 = np.linspace(ww_min, ww_max)
    y1 = np.linspace(wh_min, wh_max)
    function_name == "Three-hump camel"
    def f(x1, y1): return 2*(x1**2) - (1.05*(x1**4)) + (x1**6 / 6) + x1*y1 + y1**2
elif function_name == "Easom":
    global_x = [np.pi]
    global_y = [np.pi]
    x1 = np.linspace(ww_min, ww_max)
    y1 = np.linspace(wh_min, wh_max)
    def f(x1, y1): return - np.cos(x1)*np.cos(y1)*np.exp(-((x1-np.pi)**2 + (y1-np.pi)**2))
elif function_name == "Cross_in_tray":
    global_x = [1.34941, 1.34941, -1.34941, -1.34941]
    global_y = [-1.34941, 1.34941, 1.34941, -1.34941]
    x1 = np.linspace(ww_min, ww_max)
    y1 = np.linspace(wh_min, wh_max)
    function_name = "Cross-in-tray"
    def f(x1, y1): return -0.0001 * (np.abs(np.sin(x1)*np.sin(y1)*np.exp(np.abs(100 - (np.sqrt(x1**2 + y1**2)/np.pi)))) + 1)**0.1
elif function_name == "Eggholder":
    global_x = [512]
    global_y = [404.2319]
    x1 = np.linspace(ww_min, ww_max)
    y1 = np.linspace(wh_min, wh_max)
    def f(x1, y1): return -(y1+47)*np.sin(np.sqrt(np.abs((x1/2)+(y1+47)))) - x1*np.sin(np.sqrt(np.abs(x1 - (y1+47))))
elif function_name == "Holder":
    global_x = [8.05502, -8.05502, 8.05502, -8.05502]
    global_y = [9.66459, 9.66459, -9.66459, -9.66459]
    x1 = np.linspace(ww_min, ww_max)
    y1 = np.linspace(wh_min, wh_max)
    def f(x1, y1): return - np.abs(np.sin(x1)*np.cos(y1)*np.exp(np.abs(1 - (np.sqrt(x1**2 + y1**2)/np.pi))))
elif function_name == "McCormick":
    global_x = [-0.54719]
    global_y = [-1.54719]
    x1 = np.linspace(ww_min, ww_max)
    y1 = np.linspace(wh_min, wh_max)
    def f(x1, y1): return np.sin(x1+y1) + (x1-y1)**2 - 1.5*x1 + 2.5*y1 + 1
elif function_name == "Schaffer_N2":
    global_x = [0]
    global_y = [0]
    x1 = np.linspace(ww_min, ww_max)
    y1 = np.linspace(wh_min, wh_max)
    function_name = "Schaffer N.2"
    def f(x1, y1): return 0.5 + ((np.sin(x1**2 - y1**2)**2 - 0.5)/((1+0.001*(x1**2 + y1**2)**2)))
elif function_name == "Schaffer_N4":
    global_x = [0, 0, 1.25313, -1.25313]
    global_y = [1.25313, -1.25313, 0, 0]
    x1 = np.linspace(ww_min, ww_max)
    y1 = np.linspace(wh_min, wh_max)
    function_name = "Schaffer N.4"
    def f(x1, y1): return 0.5 + ( ((np.cos(np.sin(np.abs(x1**2 - y1**2)))**2) - 0.5) / ((1 + 0.001*(x1**2 + y1**2))**2) )
else:
    print("FUNCTION ERROR EXITING")
    exit()
  
#def f(x1, y1): return np.cos(X / 2) + np.sin(Y / 4)
  
# plots contour lines
#ax.contourf(x, y, Z)

X1, Y1 = np.meshgrid(x1, y1)
F = f(x1, y1)

cs = plt.contourf(X1, Y1, f(X1, Y1))
#plt.contour(X1, Y1, f(X1, Y1), 10)

plt.colorbar(cs)

path = "SwarmData\\"

num_outside_graph = 0
total_runs = 0

#ax.plot_surface(X1, Y1, f(X1, Y1), cmap='jet', alpha=0.8)

ax.set_xlabel('x')
ax.set_ylabel('y')

file_extension = os.path.splitext(file_name)[1]
print(file_extension)
average_total = 0
total_runs = 0

#its swarm data
if file_extension == '.txt':
    ax.set_title(function_name + ' Swarm')
    path = 'SwarmData\\' + file_name
    with open(path) as file:
        lines = file.readlines()

        i = 0
        for line in lines:
            if line[:16] == "solution_found: ":
                total_runs += 1
                solution = line[16:]
                solution = solution.strip()
                solution = solution.strip('[')
                solution = solution.strip()
                solution = solution.strip(']')
                solution = solution.split(' ')
                sol_x = float(solution[0])
                for i in range(len(solution)):
                    if i != 0 and solution[i] != '':
                        sol_y = float(solution[i])
                        break
                #print(sol_x, sol_y)
                if ww_min < sol_x < ww_max and wh_min < sol_y < wh_max:
                    plt.plot(sol_x, sol_y, color='black', marker='o')
                else:
                    num_outside_graph += 1
            if line[:9] == "fitness: ":
                fitness = line[9:]
                fitness_val = float(fitness)
                average_total += fitness_val
                #print(fitness_val)
                #exit()

elif file_extension == '.csv':
    ax.set_title(function_name + ' Evolutionary')
    path = 'EvolutionData\\' + file_name
    with open(path, 'r', newline='') as csvfile:
        csvFile = csv.reader(csvfile)
        next(csvFile)

        for lines in csvFile:
            if lines[5] == '29':
                total_runs += 1
                solution = lines[8]
                solution = solution.strip()
                solution = solution.strip('[')
                solution = solution.strip()
                solution = solution.strip(']')
                solution = solution.split(',')
                #print(solution)
                fitness = float(lines[7])
                average_total += fitness
                sol_x = float(solution[0])
                for i in range(len(solution)):
                    if i != 0 and solution[i] != '':
                        sol_y = float(solution[i])
                        break
                #print(sol_x, sol_y)
                #print(sol_x, sol_y)
                if ww_min < sol_x < ww_max and wh_min < sol_y < wh_max:
                    plt.plot(sol_x, sol_y, color='black', marker='o')
                else:
                    num_outside_graph += 1

else:
    exit()

if num_outside_graph != 0:
    plt.figtext(0.5, 0.03, ('Number of points outside graph: ' + str(num_outside_graph) + '/' + str(total_runs)), style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 3})

#plot the convergance points
for (gx, gy) in zip(global_x ,global_y):
    plt.plot(gx, gy, 'ro')

#exit()  
#plt.savefig((function_name + '.jpg'))
print(average_total / total_runs)
#plt.show()
#plt.close()
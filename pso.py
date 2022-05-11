# CS 420/CS 527 Lab 5: Particle Swarm Optimization 
# Hunter Kitts
# April 2022

from cmath import cos, exp, sqrt
from nbformat import write
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import argparse
import decimal
import winsound

class Particle:
    def __init__(self, position, function):
        self.position = np.array(position)
        self.v = np.array([0,0])
        self.best_position = self.position.copy()
        self.function = function
        
    def update(self, pso):
        self.v = pso.inertia*self.v+pso.phi_1*np.random.random(2)*(np.subtract(self.best_position,self.position))+pso.phi_2*np.random.random(2)*np.subtract(pso.global_best,self.position)
            
        if (self.v[0]**2+self.v[1]**2 > pso.max_vel**2):
            self.v = (pso.max_vel/np.sqrt(self.v[0]**2+self.v[1]**2))*self.v
        
        self.position = np.add(self.position, self.v)
            
        val = pso.Q(self.position, self.function)
        if (val < self.best_val):
            self.best_val = val
            self.best_position = self.position.copy()
        
        if (val < pso.global_best_val):
            pso.global_best_val = val
            pso.global_best = self.position.copy()
        
class PSO:
    #args.num_particles, args.inertia, args.cognition, args.social, 100, 100, 2)
    def __init__(self, num_particles, inertia, phi_1, phi_2, ww_min, ww_max, wh_min, wh_max , max_vel, function):
        self.num_particles = num_particles
        self.inertia = inertia
        self.phi_1 = phi_1
        self.phi_2 = phi_2
        self.ww_min = ww_min
        self.ww_max = ww_max
        self.wh_min = wh_min
        self.wh_max = wh_max
        self.max_vel = max_vel
        self.global_best = np.array([0,0])
        self.global_best_val = None
        self.particles = []
        self.function = function
        
        for i in range(num_particles):
            p = []
            p.append(np.random.uniform(self.ww_min, self.ww_max))
            p.append(np.random.uniform(self.wh_min, self.wh_max))
            particle = Particle(p, self.function)
            particle.best_val = self.Q(p, self.function)
            #print(particle.best_val)
            if (self.global_best_val == None or self.global_best_val > particle.best_val):
                self.global_best_val = particle.best_val
                self.global_best[:] = p[:]
            self.particles.append(particle)
            
    
    def Q(self, position, function):
        x = position[0]
        y = position[1]
        #Rosenbrock | Booth
        if function == "Rosenbrock":
            # Rosenbrock (banana) function
            val=(1-x)**2+100*(y-x**2)**2
        elif function == "Booth":
            # Booth function
            val = (x+2*y-7)**2 + (2*x+y-5)**2
        elif function == "Ackley":
            val = -20 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2*np.pi*y))) + np.e + 20
        elif function == "Beale":
            val = (1.5 - x + x * y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x * y**3)**2
        elif function == "Goldstein_Price":
            val = (1 + (x+y+1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)) * (30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y -36*x*y + 27*y**2))
        elif function == "Bukin":
            val = 100 * np.sqrt(np.abs(y - 0.01*x**2)) + 0.01 * np.abs(x + 10)
        elif function == "Matyas":
            val = 0.26 * (x**2 + y**2) - 0.48*x*y
        elif function == "Levi":
            val = np.sin(3*np.pi*x)**2 + (x - 1)**2 * (1+np.sin(3*np.pi*y)**2)
            + (y-1)**2 *(1+np.sin(2*np.pi*y)**2)
        elif function == "Himmelblau":
            val = (x**2 + y - 11)**2 + (x + y**2 - 7)**2
        elif function == "Three_hump_camel":
            val = 2*x**2 - 1.05*x**4 + (x**6 / 6) + x*y + y**2
        elif function == "Easom":
            val = - np.cos(x)*np.cos(y)*np.exp(-((x-np.pi)**2 + (y-np.pi)**2))
        elif function == "Cross_in_tray":
            val = -0.0001 * (np.abs(np.sin(x)*np.sin(y)*np.exp(np.abs(100 - (np.sqrt(x**2 + y**2)/np.pi)))) + 1)**0.1
        elif function == "Eggholder":
            val = -(y+47)*np.sin(np.sqrt(np.abs((x/2)+(y+47)))) - x*np.sin(np.sqrt(np.abs(x - (y+47))))
        elif function == "Holder":
            val = - np.abs(np.sin(x)*np.cos(y)*np.exp(np.abs(1 - (np.sqrt(x**2 + y**2)/np.pi))))
        elif function == "McCormick":
            val = np.sin(x+y) + (x-y)**2- 1.5*x + 2.5*y + 1
        elif function == "Schaffer_N2":
            val = 0.5 + ((np.sin(x**2 - y**2)**2 - 0.5)/((1+0.001*(x**2 + y**2)**2)))
        elif function == "Schaffer_N4":
            val = 0.5 + ( ((np.cos(np.sin(np.abs(x**2 - y**2)))**2) - 0.5) / ((1 + 0.001*(x**2 + y**2))**2) )
        else:
            print("FUNCTION ERROR EXITING")
            exit()

        return val
    
    def update(self):
        for i in range(self.num_particles):
            p = self.particles[i]
            p.update(self)
            
    def scatter_plot(self):
        x = []
        y = []
        for i in range(self.num_particles):
            x.append(self.particles[i].position[0])
            y.append(self.particles[i].position[1])
        return x,y

class TestsRun:

    def set_defaults(self, args):
        args.num_particles = 40
        args.inertia = 0.5
        args.cognition = 1
        args.social = 1

parser = argparse.ArgumentParser(description="CS 420/CS 527 Lab 5: PSO")
parser.add_argument("--num_particles", default=40, type=int, help="Number of particles")
parser.add_argument("--inertia", default=0.5, type=float, help="Inertia")
parser.add_argument("--cognition", default=1, type=float, help="Cognition parameter")
parser.add_argument("--social", default=1, type=float, help="Social parameter")
parser.add_argument("--function", default="Rosenbrock", type=str, help="Rosenbrock | Booth")
parser.add_argument("--all", default=False, type=bool)
    
args = parser.parse_args()
#name arguments = [num_particles, inertia, cognition, social]
inertia_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8 , 0.9, 1.0]
cog_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8 , 0.9, 1.0,
            1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8 , 1.9, 2.0,
            2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8 , 2.9, 3.0,
            3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8 , 3.9, 4.0,]
social_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8 , 0.9, 1.0, 
            1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8 , 1.9, 2.0,
            2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8 , 2.9, 3.0,
            3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8 , 3.9, 4.0,]


#exit()
if args.all:
    testruns = TestsRun()

    file_str = "data_" + args.function + ".txt"
    file = open(file_str, 'w')

    if args.function == "Rosenbrock":
        ww_min = -1.0
        ww_max = 1.5
        wh_min = -0.5
        wh_max = 2.5
    elif args.function == "Booth":
        ww_min = -10
        ww_max = 10
        wh_min = -10
        wh_max = 10
        #bnd = [[-10, 10]]*2
    elif args.function == "Ackley":
        ww_min = -5
        ww_max = 5
        wh_min = -5
        wh_max = 5
        #bnd = [[-5, 5]]*2
    elif args.function == "Beale":
        ww_min = -4.5
        ww_max = 4.5
        wh_min = -4.5
        wh_max = 4.5
        #bnd = [[-4.5, 4.5]]*2
    elif args.function == "Goldstein_Price":
        ww_min = -2
        ww_max = 2
        wh_min = -2
        wh_max = 2
        #bnd = [[-2, 2]]*2
    elif args.function == "Bukin":
        ww_min = -15
        ww_max = -5
        wh_min = -3
        wh_max = 3
        #bnd = [[-15, -5], [-3, 3]]
    elif args.function == "Matyas":
        ww_min = -10
        ww_max = 10
        wh_min = -10
        wh_max = 10
        #bnd = [[-10, 10]]*2
    elif args.function == "Levi":
        ww_min = -10
        ww_max = 10
        wh_min = -10
        wh_max = 10
        #bnd = [[-10, 10]]*2
    elif args.function == "Himmelblau":
        ww_min = -5
        ww_max = 5
        wh_min = -5
        wh_max = 5
        #bnd = [[-5, 5]]*2
    elif args.function == "Three_hump_camel":
        ww_min = -5
        ww_max = 5
        wh_min = -5
        wh_max = 5
        #bnd = [[-5, 5]]*2
    elif args.function == "Easom":
        ww_min = -100
        ww_max = 100
        wh_min = -100
        wh_max = 100
        #bnd = [[-100, 100]]*2
    elif args.function == "Cross_in_tray":
        ww_min = -10
        ww_max = 10
        wh_min = -10
        wh_max = 10
        #bnd = [[-10, 10]]*2
    elif args.function == "Eggholder":
        ww_min = -512
        ww_max = 512
        wh_min = -512
        wh_max = 512
        #bnd = [[-512, 512]]*2
    elif args.function == "Holder":
        ww_min = -10
        ww_max = 10
        wh_min = -10
        wh_max = 10
        #bnd = [[-10, 10]]*2
    elif args.function == "McCormick":
        ww_min = -1.5
        ww_max = 4
        wh_min = -3
        wh_max = 4
        #bnd = [[-1.5, 4], [-3, 4]]
    elif args.function == "Schaffer_N2":
        ww_min = -100
        ww_max = 100
        wh_min = -100
        wh_max = 100
        #bnd = [[-100, 100]]*2
    elif args.function == "Schaffer_N4":
        ww_min = -100
        ww_max = 100
        wh_min = -100
        wh_max = 100
        #bnd = [[-100, 100]]*2
    else:
        print('Bounds not right')
        exit()    

    for param in range(4):
        testruns.set_defaults(args)

        #change num particles
        if param == 0:
            changing = np.arange(10, 110, 10)
            print('num particles')
        if param == 1:
            changing = inertia_list
            print('inertia')
        if param == 2:
            changing = cog_list
            print('cog')
        if param == 3:
            changing = social_list
            print('social')

        for loop in changing:
            #print('fuck this shit', i)
            if param == 0:
                args.num_particles = loop
                #print(loop)
            if param == 1:
                args.inertia = loop
            if param == 2:
                args.cognition = loop
            if param == 3:
                args.social = loop
            #print(args)

            #do each run 10 times
            for run in range(10):

                # Print all of the command line arguments
                d = vars(args)
                for k in d.keys():
                    if k != "all":
                        file.write(k + str(":") + str(d[k]) + '\n')

                # Create PSO
                # TODO set ww and wh 
                pso = PSO(args.num_particles, args.inertia, args.cognition, args.social, ww_min, ww_max, wh_min, wh_max, 2 , args.function)

                for i in range(1000):
                    pso.update()
                    x,y = pso.scatter_plot()
                    error_x = np.sum([(pso.particles[k].position[0]-pso.global_best[0])**2 for k in range(args.num_particles)])
                    error_y = np.sum([(pso.particles[k].position[1]-pso.global_best[1])**2 for k in range(args.num_particles)])
                    error_x = np.sqrt((1.0/(2*args.num_particles))*error_x)
                    error_y = np.sqrt((1.0/(2*args.num_particles))*error_y)
                    if (error_x < 0.00001 and error_y < 0.00001):
                        break
                
                #print(pso.global_best_val)
                file.write("epoch_stop: " + str(i) + '\n')
                file.write("solution_found: " + str(pso.global_best)+ '\n')
                file.write("fitness: " + str(pso.global_best_val) + '\n')
                file.write('\n')
    file.close()
    winsound.Beep(2500, 1000)

else:
    args = parser.parse_args()
    # Print all of the command line arguments
    d = vars(args)
    for k in d.keys():
        if k != "all":
            print(k + str(":") + str(d[k]))

    # Create PSO
    pso = PSO(args.num_particles, args.inertia, args.cognition, args.social, 100, 100, 2, args.function)

    for i in range(1000):
        pso.update()
        x,y = pso.scatter_plot()
        error_x = np.sum([(pso.particles[k].position[0]-pso.global_best[0])**2 for k in range(args.num_particles)])
        error_y = np.sum([(pso.particles[k].position[1]-pso.global_best[1])**2 for k in range(args.num_particles)])
        error_x = np.sqrt((1.0/(2*args.num_particles))*error_x)
        error_y = np.sqrt((1.0/(2*args.num_particles))*error_y)
        if (error_x < 0.00001 and error_y < 0.00001):
            break

    print("epoch_stop:", i)
    print("solution_found:", pso.global_best)
    print("fitness:", pso.global_best_val)
    print()

from email.errors import FirstHeaderLineIsContinuationDefect
from matplotlib import markers
import numpy as np 
import matplotlib.pyplot as plt
import os
import sys
import argparse
from pathlib import Path

class RunData:
    def __init__(self):
        self.runDict = {
            'C': {'particles': [], 'inertia': [], 'cognition': [], 'social': []},
            'N': {'particles': [], 'inertia': [], 'cognition': [], 'social': []}
        }
        self.ten_runs = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
        self.particles = {10: [], 20: [], 30: [], 40: [], 50: [], 60: [], 70: [], 80: [], 90: [], 100: []}
        self.inertia = {0.1: [], 0.2: [], 0.3: [], 0.4: [], 0.5: [], 0.6: [], 0.7: [], 0.8: [], 0.9: [], 1.0: []}
        self.cognition = {0.1: [], 0.2: [], 0.3: [], 0.4: [], 0.5: [], 0.6: [], 0.7: [], 0.8 : [], 0.9: [], 1.0: [],
                          1.1: [], 1.2: [], 1.3: [], 1.4: [], 1.5: [], 1.6: [], 1.7: [], 1.8 : [], 1.9: [], 2.0: [],
                          2.1: [], 2.2: [], 2.3: [], 2.4: [], 2.5: [], 2.6: [], 2.7: [], 2.8 : [], 2.9: [], 3.0: [],
                          3.1: [], 3.2: [], 3.3: [], 3.4: [], 3.5: [], 3.6: [], 3.7: [], 3.8 : [], 3.9: [], 4.0: []}
        self.social =    {0.1: [], 0.2: [], 0.3: [], 0.4: [], 0.5: [], 0.6: [], 0.7: [], 0.8 : [], 0.9: [], 1.0: [],
                          1.1: [], 1.2: [], 1.3: [], 1.4: [], 1.5: [], 1.6: [], 1.7: [], 1.8 : [], 1.9: [], 2.0: [],
                          2.1: [], 2.2: [], 2.3: [], 2.4: [], 2.5: [], 2.6: [], 2.7: [], 2.8 : [], 2.9: [], 3.0: [],
                          3.1: [], 3.2: [], 3.3: [], 3.4: [], 3.5: [], 3.6: [], 3.7: [], 3.8 : [], 3.9: [], 4.0: []}
        self.particles_line = []
        self.inertia_line = []
        self.cognition_line = []
        self.social_line = []
        self.function_name = ""
    
    def test_converge(self, fitness, function_name):
        self.function_name = function_name
        if function_name == "Rosenbrock":
            if fitness > 1e-10:
                return 'N'
            else:
                return 'C'
        if function_name == "Booth":
            if fitness > 1e-10:
                return 'N'
            else:
                return 'C'
        if function_name == "Ackley":
            if fitness > 1e-10:
                return 'N'
            else:
                return 'C'
        if function_name == "Goldstein-Price":
            if fitness > 3.0000000001:
                return 'N'
            else:
                return 'C'
        if function_name == "Bukin":
            if fitness > 1e-10:
                return 'N'
            else:
                return 'C'
        if function_name == "Levi":
            if fitness > 1e-10:
                return 'N'
            else:
                return 'C'
        if function_name == "Himmelblau":
            if fitness > 1e-10:
                return 'N'
            else:
                return 'C'
        if function_name == "Three-hump camel":
            if fitness > 1e-10:
                return 'N'
            else:
                return 'C'
        if function_name == "Easom":
            if fitness > -1.0000000001 and fitness < -0.9999999999: 
                return 'C'
            else:
                return 'N'
        if function_name == "Cross-in-tray":
            if fitness > -2.0626100001:
                return 'N'
            else:
                return 'C'
        if function_name == "Eggholder":
            if fitness > -959.6407000001:
                return 'N'
            else:
                return 'C'
        if function_name == "Holder":
            if fitness > -19.2085000001:
                return 'N'
            else:
                return 'C'
        if function_name == "McCormick":
            if fitness > -1.9132000001:
                return 'N'
            else:
                return 'C'
        if function_name == "Schaffer N2":
            if fitness > 1e-10:
                return 'N'
            else:
                return 'C'
        if function_name == "Schaffer N4":
            if fitness > 0.2925799:
                return 'N'
            else:
                return 'C'
        if function_name == "Beale":
            if fitness > 1e-10:
                return 'N'
            else:
                return 'C'
        if function_name == "Matyas":
            if fitness > 1e-10:
                return 'N'
            else:
                return 'C'
        else:
            print('function not here')
            exit()
        

    def get_int(self, value):
        value = str(value)
        value = value.split(':')
        return int(value[1])

    def get_float(self, value):
        value = str(value)
        value = value.split(':')
        return float(value[1])

    def get_function(self, value):
        value = str(value)
        value = value.split(':')
        return value[1]

    def get_solution(self, solution):
        solution = str(solution)
        solution = solution.split(':')
        solution = solution[1].strip(']')
        solution = solution[2:]
        solution = solution.strip()
        solution = solution.split(' ')
        #print(solution)
        x = float(solution[0])
        for i in range(len(solution)):
            if i != 0 and solution[i] != '':
                y = float(solution[i])
                break
        solution = [x, y]
        return solution

    def process_test(self, test, i, function_name, parameter):
        particles = self.get_int(test[0])
        inertia = self.get_float(test[1])
        cognition = self.get_float(test[2])
        social = self.get_float(test[3])
        function = self.get_function(test[4])
        epoch_stop = self.get_int(test[5])
        solution = self.get_solution(test[6])
        fitness = self.get_float(test[7])
        #print(fitness)
        convergance = self.test_converge(fitness, function_name)        
        test = [particles, inertia, cognition, social, epoch_stop, solution, fitness]
       
        if convergance == 'C':
            self.runDict['C'][parameter].append(test)
        elif convergance == 'N':
            self.runDict['N'][parameter].append(test)

    def store_particles_c(self):
        convergance = self.runDict['C']
        #print(self.runDict['N']['particles'])
        for key, value in convergance.items():
            if key == 'particles':
                test_list = value
                for i in test_list:
                    test = i
                    self.particles[test[0]].append(test[4])
    
    def plot_particles_c(self):
        particles = []
        for key, value in self.particles.items():
            y = np.asarray(value)
            mean = np.mean(y)
            particles.append(y)
            self.particles_line.append(mean)
        x = np.asarray(range(1, 11))
        plt.plot(x, self.particles_line, marker='o')
        plt.boxplot(particles, labels= ['10', '20', '30', '40', '50', '60', '70', '80', '90', '100'])
        title = " - Converged - Epoch vs Number of Particles"
        whole_title = self.function_name + title
        fig_title = self.function_name + '_C_num_particles.jpg'
        plt.title(whole_title)
        plt.ylabel('Epoch to Converge')
        plt.xlabel('Number of Particles')
        plt.savefig(fig_title)
        plt.close()

    def store_inertia_c(self):
        convergance = self.runDict['C']
        for key, value in convergance.items():
            if key == 'inertia':
                test_list = value
                for i in test_list:
                    test = i
                    self.inertia[test[1]].append(test[4])
    
    def plot_inertia_c(self):
        inertia = []
        for key, value in self.inertia.items():
            y = np.asarray(value)
            if len(y) != 0:
                mean = np.mean(y)
                self.inertia_line.append(mean)
            else:
                self.inertia_line.append(0)
            inertia.append(y)   
        x = np.asarray(range(1, 11))
        plt.plot(x, self.inertia_line, marker='o')
        plt.boxplot(inertia, labels= ['0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1.0'])
        title = " - Converged - Epoch vs Inertia"
        whole_title = self.function_name + title
        plt.title(whole_title)
        plt.ylabel('Epoch to Converge')
        plt.xlabel('Inertia')
        fig_title = self.function_name + '_C_inertia.jpg'
        plt.savefig(fig_title)
        plt.close()

    def store_cognition_c(self):
        convergance = self.runDict['C']
        for key, value in convergance.items():
            if key == 'cognition':
                test_list = value
                for i in test_list:
                    test = i
                    self.cognition[test[2]].append(test[4])

    def plot_cognition_c(self):
        cognition = []
        for key, value in self.cognition.items():
            y = np.asarray(value)
            if len(y) != 0:
                mean = np.mean(y)
                self.cognition_line.append(mean)
            else:
                self.cognition_line.append(0)
            cognition.append(y)
        x = np.asarray(range(1, 41))
        plt.figure(figsize=(14, 6))
        plt.plot(x, self.cognition_line, marker='o')
        plt.boxplot(cognition, labels= [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8 , 0.9, 1.0,
                1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8 , 1.9, 2.0,
                2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8 , 2.9, 3.0,
                3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8 , 3.9, 4.0])
        title = " - Converged - Epoch vs Cognition"
        whole_title = self.function_name + title
        fig_title = self.function_name + '_C_cognition.jpg'
        plt.title(whole_title)
        plt.ylabel('Epoch to Converge')
        plt.xlabel('Cognition')
        plt.savefig(fig_title)
        plt.close()
    
    def store_social_c(self):
        convergance = self.runDict['C']
        for key, value in convergance.items():
            if key == 'social':
                test_list = value
                for i in test_list:
                    test = i
                    self.social[test[3]].append(test[4])

    def plot_social_c(self):
        social = []
        for key, value in self.social.items():
            y = np.asarray(value)
            if len(y) != 0:
                mean = np.mean(y)
                self.social_line.append(mean)
            else:
                self.social_line.append(0)
            social.append(y)
        
        x = np.asarray(range(1, 41))
        plt.figure(figsize=(14, 6))
        plt.plot(x, self.social_line, marker='o')
        plt.boxplot(social, labels= [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8 , 0.9, 1.0,
                1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8 , 1.9, 2.0,
                2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8 , 2.9, 3.0,
                3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8 , 3.9, 4.0])
        title = " - Converged - Epoch vs Social'"
        whole_title = self.function_name + title
        fig_title = self.function_name + '_C_social.jpg'
        plt.title(whole_title)
        plt.ylabel('Epoch to Converge')
        plt.xlabel('Social')
        plt.savefig(fig_title)
        plt.close()

    def write_num_cn(self):
        path = 'convergance_data.txt'

        file = open(path, 'a+')

        #get number of convergance
        cparticles = 'particles: ' + str(len(self.runDict['C']['particles'])) + '\n'
        cinertia = 'inertia: ' + str(len(self.runDict['C']['inertia'])) + '\n'
        ccognition = 'cognition: ' + str(len(self.runDict['C']['cognition'])) + '\n'
        csocial = 'social: ' + str(len(self.runDict['C']['social'])) + '\n'
        nparticles = 'particles: ' + str(len(self.runDict['N']['particles'])) + '\n'
        ninertia = 'inertia: ' + str(len(self.runDict['N']['inertia'])) + '\n'
        ncognition = 'cognition: ' + str(len(self.runDict['N']['cognition'])) + '\n'
        nsocial = 'social: ' + str(len(self.runDict['N']['social'])) + '\n'
        func = self.function_name + '\n'
        
        file.write(func)
        file.write('Converged\n')
        file.write(cparticles)
        file.write(cinertia)
        file.write(ccognition)
        file.write(csocial)
        file.write('NotConverged\n')
        file.write(nparticles)
        file.write(ninertia)
        file.write(ncognition)
        file.write(nsocial)
        file.write('\n')



if __name__ == '__main__':
    path = 'SwarmData/'

    parser = argparse.ArgumentParser(description="Plot Swarm Data")
    parser.add_argument("--file",  required=True, help="name of file", type=str)
    args = parser.parse_args() 

    filename = args.file
    function_name = args.file.strip('.txt')
    function_name = function_name.split('_')
    temp = function_name[1:]
    function_name = ""
    for words in temp:
        function_name += words + ' '
    function_name = function_name.strip()
        
    #print(function_name)
    #exit()
    path += args.file

    if os.path.exists(path):
        file = open(path, 'r')
        dc = RunData()
        lines = file.readlines()
        test = []
        i = 0
        j = 1
        for line in lines:
            test.append(line.strip())
            if(len(test)) == 9:
                if j <= 100:
                    parameter = "particles"
                elif j > 100 and j <= 200:
                    parameter = "inertia"
                elif j > 200 and j <= 600:
                    parameter = "cognition"
                elif j > 600 and j <= 1000:
                    parameter = "social"
                dc.process_test(test, i, function_name, parameter)
                #print(test)
                i += 1
                j += 1
                test = []
                if(i > 9): i = 0
        dc.store_particles_c()
        dc.plot_particles_c()

        dc.store_inertia_c()
        dc.plot_inertia_c()

        dc.store_cognition_c()
        dc.plot_cognition_c()

        dc.store_social_c()
        dc.plot_social_c()

        dc.write_num_cn()

    else:
        print("file doesn't exists")
        exit()
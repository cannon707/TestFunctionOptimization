import glob
import numpy
import pandas as pd
import csv
import os
import sys
import argparse
import numpy as np

writeFile = 'evo_convergance_data.txt'
dataPath = 'EvolutionData\\'

csvFiles = glob.glob(dataPath + "/*.csv")
conv_file = open(writeFile, 'a+')

for i in csvFiles:
    file_name = i[14:]
    file_name = file_name.replace('_datafile.csv', "")
    file_name = file_name.split('_')

    if len(file_name) > 1:
        if file_name[0] == "Cross":
            function_name = "Cross-in-tray"
        elif file_name[0] == "Goldstein":
            function_name = "Goldstein-Price"
        elif file_name[0] == "Three":
            function_name = "Three-hump camel"
        elif file_name[0] == "Schaffer" and file_name[1] == "N2":
            function_name = "Schaffer N2"
        elif file_name[0] == "Schaffer" and file_name[1] == "N4":
            function_name = "Schaffer N4"
    else:
        function_name = file_name[0]

    with open(i, mode='r') as file:
        csvFile = csv.reader(file)
        num_estimated_converge = 0
        total_runs = 0
        #print(function_name)

        for lines in csvFile:
            if lines[5] == '29':
                total_runs += 1
                #n = float(lines[0])
                #p_m = float(lines[1])
                #p_c = float(lines[2])
                #tourn = float(lines[3])
                #check filename to do comparison
                if function_name == "Ackley":
                    comp = 0
                    #check lines[7]
                    if (comp - 0.1) < float(lines[7]) < (comp + 0.1):
                        num_estimated_converge += 1
                elif function_name == "Beale":
                    comp = 0
                    #check lines[7]
                    if (comp - 0.1) < float(lines[7]) < (comp + 0.1):
                        num_estimated_converge += 1
                elif function_name == "Booth":
                    comp = 0
                    #check lines[7]
                    if (comp - 0.1) < float(lines[7]) < (comp + 0.1):
                        num_estimated_converge += 1
                elif function_name == "Three-hump camel":
                    comp = 0
                    if (comp - 0.1) < float(lines[7]) < (comp + 0.1):
                        num_estimated_converge += 1
                elif function_name == "Bukin":
                    comp = 0
                    #check lines[7]
                    if (comp - 0.1) < float(lines[7]) < (comp + 0.1):
                        num_estimated_converge += 1
                elif function_name == "Cross-in-tray":
                    comp = -2.062
                    #check lines[7]
                    if (comp - 0.0009) < float(lines[7]) < (comp + 0.0009):
                        num_estimated_converge += 1
                elif function_name == "Easom":
                    comp = -1
                    #check lines[7]
                    if (comp - 0.1) < float(lines[7]) < (comp + 0.1):
                        num_estimated_converge += 1
                elif function_name == "Eggholder":
                    comp = -959.6407
                    #check lines[7]
                    if (comp - 0.9) < float(lines[7]) < (comp + 0.9):
                        num_estimated_converge += 1
                elif function_name == "Goldstein-Price":
                    comp = 3
                    #check lines[7]
                    if (comp - 0.1) < float(lines[7]) < (comp + 0.1):
                        num_estimated_converge += 1
                elif function_name == "Himmelblau":
                    comp = 0
                    #check lines[7]
                    if (comp - 0.1) < float(lines[7]) < (comp + 0.1):
                        num_estimated_converge += 1
                elif function_name == "Holder":
                    comp = -19.2085
                    #check lines[7]
                    if (comp - 0.1) < float(lines[7]) < (comp + 0.1):
                        num_estimated_converge += 1
                elif function_name == "Levi":
                    comp = 0
                    #check lines[7]
                    if (comp - 0.1) < float(lines[7]) < (comp + 0.1):
                        num_estimated_converge += 1
                elif function_name == "Matyas":
                    comp = 0
                    #check lines[7]
                    if (comp - 0.1) < float(lines[7]) < (comp + 0.1):
                        num_estimated_converge += 1
                elif function_name == "McCormick":
                    comp = -1.9133
                    #check lines[7]
                    if (comp - 0.01) < float(lines[7]) < (comp + 0.01):
                        num_estimated_converge += 1
                elif function_name == "Rosenbrock":
                    comp = 0
                    #check lines[7]
                    if (comp - 0.1) < float(lines[7]) < (comp + 0.1):
                        num_estimated_converge += 1
                elif function_name == "Schaffer N2":
                    comp = 0
                    #check lines[7]
                    if (comp - 0.1) < float(lines[7]) < (comp + 0.1):
                        num_estimated_converge += 1
                elif function_name == "Schaffer N4":
                    comp = 0.292579
                    #check lines[7]
                    if (comp - 0.001) < float(lines[7]) < (comp + 0.001):
                        num_estimated_converge += 1

        conv_file.write(function_name + '\n')
        conv_file.write('converged\n')
        conv_file.write(str(num_estimated_converge) + '\n')
        conv_file.write('notConverged\n')
        conv_file.write(str(total_runs - num_estimated_converge) + '\n')
        conv_file.write('\n') 
    






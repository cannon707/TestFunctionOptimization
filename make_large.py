import glob
import numpy
import pandas as pd
import csv
import os
import sys
import argparse
import numpy as np

path = "lab2_data\\"
max_generations = 24
# func = ["Rosenbrock", "Booth", "Ackley", "Beale", "Goldstein_Price", "Bukin",
#         "Matyas", "Levi", "Himmelblau", "Three_hump_camel", "Easom", "Cross_in_tray",
#         "Eggholder", "Holder", "McCormick", "Schaffer_N2", "Schaffer_N4" ]

parser = argparse.ArgumentParser(description="Bring all data together")
parser.add_argument("--file",  required=True, help="name of file", type=str)
args = parser.parse_args() 
function_name = args.file
#print(function_name)

if function_name == "Rosenbrock":
    compare_fitness = 0
elif function_name == "Booth":
    compare_fitness = 0
elif function_name == "Ackley":
    compare_fitness = 0
elif function_name == "Beale":
    compare_fitness = 0
elif function_name == "Goldstein_Price":
    compare_fitness = 3
elif function_name == "Himmelblau":
    compare_fitness = 0
elif function_name == "Bukin":
    compare_fitness = 0
elif function_name == "Matyas":
    compare_fitness = 0
elif function_name == "Levi":
    compare_fitness = 0
elif function_name == "Three_hump_camel":
    compare_fitness = 0
elif function_name == "Easom":
    compare_fitness = -1
elif function_name == "Cross_in_tray":
    compare_fitness = -2.06261
elif function_name == "Eggholder":
    compare_fitness = -959.6407
elif function_name == "Holder":
    compare_fitness = 19.2085
elif function_name == "McCormick":
    compare_fitness = -1.9133
elif function_name == "Schaffer_N2":
    compare_fitness = 0
elif function_name == "Schaffer_N4":
    compare_fitness = 0.292579
else:
    print('function not here')
    exit()

#print(function_name)
path += function_name
#print(path)

fields = ['N', 'p_m', 'p_c', 'tournament_size', 'iteration',
        'generation', 'average_fitness', 'best_fitness',
        'best_genome', 'solution_found', 'num_solutions_found',
        'diversity_metric']
files = glob.glob(path + "/*.csv")
master_file_name = function_name + '_datafile.csv'

with open(master_file_name, 'w', newline='') as csvfile:
    master_writer = csv.writer(csvfile)
    master_writer.writerow(fields)

    current_row = 0

    for i in files:
        #print(i)
        s = i.replace(function_name, "junk")
        s = s.split('_',1)[1]
        s = s.strip('.csv')
        s = s.split('_')

        n = int(s[1])
        pm = float(s[2])
        pc = float(s[3])
        tournament_size = int(s[4])
        iteration = int(s[5])
        # print(function_name)
        # print(n)
        # print(pc)
        # print(tournament_size)
        # print(iteration)

        with open(i, mode='r') as file:
            
            csvFile = csv.reader(file)

            for i in range(30):
                skip = next(csvFile)
                index = 0
                avg_fitness = 0
                fitness_total = 0
                best_fitness = 100000000000
                max_genome = 0
                best_genome = []
                solution_found = 0
                num_solutions = 0

                for lines in csvFile:
                    #get values from file
                    cur_genome = 0
                    step = int(lines[0])
                    fitness = float(lines[1])
                    genome_str = lines[2]
                    genome_str = genome_str.strip()
                    genome_str = genome_str.strip('[')
                    genome_str = genome_str.strip(']')
                    genome_str = genome_str.split()
                    genome = []
                    for i in genome_str:
                        genome.append(float(i))
                    
                    #to get average fitness add them up in total
                    fitness_total += fitness

                    #check for best_fitness
                    #compare to compare_fitness
                    tmp = np.abs(fitness - (compare_fitness))
                    if tmp <= best_fitness:
                        best_fitness = fitness
                        best_genome = genome
    
                    if (compare_fitness - 0.0000000001) < fitness < compare_fitness + 0.0000000001:
                        solution_found = 1
                        num_solutions += 1
                    index += 1
                    if index == n:
                        break
                avg_fitness = fitness_total / n
                #print(avg_fitness)
                #exit()
                fields = ['N', 'p_m', 'p_c', 'tournament_size', 'iteration',
                        'generation', 'average_fitness', 'best_fitness',
                        'best_genome', 'solution_found', 'num_solutions_found',
                        'diversity_metric']
                fields = [n, pm, pc, tournament_size, iteration,
                        step, avg_fitness, best_fitness,
                        best_genome, solution_found, num_solutions,
                        0]

                master_writer.writerow(fields)
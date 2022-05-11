# CS 420/CS 527 Lab 2: Genetic Algorithms in LEAP 
# Author: Catherine Schuman
# February 2022

import os
import numpy as np
from toolz import pipe

from leap_ec import Individual, context, test_env_var
from leap_ec import ops, probe, util
from leap_ec.decoder import IdentityDecoder
from leap_ec.binary_rep.initializers import create_binary_sequence
from leap_ec.binary_rep.ops import mutate_bitflip
from leap_ec.binary_rep.problems import ScalarProblem
#from leap_ec.binary_rep.initializers import create_real_vector
from leap_ec.distrib import DistributedIndividual
from leap_ec.decoder import IdentityDecoder
from leap_ec.real_rep.initializers import create_real_vector
import argparse
import sys

# Implementation of a custom problem
class Lab2Problem(ScalarProblem):
    def __init__(self, func):
        super().__init__(maximize=False)
        self.func = func
        
    def evaluate(self, ind):
        #print(ind)
        x = ind[0]
        y = ind[1]
        if self.func == "Rosenbrock":
            # Rosenbrock (banana) function
            val = (1-x)**2+100*(y-x**2)**2
        elif self.func == "Booth":
            # Booth function
            val = (x+2*y-7)**2 + (2*x+y-5)**2
        elif self.func == "Ackley":
            val = -20 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2*np.pi*y))) + np.e + 20
        elif self.func == "Beale":
            val = (1.5 - x + x * y)**2 + (2.25 - x + x*y**2)**2 + (2.625 - x + x * y**3)**2
        elif self.func == "Goldstein_Price":
            val = (1 + (x+y+1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)) * (30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y -36*x*y + 27*y**2))
        elif self.func == "Bukin":
            val = 100 * np.sqrt(np.abs(y - 0.01*x**2)) + 0.01 * np.abs(x + 10)
        elif self.func == "Matyas":
            val = 0.26 * (x**2 + y**2) - 0.48*x*y
        elif self.func == "Levi":
            val = np.sin(3*np.pi*x)**2 + (x - 1)**2 * (1+np.sin(3*np.pi*y)**2)
            + (y-1)**2 *(1+np.sin(2*np.pi*y)**2)
        elif self.func == "Himmelblau":
            val = (x**2 + y - 11)**2 + (x + y**2 - 7)**2
        elif self.func == "Three_hump_camel":
            val = 2*x**2 - 1.05*x**4 + (x**6 / 6) + x*y + y**2
        elif self.func == "Easom":
            val = - np.cos(x)*np.cos(y)*np.exp(-((x-np.pi)**2 + (y-np.pi)**2))
        elif self.func == "Cross_in_tray":
            val = -0.0001 * (np.abs(np.sin(x)*np.sin(y)*np.exp(np.abs(100 - (np.sqrt(x**2 + y**2)/np.pi)))) + 1)**0.1
        elif self.func == "Eggholder":
            val = -(y+47)*np.sin(np.sqrt(np.abs((x/2)+(y+47)))) - x*np.sin(np.sqrt(np.abs(x - (y+47))))
        elif self.func == "Holder":
            val = - np.abs(np.sin(x)*np.cos(y)*np.exp(np.abs(1 - (np.sqrt(x**2 + y**2)/np.pi))))
        elif self.func == "McCormick":
            val = np.sin(x+y) + (x-y)**2- 1.5*x + 2.5*y + 1
        elif self.func == "Schaffer_N2":
            val = 0.5 + ((np.sin(x**2 - y**2)**2 - 0.5)/((1+0.001*(x**2 + y**2)**2)))
        elif self.func == "Schaffer_N4":
            val = 0.5 + ( ((np.cos(np.sin(np.abs(x**2 - y**2)))**2) - 0.5) / ((1 + 0.001*(x**2 + y**2))**2) )
        else:
            print("FUNCTION ERROR EXITING")
            exit()
        #print(val)
        return val

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Lab 2: Genetic Algorithms")
    parser.add_argument("--n", default=50, help="population size", type=int)
    parser.add_argument("--p_m", default=0.01, help="probability of mutation", type=float)
    parser.add_argument("--p_c", default=0.3, help="probability of crossover", type=float)
    parser.add_argument("--trn_size", default=2, help="tournament size", type=int)
    parser.add_argument("--csv_output", required=True, help="csv output file name", type=str)
    parser.add_argument("--function", default="Rosenbrock", help="name of optimization function", type=str)
    args = parser.parse_args()    

    N = args.n
    p_m = args.p_m
    p_c = args.p_c
    trn_size = args.trn_size
    func = args.function
    if func == "Rosenbrock":
        bnd = [[-1.5, 1.5], [-0.5, 0.5]]
    elif func == "Booth":
        bnd = [[-10, 10]]*2
    elif func == "Ackley":
        bnd = [[-5, 5]]*2
    elif func == "Beale":
        bnd = [[-4.5, 4.5]]*2
    elif func == "Goldstein_Price":
        bnd = [[-2, 2]]*2
    elif func == "Bukin":
        bnd = [[-15, -5], [-3, 3]]
    elif func == "Matyas":
        bnd = [[-10, 10]]*2
    elif func == "Levi":
        bnd = [[-10, 10]]*2
    elif func == "Himmelblau":
        bnd = [[-5, 5]]*2
    elif func == "Three_hump_camel":
        bnd = [[-5, 5]]*2
    elif func == "Easom":
        bnd = [[-100, 100]]*2
    elif func == "Cross_in_tray":
        bnd = [[-10, 10]]*2
    elif func == "Eggholder":
        bnd = [[-512, 512]]*2
    elif func == "Holder":
        bnd = [[-10, 10]]*2
    elif func == "McCormick":
        bnd = [[-1.5, 4], [-3, 4]]
    elif func == "Schaffer_N2":
        bnd = [[-100, 100]]*2
    elif func == "Schaffer_N4":
        bnd = [[-100, 100]]*2
    else:
        print('Bounds not right')
        exit()


    max_generation = 30
    l = 40
    parents = DistributedIndividual.create_population(N,
                                           initialize=create_real_vector(bounds=bnd),
                                           decoder=IdentityDecoder(),
                                           problem=Lab2Problem(func))

    # Evaluate initial population
    parents = Individual.evaluate_population(parents)

    generation_counter = util.inc_generation()
    out_f = open(args.csv_output, "w")
    while generation_counter.generation() < max_generation:
        offspring = pipe(parents,
                         ops.tournament_selection(k=trn_size),
                         ops.clone,
                         mutate_bitflip(probability=p_m),
                         ops.uniform_crossover(p_xover=p_c),
                         ops.evaluate,
                         ops.pool(size=len(parents)),  # accumulate offspring
                         probe.AttributesCSVProbe(stream=out_f, do_fitness=True, do_genome=True)
                        )
        parents = offspring
        generation_counter()  # increment to the next generation

    out_f.close()

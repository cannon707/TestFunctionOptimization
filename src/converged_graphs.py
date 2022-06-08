import glob
import numpy
import pandas as pd
import csv
import os
import sys
import argparse
import numpy as np
from email.errors import FirstHeaderLineIsContinuationDefect
import numpy as np 
import matplotlib.pyplot as plt
import os
import sys
import argparse
from pathlib import Path

swarm_convergance = 'convergance_data.txt'

swarm_dict = {"Ackley": [[],[]],
              "Beale": [[],[]],
              "Booth": [[],[]],
              "Bukin": [[],[]],
              "Cross-in-tray": [[],[]],
              "Easom": [[],[]],
              "Eggholder": [[],[]],
              "Goldstein-Price": [[],[]],
              "Himmelblau": [[],[]],
              "Holder": [[],[]],
              "Levi": [[],[]],
              "Matyas": [[],[]],
              "McCormick": [[],[]],
              "Rosenbrock": [[],[]],              
              "Schaffer N2": [[],[]],
              "Schaffer N4": [[],[]],
              "Three-hump camel": [[],[]],}


swarm = open(swarm_convergance, 'r')
swarm_lines = swarm.readlines()

for i in range(17):
    j = i*12
    cur = swarm_lines[j].strip()
    if cur in swarm_dict.keys():
        result = swarm_dict.get(cur)
        j += 2
        particles = swarm_lines[j].strip()
        particles = particles.replace('particles: ', "")
        result[0].append(int(particles))
        j += 1
        inertia = swarm_lines[j].strip()
        inertia = inertia.replace('inertia: ', "")
        result[0].append(int(inertia))
        j += 1
        cognition = swarm_lines[j].strip()
        cognition = cognition.replace('cognition: ', "")
        result[0].append(int(cognition))
        j += 1
        social = swarm_lines[j].strip()
        social = social.replace('social: ', "")
        result[0].append(int(social))
        j += 2
        particles = swarm_lines[j].strip()
        particles = particles.replace('particles: ', "")
        result[1].append(int(particles))
        j += 1
        inertia = swarm_lines[j].strip()
        inertia = inertia.replace('inertia: ', "")
        result[1].append(int(inertia))
        j += 1
        cognition = swarm_lines[j].strip()
        cognition = cognition.replace('cognition: ', "")
        result[1].append(int(cognition))
        j += 1
        social = swarm_lines[j].strip()
        social = social.replace('social: ', "")
        result[1].append(int(social))
        
#print(swarm_dict)
#print()

evol_dict = {"Ackley": [],
              "Beale": [],
              "Booth": [],
              "Bukin": [],
              "Cross-in-tray": [],
              "Easom": [],
              "Eggholder": [],
              "Goldstein-Price": [],
              "Himmelblau": [],
              "Holder": [],
              "Levi": [],
              "Matyas": [],
              "McCormick": [],
              "Rosenbrock": [],              
              "Schaffer N2": [],
              "Schaffer N4": [],
              "Three-hump camel": [],}

evolution_convergance = 'evo_convergance_data.txt'
evol = open(evolution_convergance, 'r')
evol_lines = evol.readlines()

for i in range(17):
    j = i*6
    #print(j)
    cur = evol_lines[j].strip()
    if cur in evol_dict.keys():
        result = evol_dict.get(cur)
        j += 2
        converged = evol_lines[j].strip()
        #print(converged)
        result.append(int(converged))
        j += 2
        notConverged = evol_lines[j].strip()
        #print(notConverged)
        result.append(int(notConverged))

#rint(evol_dict)



#create bar plot
#create bar graph for number of converged
con_name = []
con_total = []

for i in swarm_dict:
    #print(i, swarm_dict[i])
    con_name.append(i)
    total_converged = 0
    for j in swarm_dict[i][0]:
        total_converged += j
    con_total.append(total_converged)

print("Particle Swarm")
print(con_total)
plt.figure(figsize = (10, 10))
plt.xticks(rotation=90)
plt.bar(con_name, con_total, width=0.4)
plt.title('Particle Swarm - Solutions')
plt.xlabel('Optimization Function')
plt.ylabel('Number of Solutions Found')
plt.tight_layout()
plt.figtext(0.07, 0.98, ('Total Tests: 1000'), style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 3})
plt.savefig('ParticleSwarmSolutions.jpg')
plt.close()

con_name = []
con_total = []

for i in evol_dict:
    con_name.append(i)
    total_converged = evol_dict[i][0]
    con_total.append(total_converged)

#print(evol_dict)
print("Evolutionary Algorithm")
print(con_total)
plt.figure(figsize = (10, 10))
plt.xticks(rotation=90)
plt.bar(con_name, con_total, width=0.4)
plt.title('Evolutionary Algorithm - Solutions')
plt.xlabel('Optimization Function')
plt.ylabel('Number of Solutions Found')
plt.tight_layout()
plt.figtext(0.07, 0.98, ('Total Tests: 768'), style='italic',
        bbox={'facecolor': 'red', 'alpha': 0.5, 'pad': 3})
plt.savefig('EvolutionaryAlgorithmSolutions.jpg')
#plt.show()
plt.close()
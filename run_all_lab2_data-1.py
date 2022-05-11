import os
import sys
import winsound

N = [25, 50, 75, 100]
p_m = [0, 0.01, 0.03, 0.05]
p_c = [0, 0.1, 0.3, 0.5]
trn_size = [2, 3, 4, 5]
func = ["McCormick"]
# func = ["Rosenbrock", "Booth", "Ackley", "Beale", "Goldstein_Price", "Bukin",
#         "Matyas", "Levi", "Himmelblau", "Three_hump_camel", "Easom", "Cross_in_tray",
#         "Eggholder", "Holder", "McCormick", "Schaffer_N2", "Schaffer_N4" ]

for n in N:
    for pm in p_m:
        for pc in p_c:
            for ts in trn_size:
                for f in func:
                    for i in range(3):
                        command = "python lab2.py --n " + str(n) + " --p_m " + str(pm) + " --p_c " + str(pc) + " --trn_size " + str(ts) + " --csv_output lab2_data/" + str(f) + "/" + str(f) + "_" +str(n) + "_" + str(pm) + "_" + str(pc) + "_" + str(ts) + "_" + str(i) + ".csv" + " --function " + str(f)
                        os.system(command)
    winsound.Beep(2500, 1000)
winsound.Beep(2500, 5000)

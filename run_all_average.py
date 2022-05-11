import os
commands_list = [
"python create_contor.py --function Ackley --path data_Ackley.txt",
"python create_contor.py --function Beale --path data_Beale.txt",
"python create_contor.py --function Booth --path data_Booth.txt",
"python create_contor.py --function Bukin --path data_Bukin.txt",
"python create_contor.py --function Cross_in_tray --path data_Cross-in-tray.txt",
"python create_contor.py --function Easom --path data_Easom.txt",
"python create_contor.py --function Eggholder --path data_Eggholder.txt",
"python create_contor.py --function Goldstein_Price --path data_Goldstein-Price.txt",
"python create_contor.py --function Himmelblau --path data_Himmelblau.txt",
"python create_contor.py --function Holder --path data_Holder.txt",
"python create_contor.py --function Levi --path data_Levi.txt",
"python create_contor.py --function Matyas --path data_Matyas.txt",
"python create_contor.py --function McCormick --path data_McCormick.txt",
"python create_contor.py --function Rosenbrock --path data_Rosenbrock.txt",
"python create_contor.py --function Schaffer_N2 --path data_Schaffer_N2.txt",
"python create_contor.py --function Schaffer_N4 --path data_Schaffer_N4.txt",
"python create_contor.py --function Three_hump_camel --path data_Three-hump_camel.txt"
]


for i in commands_list:
    os.system(i)
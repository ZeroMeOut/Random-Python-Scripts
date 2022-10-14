import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mc_example = {'A': [0.36, 0, 0, 0, 1],
              'B': [0.64, 0.56, 0, 0, 0],
              'C': [0, 0.44, 0.76, 0, 0],
              'D': [0, 0, 0.24, 0.96, 0],
              'E': [0, 0, 0, 0.04, 0]
              }

mc = pd.DataFrame(data=mc_example, index=['A', 'B', 'C', 'D', 'E'])

art_sim = [mc.iloc[0].index[0]]
art = np.random.choice(mc.iloc[0].index, p=mc.iloc[0])
art_sim.append(art)
userInput = int(input("Enter a number: "))

while len(art_sim) < userInput:
    art = np.random.choice(mc.iloc[mc.index.get_loc(art)].index, p=mc.iloc[mc.index.get_loc(art)])
    art_sim.append(art)

print(art_sim)
print("\n" + "A = " + str(art_sim.count('A')) +
      "\n" + "B = " + str(art_sim.count('B')) +
      "\n" + "C = " + str(art_sim.count('C')) +
      "\n" + "D = " + str(art_sim.count('D')) +
      "\n" + "E = " + str(art_sim.count('E'))
      )

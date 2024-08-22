import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

no_of_trials = 1000
probability_per_trial = {}

for no_of_people in range(2, 80):
    people_having_same_birthday = 0
    for n in range(no_of_trials):
        random_birthday = np.random.randint(low = 1, high = 365, size = no_of_people)
        unique_birthday = np.unique(random_birthday)
        if no_of_people > len(unique_birthday):
            people_having_same_birthday += 1
    probability_per_trial[no_of_people] = people_having_same_birthday/no_of_trials


prob_series = pd.Series(probability_per_trial)

x = prob_series.index
y = prob_series.values*100


plt.plot(x,y)
plt.xlabel("No of people")
plt.ylabel("Probability of at least one common birthday ")
for i in prob_series.index:
    if i%8 == 0 and i<=50:
        plt.axhline(y=y[i],color='black',linestyle='-', linewidth = 0.5)
        hline_txt = 'N=' + str(i) + ' | P=' + str(prob_series[i])
        plt.text(4,y[i],hline_txt, fontsize = 10)
#plt.xticks()
plt.show()





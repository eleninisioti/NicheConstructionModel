from numpy.random import normal
import numpy
import matplotlib.pyplot as plt
# check if you can evolve with very low evolvability

start= 125
add = 11.5
N=25
for i in range(N):
    next_num  = start + add
    start = next_num
    print(next_num)

mutation = 0.005
generations = 500
mu_values = [0]*500
keep_mean = []
for gen in range(generations):

    # choose the half fittest for reproduction
    sorted_mu = list(numpy.argsort(mu_values))
    to_reproduce = sorted_mu[int(len(mu_values)/2):]
    new_mu_values = []
    for agent_idx, mu in enumerate(mu_values):
        if agent_idx in to_reproduce:
            new_mu_values.append(mu + normal(0, mutation))
            new_mu_values.append(mu + normal(0, mutation))
    mu_values = new_mu_values
    keep_mean.append(numpy.mean(mu_values))

plt.plot(range(generations), keep_mean)
plt.show()





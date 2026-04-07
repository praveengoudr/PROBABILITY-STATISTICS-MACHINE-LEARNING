import numpy as np

data = np.array([1,3,5,7,9])

print("Mean:", np.mean(data))
print("Variance:", np.var(data))
print("Std Dev:", np.std(data))

# Probability example
# Coin toss simulation
trials = 10000
heads = np.random.binomial(3, 0.5, trials)
prob_2_heads = np.sum(heads == 2) / trials

print("Probability of exactly 2 heads:", prob_2_heads)

#%% Import and GCF function
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def gcf(nums):
    """Returns the greatest common factor (GCF) of two natural numbers provided as a list
    or tuple"""
    a = nums[0]
    b = nums[1]
    # Both numbers should be nonnegative
    if a < 0 or b < 0:
        raise Exception('Both numbers should be nonnegative')
    
    # Both numbers should be integers
    if a % 1 != 0 or b % 1 != 0:
        raise Exception('Both numbers should be integers')
    
    # Define big and little
    big = max(a, b)
    little = min(a, b)
    
    # If either is 0, return zero
    if big * little == 0: return 0
    
    # Otherwise, if they're the same, return a
    elif big == little: return a
    
    # Otherwise, recurse
    return gcf([big - little, little])

#%% Simulate for one choice of bounds
# Set up simulation
np.random.seed(314)
n_sims = 100000

# Lower and upper bounds on random integers
lower = 1
upper = 10

# Generate random integers between (inclusive) specified bounds
rand_ints = np.random.randint(low = lower, high = upper + 1, size = (n_sims, 2))

# Calculate GCF of each pair of numbers to check coprimality
gcf_list = [gcf(x) for x in rand_ints.tolist()]
coprime_list = [x == 1 for x in gcf_list]

# What is the probability that two randomly drawn natural numbers in range are coprime?
prob_coprime = np.mean(coprime_list)
print('Probability of drawing two coprime integers:', prob_coprime)

# That probability should be approximately 6 over pi-squared, so estimate pi
pi_est = math.sqrt(6 / prob_coprime)
print('Estimate of pi:', pi_est)

#%% Test for a number of different choices of upper bound
np.random.seed(314)
n_sims = 100000
lower = 1

smallest_upper_bound = 10
largest_upper_bound = 1000
upper_bounds = range(smallest_upper_bound, largest_upper_bound + 1)
coprime_probs = np.zeros(shape = (len(upper_bounds), ))
pi_ests = np.zeros(shape = (len(upper_bounds), ))

for b in range(len(upper_bounds)):
    # Generate pairs of random integers and check for coprimality
    rand_ints = np.random.randint(low = lower, high = upper_bounds[b] + 1, size = (n_sims, 2))
    gcf_list = [gcf(x) for x in rand_ints.tolist()]
    coprime_list = [x == 1 for x in gcf_list]
    
    # Calculate stuff
    prob_coprime = np.mean(coprime_list)
    coprime_probs[b] = np.mean(coprime_list)
    pi_ests[b] = math.sqrt(6 / prob_coprime)
    

#%% Stick 'em in a data frame and plot
pi_est_df = pd.DataFrame({'upper_bound': upper_bounds,
                          'prob_coprime': coprime_probs,
                          'pi_est': pi_ests})

# Plot estimates of pi vs. upper bound used
plt.style.use('ggplot')
pi_plot = sns.lineplot(x = 'upper_bound', y = 'pi_est', data = pi_est_df)
pi_plot.axhline(math.pi, color = 'black')

# simulation settings
POP_SIZE=2000
SIM_LENGTH = 50    # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DELTA_T = 1       # years

# the transition probability matrix
Prob_MATRIX = [
    [0.75, 0.15, 0.0, 0.1],   # well
    [0.0,  0.0,  1.0, 0.0],   # stroke
    [0.0,  0.25, 0.55, 0.2],   # post stroke
    ]

# New Matrix after the drug
Prob_DRUG_MATRIX = [
    [0.75, 0.15, 0.0, 0.1],   # well
    [0.0,  0.0,  1.0, 0.0],   # stroke
    [0.0,  0.1625, 0.701, 0.1365],   # post stroke
    ]

#
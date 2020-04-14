import SimPy.FittingProbDist_MM as MM


# fitting an exponential distribution
exp_params = MM.get_expon_params(mean=10)
print('Parameters of exponential distribution:', exp_params)

# fitting a beta distribution
beta_params = MM.get_beta_params(mean=20,
                                 st_dev=5,
                                 minimum=0,
                                 maximum=1)
print('Parameters of beta distribution:', beta_params)

# fitting a Poisson distribution
poisson_params = MM.get_poisson_params(mean=20)
print('Parameters of Poisson distribution', poisson_params)

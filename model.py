import matplotlib.pyplot as pplot

def run_sir_model(
        population = 10000,
        infection_seed = 80,
        infection_rate = 0.03,
        recovery_rate = 0.01,
        relapse_rate = 0,
        death_rate = 0,
        vaccination_rate = 0,
        vaccination_time = 1000,
        time = 1000
    ):
    """
    Run a standard SIR model with death, for given data and plot results

    Keyword arguments:
    population -- the population size for the SIR model
    infection_seed -- the initial number of infected members in the population
    infection_rate -- the rate at which those in the population susceptible to
                      infection are infected
    recovery_rate -- the rate at which infected members of the population heal
                     and are no longer infected
    relapse_rate -- the rate at which those immune (natural or vaccine) become
                    susceptible once again
    death_rate -- the rate at which those infected die
    vaccination_rate -- the rate at which the population is being vaccinated
    vaccination_time -- the days at which vaccines start being given
    time -- number of steps the simulation should run
    """
    infected = infection_seed
    susceptible = population - infected
    recovered = 0
    dead = 0
    immune = 0
    history = ([susceptible],
               [infected],
               [recovered],
               [dead],
               [immune],
               [susceptible + recovered + immune]
              )
    days = 0
    vaccine_recovery = 0
    immunizations = 0
    while (days < time):
        days = days + 1
        if (days > vaccination_time):
            vaccine_recovery = vaccination_rate
            immunizations = (susceptible + infected \
                             + recovered)*vaccination_rate

        infections = susceptible*infection_rate
        recoveries = infected*recovery_rate
        relapses = recovered*relapse_rate
        deaths = infected*death_rate
        
        infected = infected*(1 - vaccine_recovery) + infections \
                   - recoveries - deaths
        recovered = recovered*(1 - vaccine_recovery) + recoveries - relapses
        immune = immune + immunizations
        susceptible = susceptible*(1 - vaccine_recovery) + relapses \
                      - infections
        dead = dead + deaths

        for i, e in enumerate([
                susceptible,
                infected,
                recovered,
                dead,
                immune,
                susceptible + immune
            ]):
            history[i].append(e)
    
    data_range = range(len(history[0]))
    pplot.plot(
        data_range, history[0],
        data_range, history[1],
        data_range, history[2],
        data_range, history[3],
        data_range, history[4],
        data_range, history[5],
        '--'
    )
    pplot.legend([
        'susceptible',
        'infected',
        'recovered',
        'dead',
        'immune',
        'healthy'
    ])
    pplot.tight_layout(pad=2)
    pplot.grid()
    pplot.xlabel('Days')
    pplot.ylabel('People')
    pplot.show()

'''
#SIR
run_sir_model(
    population = 2500000,
    time = 400
)
'''

'''
#SIRS
run_sir_model(
    population = 2500000,
    relapse_rate = 0.015,
    time = 400
)
'''

'''
#SIRS with death
run_sir_model(
    population = 2500000,
    relapse_rate = 0.015,
    death_rate = 0.0008,
    time = 1500
)
'''

#SIRS with death and vaccinations
run_sir_model(
    population = 2500000,
    relapse_rate = 0.015,
    death_rate = 0.0008,
    vaccination_rate = 0.005,
    vaccination_time = 365,
    time = 730
)
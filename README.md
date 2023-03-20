# Dynamics of niche construction in adaptable populations evolving in diverse environments

This is the code accompannying our submission.

In this work we have studied the evolution of niche construction in a population of agents that can adapt its plasticity and evolvability in a world divided in niches that differ in their quality.
 

Each niche $n$ is characterized by its environmental state $e_n^g$ which is the sum of the intrinsic state $i_n$ (in blue) and the niche-constructed state $a_n^g$ (in red). The intrinsic state remains constant with time and is determined by the state of the reference niche $(e_0)$ and the offset $\epsilon$. The niche-constructed state is the sum of the niche-constructing behavior of agents that reproduce in this niche in the current generation and the niche-constructed state at the previous generation discounted by $\gamma$. It therefore, varies with time.

![world](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Feleni%2FwKKA6Vq5G3.png?alt=media&token=74d42d5b-bf70-4681-9d27-074e10ca3c1f)

We model the plasticity of an individual using tolerance curves  originally developed in ecology. Plasticity curves have the form of a Gaussian the capture the benefits and costs of plasticity when comparing a specialist (left) with a generalist (right) agent:

![plasticity](https://firebasestorage.googleapis.com/v0/b/firescript-577a2.appspot.com/o/imgs%2Fapp%2Feleni%2FNxx4mqJX7h.png?alt=media&token=c2a2d6e3-2119-4929-b5b4-b440ea64cb54)



The repo contains the following main elements :

* folder source contains the main functionality for running a simulation
* folder scripts contains scripts for reproducing the experiments and figures
* folder projects contains data generated from running a simulation

# How to run

To install all package dependencies you can create a conda environment as:

`conda env create -f environment.yml`

All script executions need to be run from folder source. Once there, you can use simulate.py, the main interface of the codebase to run a simulation, For example:

`python simulate.py --project test_stable --num_gens 300 --capacity 1000 --num_niches 10 --trials 10 --selection_type NF --climate_mean_init 2`

will run a simulation with an environment with a climate function whose state is constantly 2 consisting of 100 niches for 300 generations and 10 independent trials. The maximum population size will be 1000*2 and selection will be fitness-based (higher fitness means higher chances of reproduction) and niche limited (individuals reproduce independently in each niche and compete only within a niche),





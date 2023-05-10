def niche_construction_stable(mode):
    top_dir = setup_dir(project="niche_construction", mode=mode) + "/longer/"

    flags = ["--project",
             "--env_type",
             "--num_gens",
             "--trial",
             "--selection_type",
             "--genome_type",
             "--num_niches",
             "--climate_mean_init"
             ]

    env_type = "stable"
    num_gens = 2000
    genome_types = ["niche-construction"]
    num_niches_values = [1, 20, 50, 100]
    selection_types = ["F", "NF"]  # F is global, NF is local
    climate_mean_init_values = [0.6]

    for num_niches in num_niches_values:
        for genome_type in genome_types:
            for climate_mean_init in climate_mean_init_values:
                for S in selection_types:
                    project = top_dir + "S_" + S + "_G_" + genome_type + "_N_" + \
                              str(num_niches) + "_climate_" + str(climate_mean_init)
                    values = [project, env_type, num_gens, trial, S, genome_type, num_niches, climate_mean_init]
                    config = dict(zip(flags, values))
                    exec_command(config)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("You need to provide the number of trials and mode.")
    else:
        trials = int(sys.argv[1])  # number of independent trials

        for trial in range(trials):
            niche_construction()

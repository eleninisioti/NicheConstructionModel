""" You can run this script to reproduce all figures in the paper.
Figures will be saved under the top_dir that you specify when calling a function
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

# produce figure 3
from scripts.compare_projects import plot
plot(top_dir="alife_2023/oneniche", parameter="num_niches")

# produce figure 4
plot(top_dir="alife_2023/F_average", parameter="genome")

# produce figure 5
plot(top_dir="alife_2023/NF_average", parameter="genome")

# produce figures 6 and 7
from plot_projects import plot_project
plot_project(top_dir="alife_2023/F_trials")

# produce figure 8
plot_project(top_dir="alife_2023/NF_trials")

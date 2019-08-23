"""
Collect the results of the screening simulations
and put into a CSV file for loading into numpy and pandas later.
"""

import signac
import numpy as np

groups = ["toluene", "isopropylbenzene", "phenol"]

p = signac.get_project()

from atools_ml import rf

job_ids = p.

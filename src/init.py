#!/usr/bin/env python
"""Initialize the project's data space.

Iterates over all defined state points and initializes
the associated job workspace directories."""
import argparse
import logging
import datetime
from copy import deepcopy
from hashlib import sha1

import signac

logging.basicConfig(filename='init.log', filemode='w', level=logging.INFO)

'''
-----------------------------
NEW 5 terminal group chemistries
-----------------------------
These will be the same group on top and bottom
'''
terminal_groups_new_A = ['toluene', 'benzoicacid', 'phenol',
                         'isopropylbenzene', 'difluoromethyl']

terminal_groups_new_B = deepcopy(terminal_groups_new_A)


# Initialize the project
def main(args, random_seed):
    project = signac.init_project("screeningAccuracy")
    logging.info("Init begin: {}".format(datetime.datetime.today()))
    logging.info("Initialized project name")
    statepoints = list()
    # generate the new equvalent top and bottom monolayers
    for layerA, layerB in zip(terminal_groups_new_A, terminal_groups_new_B):
        for n_rep in range(args.num_replicas):
                assert layerA == layerB,\
                    'top and bottom terminal groups are not the same'
                the_statepoint = dict(
                    # carbon backbone length
                    chainlength=int(args.chain_length),
                    # num of chains on surface
                    n=100,
                    # random seed
                    seed=random_seed*(n_rep+1),
                    # monolayer chemistries
                    terminal_groups=tuple(sorted((layerA, layerB)))
                )
                project.open_job(statepoint=the_statepoint).init()
                statepoints.append(the_statepoint)
                logging.info(msg="At the statepoint: {}".format(the_statepoint))
    # write statepoints to signac statepoint file
    project.write_statepoints(statepoints=statepoints)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Initialize the data space.")
    parser.add_argument(
        'random',
        type=str,
        help="A string to generate a random seed.")
    parser.add_argument(
        '-n', '--num-replicas',
        type=int,
        default=1,
        help="Initialize multiple replications.")
    parser.add_argument(
        '-c', '--chain-length',
        type=int,
        default=17,
        help="Backbone length of chain.")
    args = parser.parse_args()

    # Generate an integer from the random str.
    try:
        random_seed = int(args.random)
    except ValueError:
        random_seed = int(sha1(args.random.encode()).hexdigest(), 16) % (10 ** 8)
    
    logging.info("Params:\
                random: {}\
                num-replicas: {}\
                chain_length: {}".format(
                    random_seed,
                    args.num_replicas,
                    args.chain_length
                    ))

    main(args, random_seed)

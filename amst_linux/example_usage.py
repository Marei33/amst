
# Copy this script to a desired location
# E.g., if AMST was cloned to /home/user/src/amst make a home/user/src/amst_experiments folder for the execution scripts

import sys
# Append the location of the amst package to the system path. Replace by the proper location, e.g. '/home/user/src/amst'
# for the example above
sys.path.append('/Users/marei/git-repositories/amst/')

from amst_linux.amst_main import amst_align, default_amst_params

raw_folder = '/Users/marei/fruit-fly-data/igor-the-larva/alignment_correction/raw_data'
pre_alignment_folder = '/Users/marei/fruit-fly-data/igor-the-larva/alignment_correction/amst/pre_alignment'
target_folder = '/Users/marei/fruit-fly-data/igor-the-larva/alignment_correction/amst/target'

# Load the default parameters
params = default_amst_params()

# Due to the multiprocessing, in Windows, the following has to be inside a __name__ == '__main__' block
# In Linux it doesn't matter, but it also does no harm
if __name__ == '__main__':
    amst_align(
        raw_folder=raw_folder,
        pre_alignment_folder=pre_alignment_folder,
        target_folder=target_folder,
        **params
    )

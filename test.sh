#!/bin/bash -l
#PBS -N screeningAccuracy/bundle/84956d82c2d45f774d669585e22f1280ae0602ff
#PBS -l walltime=00:09:00
#PBS -l nodes=2
#PBS -j oe
#PBS -l gres=atlas1%atlas2
#PBS -m abe
#PBS -M gilmerjb.job.scheduler@gmail.com
#PBS -A NTI112
#PBS -q debug

set -e
set -u
module load dynamic-link
export CRAY_CUDA_MPS=1
module load gromacs/5.1.0
module load python wraprun
cd $PBS_O_WORKDIR
wraprun \
-n 1,1 --w-cd /lustre/atlas2/nti112/proj-shared/terminal_group_screening_accuracy_test/workspace/3b2f645b59431b1d63b2874fb619041c,/lustre/atlas2/nti112/proj-shared/terminal_group_screening_accuracy_test/workspace/cff74fe8f6dcdb75f05160ea3417b185 gmx_mpi trjcat -f shear_5nN.\*.xtc -o shear_5nN_combined.xtc : \
-n 1,1 --w-cd /lustre/atlas2/nti112/proj-shared/terminal_group_screening_accuracy_test/workspace/3b2f645b59431b1d63b2874fb619041c,/lustre/atlas2/nti112/proj-shared/terminal_group_screening_accuracy_test/workspace/cff74fe8f6dcdb75f05160ea3417b185 gmx_mpi trjcat -f shear_5nN.\*.trr -o shear_5nN_combined.trr 


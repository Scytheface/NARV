#!/bin/bash
#SBATCH --nodes 1
#SBATCH --partition gpu
#SBATCH --time 12:00:00
#SBATCH --mem 10000
#SBATCH --gres=gpu:tesla:2

source ./.venv/bin/activate

jupyter_port=$(shuf -i61000-62000 -n1)
RC=$(netstat -vatn | awk '{print $4}' | awk -F ":" '{print $NF}' | sort | uniq | grep -w ${jupyter_port})

while ! [[ -z $RC ]]
do
  jupyter_port=$(shuf -i61000-62000 -n1)
  RC=$(netstat -vatn | awk '{print $4}' | awk -F ":" '{print $NF}' | sort | uniq | grep -w ${jupyter_port})
done

jupyter-notebook --no-browser --port=${jupyter_port} --ip=$(hostname -f) &
pid[0]=$!
trap "kill ${pid[0]}; exit 0;" SIGINT SIGTERM
wait

exit 0

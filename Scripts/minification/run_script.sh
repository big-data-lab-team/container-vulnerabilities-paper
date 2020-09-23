#!/bin/bash

###these commands are image specific ######
export cmd1='python3 /run.py /data /data/outputs participant --participant_label 0003001 0003002 --license_file /data/license.txt'
export cmd2='python3 /run.py /data /data/outputs group1 --participant_label 0003001 0003002 --license_file /data/license.txt'
export cmd3='python3 /run.py /data /data/outputs group2 --participant_label 0003001 0003002 --license_file /data/license.txt'
###splitting image name and tag
name1="$(cut -d'/' -f1 <<<"$2")"
name2="$(cut -d'/' -f2 <<<"$2")"
name="$(cut -d':' -f1 <<<"$name2")"
###run image and mount the required dataset to /data folder inside image
###if the image needs dataset and output mounted to a specific folder that should be done in following command while running container
###for example bids/mindboggle:0.0.4-1 required dataset to be mounted to /home/jovyan/work/data so instead of /data required path
###should be passed and accordingly changes should be made to the rest of the script
docker run -itd --entrypoint="bash" --name $name --security-opt seccomp=unconfined -v $1/:/data $2
###removing outputs folder and required file if already there
docker exec -i $name bash -c "rm -rf /data/outputs/*"
docker exec -i $name bash -c "rm -f /data/scripts/required.csv"
###removing log files if already exist
rm -f ${name1}_${name}_repro.log
rm -f ${name1}_${name}_After_repro.log
###running script inside container to install Reprozip
docker exec -i $name bash -c "/data/scripts/run_repro_script.sh" &>> ${name1}_${name}_repro.log && echo "[ OK..Reprozip Installed Successfully ]"
###running reprozip trace inside container
docker exec -i $name bash -c "reprozip trace $cmd1" &>> ${name1}_${name}_repro.log && echo "[ OK..Reprozip traced cmd1 Successfully]"
docker exec -i $name bash -c "reprozip trace --continue $cmd2" &>> ${name1}_${name}_repro.log && echo "[ OK..Reprozip traced cmd2 Successfully ]"
docker exec -i $name bash -c "reprozip trace --continue $cmd3" &>> ${name1}_${name}_repro.log && echo "[ OK..Reprozip traced cmd3 Successfully ]"
###collecting reprozip trace in required format
export comm="cat .reprozip-trace/config.yml | grep -E \"  - name: \" | awk -F: '{print \$2}' | tr -d '\"' | tr -d ' ' &> /data/scripts/required.csv"
docker exec -i $name bash -c "$comm" && echo "[ OK..Reprozip trace collected Successfully]"
###stopping and removing container
docker stop $name
docker rm $name
###running another instance of the same image
docker run -itd --entrypoint="bash" --name $name -v $1/scripts/:/scripts $2
####running script inside container to get all dependencies 
docker exec -i $name bash -c "/scripts/script.sh" &>> ${name1}_${name}_After_repro.log && echo "[ OK..Now finding all dependencies of Required packages ]"
###removing container
docker stop $name
docker rm $name
###running another clean instance of image because in previous ones we install few extra packages like Debtree, aptitude etc. 
####finally in this container we remove all the unecessary packages
docker run -itd --entrypoint="bash" --name $name $2
export comm2="$(cat $1/scripts/to_remove.txt)"
export comm3="apt remove "$comm2" -y"
docker exec -i $name bash -c "$comm3" &>> ${name1}_${name}_After_repro.log && echo "[ OK..Removed packages successfully ]" && docker commit $name ${name1}_${name}:minified && echo "[OK..Committed minified image]"
docker stop $name
docker rm $name
echo "its done"



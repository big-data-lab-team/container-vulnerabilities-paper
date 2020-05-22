#!/bin/bash

export cmd1='python3 /run.py /data /data/outputs participant --participant_label 0003001 0003002 --license_file /data/license.txt'
export cmd2='python3 /run.py /data /data/outputs group1 --participant_label 0003001 0003002 --license_file /data/license.txt'
export cmd3='python3 /run.py /data /data/outputs group2 --participant_label 0003001 0003002 --license_file /data/license.txt'
name1="$(cut -d'/' -f1 <<<"$2")"
name2="$(cut -d'/' -f2 <<<"$2")"
name="$(cut -d':' -f1 <<<"$name2")"
docker run -itd --entrypoint="bash" --name $name --security-opt seccomp=unconfined -v $1/:/data $2
docker exec -i $name bash -c "rm -rf /data/outputs/*"
rm -f ${name1}_${name}_repro.log
rm -f ${name1}_${name}_After_repro.log
docker exec -i $name bash -c "/data/scripts/run_repro_script.sh" &>> ${name1}_${name}_repro.log && echo "[ OK..Reprozip Installed Successfully ]"
docker exec -i $name bash -c "rm -f /data/scripts/required.csv"
docker exec -i $name bash -c "reprozip trace echo hello" &>> ${name1}_${name}_repro.log && echo "[ OK..Reprozip traced cmd1 Successfully]"
#docker exec -i $name bash -c "reprozip trace $cmd1" &>> ${name1}_${name}_repro.log && echo "[ OK..Reprozip traced cmd1 Successfully]"
#docker exec -i $name bash -c "reprozip trace --continue $cmd2" &>> ${name1}_${name}_repro.log && echo "[ OK..Reprozip traced cmd2 Successfully ]"
#docker exec -i $name bash -c "reprozip trace --continue $cmd3" &>> ${name1}_${name}_repro.log && echo "[ OK..Reprozip traced cmd3 Successfully ]"
export comm="cat .reprozip-trace/config.yml | grep -E \"  - name: \" | awk -F: '{print \$2}' | tr -d '\"' | tr -d ' ' &> /data/scripts/required.csv"
docker exec -i $name bash -c "$comm" && echo "[ OK..Reprozip trace collected Successfully]"
docker stop $name
docker rm $name
docker run -itd --entrypoint="bash" --name $name -v $1/scripts/:/scripts $2
docker exec -i $name bash -c "/scripts/script.sh" &>> ${name1}_${name}_After_repro.log && echo "[ OK..Now finding all dependencies of Required packages ]"
docker stop $name
docker rm $name
docker run -itd --entrypoint="bash" --name $name -v $1/scripts/to_remove.txt:/scripts/to_remove.txt $2
export comm2="$(cat /scripts/to_remove.txt)"
export comm3="apt remove "$comm2" -y"
docker exec -i $name bash -c "$comm3" &>> ${name1}_${name}_After_repro.log && echo "[ OK..Removed packages successfully ]" && docker exec -i $name bash -c "rm -rf /scripts/" && echo "[ OK..Deleted desired folder]" && docker commit $name ${name1}_${name}:minified && echo "[OK..Committed minified image]"
#docker stop $name
#docker rm $name 
echo "its done"


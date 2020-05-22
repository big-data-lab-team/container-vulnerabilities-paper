#!/bin/bash

cd /scripts/
shopt -s extglob
rm -v !("required.csv"|"to_delete.py"|"check_virtuality.py"|"script.sh"|"run_repro_script.sh")
apt list --installed | awk -F/ '{print $1}' | tail -n +2 > all-packages.csv
apt-get update
apt-get install -y debtree
apt install aptitude -y
aptitude -F %p search --disable-columns '~Rprovides:~i ~v' >> virtual.csv
aptitude -F %p search --disable-columns ~pimportant >> required.csv
aptitude -F %p search --disable-columns ~prequired >> required.csv
cat required.csv | sort | uniq >> uniq_required-0.csv
touch keep_virtual.csv
IFS=$'\n'
number=0

###function####
get_dependencies() {
for k in $(cat $1)
do
(for i in $(debtree --show-installed --no-skip --show-all $k | tail -n +4); do if [[ $i == *"->"* ]]; then     c=$(echo $i | awk '{print $1}' | sed 's/"//g');     if [[ $c == *:* ]];     then       echo echo $c | awk -F: '{print $2}';     else       echo $c;     fi; else if [[ $i == *";"* ]]; then    echo $i |sed -e 's/^[[:space:]]*//' |sed 's/"//g'|head -n1 | awk '{print $1}';elif [[ $i == *"label = "* ]]; then str=$(echo $i | awk '{print $3}'); prefix='"<'; suffix='>';foo=${str#"$prefix"};foo=${foo%"$suffix"}; echo "${foo}" >> $2; fi; fi; done; ) | sort | uniq >> $3
done
cat $3 | sort | uniq >> $4
cat $2 | sort | uniq >> $5
comm -13 <(sort $4) <(sort $5) >> $6
}

#####function#####
get_package() {
for x in $(cat $1)
do
echo "getting package of virtual package "$x
aptitude -F %p search --disable-columns '~P'$x' ~i' >> $2
done
}

while [ $(cat "uniq_required-${number}.csv" | wc --lines) != 0 ]
do
echo "************************************************ROUND ${number}***********************************************************************"
uniq_required="uniq_required-${number}.csv"
label="label-${number}.csv"
total_p="total_p-${number}.csv"
total_packages="total_packages-${number}.csv"
temp_label="temp_label-${number}.csv"
uniq_label="uniq_label-${number}.csv"
installed_p="installed-${number}.csv"
virtual_p="virtual_p-${number}.csv"
installed_label="installed_label-${number}.csv"
virtual_label="virtual_label-${number}.csv"
uniq_virtual="uniq_virtual-${number}.csv"
check="check-${number}.csv"
this_check="this_check-${number}.csv"
left_virtual="left_virtual-${number}.csv"
get_dependencies $uniq_required $label $total_p $total_packages $temp_label $uniq_label
python ./check_virtuality.py $total_packages $installed_p $virtual_p
python ./check_virtuality.py $uniq_label $installed_label $virtual_label
cat $virtual_label >> $virtual_p
cat $virtual_p | sort | uniq >> $uniq_virtual
comm -13 <(sort keep_virtual.csv) <(sort $uniq_virtual) >> $left_virtual
cat $installed_p >> keep_installed.csv
get_package $left_virtual $check
cat $left_virtual >> keep_virtual.csv

cat $installed_label >> $check
cat $check | sort | uniq >> $this_check
comm -13 <(sort keep_installed.csv) <(sort $this_check) >> uniq_required-$((++number)).csv
number=$((++number))
done
cat keep_installed.csv | sort | uniq >> uniq_keep_installed.csv
echo "**************************************Finally done*******************************************************************"
python ./to_delete.py

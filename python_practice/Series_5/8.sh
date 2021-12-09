#!/bin/sh
echo "please enter adress : "
read adress
while read line
do
	echo "[" $line "]"
done < test.txt
for eachfile in ls $adress
do
	echo $eachfile *"a"*
#	if *"a"* in eachfile
#	then
#		echo $eachfile
#	fi
done

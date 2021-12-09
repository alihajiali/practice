#!/bin/sh
echo "please enter adress "
read adress
for eachfile in `ls $adress`
do
	if [ -f $eachfile ]
	then
		echo `cat $eachfile > write.txt`

	fi
done
head -n10 ./write.txt | tail -n5 ./write.txt

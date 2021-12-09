#!/bin/sh
echo "please enter your adress : "
read adress
file=0
folder=0
add=1
for eachfile in `ls $adress`
do
	if [ -f $eachfile ]
	then
		file=`expr $file + $add`
	elif [ -d $eachfile ]
	then
		folder=`expr $folder + $add`
	fi
done
echo "number of files : "$file
echo "number of folders : "$folder


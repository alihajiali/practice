#!/bin/sh
echo "please enter adress : "
read adress
if [ -f $adress ]
then
	echo "This file exists on your filesystem."
else
	`mkdir $adress`
fi

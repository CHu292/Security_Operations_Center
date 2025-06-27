#!/bin/bash
echo "Enter your name:"
read name
echo "Enter your age:"
read age
if [ "$age" -ge 18 ]
then
	echo "$name can work"
else
	echo "$name is not eligible for work"
fi

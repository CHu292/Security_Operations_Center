#!/bin/bash
name=""
company=""
pass=""

echo "Please enter your username:"
read name
echo "Please enter your company name:"
read company
echo "Please enter your password:"
read pass

if [ "$name" = "Sun" ] && [ "$company" = "KMA" ] && [ "$pass" = "2510" ]; then
	echo "Authentication Successful. You can now access yor locker, Sun."
else
	echo "Authentication Denied!!"
fi

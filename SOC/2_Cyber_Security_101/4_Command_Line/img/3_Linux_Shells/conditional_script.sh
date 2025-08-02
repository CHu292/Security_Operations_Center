#!/bin/bash
secret_name="sun"
echo "Please enter your name first:"
read name
if [ "$name" = "$secret_name" ]; then
	echo "wellcome Sun! Here is the secret: CC"
else
	echo "Sorry! You are not authorized to access the secret."
fi

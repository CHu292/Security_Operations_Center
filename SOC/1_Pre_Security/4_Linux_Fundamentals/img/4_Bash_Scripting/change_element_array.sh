#!/bin/bash
transport=('car' 'train' 'bike' 'bus')
echo "${transport[@]}"
transport[1]='trainride'
echo "${transport[@]}"


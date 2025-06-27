#!/bin/bash
transport=('car' 'train' 'bike' 'bus')
unset transport[1]
echo "${transport[@]}"


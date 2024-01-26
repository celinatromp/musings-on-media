#!/bin/sh
# we read each line from the first argument ($1)
# for each of the lines that we read we add a string starting with whatever we pass as $2, followed by the content of the current line.
# we encapsulate all of that so that the string gets added to whatever we pass as $3, instead of being printed in the console. :)
(while read line; do
    echo "$2 $line"
done < $1) > $3
# to execute: ./objective8-9.sh phone_number.txt +31 out.txt
#!/bin/bash

process_line() {
    local line="$1"
    
    # Regex patterns
    local r1='^[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$'   # Matches 'xxx-xxx-xxxx'
    local r2='^\([0-9][0-9][0-9]\) [0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]$' # Matches '(xxx) xxx-xxxx'
    
    # Check if the line matches either pattern
    if [[ "$line" =~ $r1 ]] || [[ "$line" =~ $r2 ]]; then
        echo "$line"
    fi
}



# open the file and read line by line
while IFS= read -r line || [[ -n "$line" ]];
do
    #process each lin
    process_line "$line"
done < "./193.txt"

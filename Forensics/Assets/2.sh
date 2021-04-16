#!/bin/sh

strings find-flags-in-me | grep -i 'ctf'

echo "" 

# s/ //g means to remove the whitespace

xxd find-flags-in-me | tr '.' ' ' | sed 's/ //g' | grep -i 'inc'

echo "" 

# grep -i is for case insensitive

xxd find-flags-in-me | tr '.' ' ' | sed 's/ //g' | grep -i 't'




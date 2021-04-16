#!/bin/sh

f1=Twin1
f2=Twin2

size=$(stat -c%s $f1)
i=0

echo -n "The Flag is : "

while [ $i -lt $size ]; do
  if ! r="`cmp -n 1024 -i $i -b $f1 $f2`"; then
    printf "%8x: %s\n" $i "$r" | sed 's/ //g' | sed -e 's/\(^.*\)\(.$\)/\2/' | tr '\n' ' ' | sed 's/ //g'
  fi
  i=$(expr $i + 1024)
done

echo ""

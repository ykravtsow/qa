#!/bin/bash

status=0
for ((i=1;$i<11;i=$i+1))
    do
    dir=`echo "DZ$i"`
    cd $dir && python3 -m pytest || res=$? && cd .. || /bin/true
    if [[ "$res" != "0" ]]
       then
       status=$res
    fi
    done

exit $status

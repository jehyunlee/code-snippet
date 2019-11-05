#!/bin/bash

SET=$(seq 0 25)
for i in $SET
do
  cp nohup_run.sh nohup_run_$i.sh
  sed -i "s/%/$i/" nohup_run_$i.sh
  nohup ./nohup_run_$i.sh > nohup_run_$i.out 2>&1&
done


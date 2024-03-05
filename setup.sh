#!/usr/bin/env bash
pythonlib='/usr/lib/python3.11'
pythondeps=()
binarydeps=()

for val in ${$pythondeps[@]}
do
  if [ -f "$pythonlib/$val" ]; then
    sleep(1)
  else
   pip install $val
  fi
done

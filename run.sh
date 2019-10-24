#!/bin/bash

conda activate swe4s

echo ...running calculate.py with 1 and 4...
python calculate.py --a 1 --b 4

echo ...running calculate.py with 2 and 0...
python calculate.py --a 2 --b 0

#!/bin/bash
python3 build.py
wait
python3 ../knight_dummy.pyz 0 &
python3 ../knight_dummy.pyz 1 &
python3 ../knight_dummy.pyz 2 &
python3 ../knight_rush.pyz 3 &
#!/bin/bash
python3 build.py
wait
python3 ../bot.pyz 0 &
python3 ../knight_dummy.pyz 1 &
python3 ../knight_rush.pyz 2 &
python3 ../knight_rush2.pyz 3 &
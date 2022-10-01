#!/bin/bash
python3 build.py
wait
python3 ../bot.pyz 0 &
python3 ../bot.pyz 1 &
python3 ../bot.pyz 2 &
python3 ../bot.pyz 3 &
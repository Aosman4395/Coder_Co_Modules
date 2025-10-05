#!/bin/bash
 
 grade=99
 position=1
 
 if [ $grade -ge 99 ]; then
 if [ $position -eq 1 ]; then
 echo "You are 1st place!"
 fi
 elif [ $grade -ge 70 ] && [ $grade -lt 90 ]; then
 echo "You are 2nd place!"
 else
 echo "Sorry you lost!"
 fi

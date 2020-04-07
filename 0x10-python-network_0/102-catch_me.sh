#!/bin/bash
# This will hacks its way into Holberton
curl -Ls -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me

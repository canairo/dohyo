#!/bin/bash
random=$(head -n 32 /dev/urandom | od -A n -t x | head -n 1 | tr -d ' ')

patchelf --set-interpreter ./ld-linux-x86-64.so.2 --set-rpath '$ORIGIN' chal
sudo docker build -t cane:$random .
echo "running now... connect with the following command:
---
nc 127.0.0.1 8080"
sudo docker run --rm --network host cane:$random

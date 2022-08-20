#!/bin/bash

# sleep 10
python3 -c "print('waiting for input')"
python3 -c "input()"
echo Start to run vuln

./vuln < output

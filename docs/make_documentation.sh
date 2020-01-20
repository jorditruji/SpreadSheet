#!/bin/bash

sphinx-apidoc -f -o . ../src/
sphinx-build -b html . html/


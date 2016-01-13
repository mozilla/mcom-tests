#!/bin/bash

py.test -r=fsxXR --verbose -n 15 \
        --base-url ${BASE_URL} \
        --html results/index.html \
        --junitxml results/results.xml \
        tests

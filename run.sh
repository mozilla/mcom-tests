#!/bin/bash

py.test -r=fsxXR --verbose -n 15 \
        --base-url ${BASE_URL} \
        --driver SauceLabs \
        --capability browserName "${BROWSER_NAME}" \
        --capability version "${BROWSER_VERSION}" \
        --capability platform "${PLATFORM}" \
        --capability selenium-version "${SELENIUM_VERSION}" \
        --capability build "${BUILD_TAG}" \
        --capability screenResolution "1280x1024" \
        --html results/index.html \
        --junitxml results/results.xml \
        tests

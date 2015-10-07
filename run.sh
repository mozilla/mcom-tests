#!/bin/bash

py.test -r=fsxXR --verbose -n 15 \
        --baseurl=${BASE_URL} \
        --browsername="${BROWSER_NAME}" \
        --browserver=${BROWSER_VERSION} \
        --platform="${PLATFORM}" \
        --junitxml=results/results.xml \
        --saucelabs=${SAUCE_CREDENTIALS_PATH} \
        --capability="selenium-version:${SELENIUM_VERSION}" \
        --build=${BUILD_TAG} \
        tests

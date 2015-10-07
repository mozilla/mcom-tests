Mozilla.com Selenium Tests
============================

This repository holds automated tests for [http://www.mozilla.org][MOZ]

[MOZ]: http://www.mozilla.org

Running Tests
-------------

### Python

Before you will be able to run these tests you will need to have
Python 2.7.9 installed.

__note__

Python versions before 2.7.9 do not support
[SNI](https://en.wikipedia.org/wiki/Server_Name_Indication) which will
cause tests to fail.

If you are running on Ubuntu/Debian you will need to first do

    sudo apt-get install python-setuptools

to install the required Python libraries.

__note__

The instructions below will install the required Python libraries into your
global Python installation. If you work on multiple Python projects that might
end up needing different versions of the same libraries, you might want to
follow `sudo easy_install pip` with `sudo pip install virtualenv`, and then
create and activate a [virtualenv](http://www.virtualenv.org) (e.g. `virtualenv
mcom-tests-env; source mcom-tests-env/bin/activate`) to create a clean
"virtual environment" for just this project. Then you can
`pip install -r requirements.txt` in your virtual environment
without needing to use `sudo`.

If you don't mind installing globally, just run

    sudo easy_install pip

followed by

    sudo pip install -r requirements.txt

__note__



### Running tests locally

To run tests locally, it's a simple case of calling the command below from this directory

    py.test --driver=firefox

For more command line options, see https://github.com/mozilla/pytest-mozwebqa


### Running tests with Docker

__note__

You will need a working Docker installation. Docker provides complete
[installation documenation](https://docs.docker.com/installation/) for
various systems including Linux, OSX and Windows.

To run Saucelabs backed tests with Docker:

1. Save Saucelabs credentials in a file named `creds.yml` in the
   following format

        username: USERNAME
        password: PASSWORD
        api-key: API_KEY

2. Run:

    docker run -v `pwd`/creds.yml:/tmp/creds -v `pwd`/results/:/app/results mozorg/mcom-tests

3. Find the test results in the `results` directory.

__note__

The default test configuration is listed in the
[Dockerfile](Dockerfile) and can be overriden with environment
variables. For example to test against the stage server, override
BASE_URL environment variable:

    docker run -v `pwd`/creds.yml:/tmp/creds -e BASE_URL=https://www.allizom.org mozorg/mcom-tests

__note__

Docker registry builds new docker images for every code commit in
mozilla/mcom-tests. To fetch an up to date image run:

    docker pull mozorg/mcom-tests



Writing Tests
-------------

If you want to get involved and add more tests then there's just a few things
we'd like to ask you to do:

1. Use the [template files][GitHub Templates] for all new tests and page objects
2. Follow our simple [style guide][Style Guide]
3. Fork this project with your own GitHub account
4. Make sure all tests are passing, and submit a pull request with your changes

[GitHub Templates]: https://github.com/mozilla/mozwebqa-test-templates
[Style Guide]: https://wiki.mozilla.org/QA/Execution/Web_Testing/Docs/Automation/StyleGuide

License
-------
This software is licensed under the [MPL] 2.0:

    This Source Code Form is subject to the terms of the Mozilla Public
    License, v. 2.0. If a copy of the MPL was not distributed with this
    file, You can obtain one at http://mozilla.org/MPL/2.0/.

[MPL]: http://www.mozilla.org/MPL/2.0/

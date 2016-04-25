#!/usr/bin/env bash

# Install VirtualEnv + VirtualEnv-Wrapper via VirtualEnv-Burrito
command -v virtualenv >/dev/null 2>&1 || {
  echo >&2 "VirtualEnv is not installed.";
  curl -sL https://raw.githubusercontent.com/brainsik/virtualenv-burrito/master/virtualenv-burrito.sh | $SHELL;
}

cd ~;
source `which virtualenvwrapper.sh`;
mkvirtualenv wh101;
workon wh101;
git clone git@github.com:andrewnelder/webhooks101-sample.git;
cd ./webhooks101-sample;
pip install -r requirements.txt;

echo "Installation complete!  You may now proceed with the tutorial.";
echo ""
echo "=============================="
echo ""
echo "To start your webserver:";
echo "  $ workon wh101;";
echo "  $ cd webhooks101-sample;";
echo "  $ python main.py;";
echo ""
echo "=============================="
echo ""

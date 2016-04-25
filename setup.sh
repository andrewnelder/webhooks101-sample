#!/usr/bin/env bash

# Install VirtualEnv + VirtualEnv-Wrapper via VirtualEnv-Burrito
command -v virtualenv >/dev/null 2>&1 || {
  echo >&2 "VirtualEnv is not installed.";
  curl -sL https://raw.githubusercontent.com/brainsik/virtualenv-burrito/5b5b27feae7ac5b586d8511e90cab49244688965/virtualenv-burrito.sh | $SHELL;
  source ~/.venvburrito/startup.sh;
}
source `which virtualenvwrapper.sh`;

# Install VirtualEnv + VirtualEnv-Wrapper via VirtualEnv-Burrito
command -v ngrok >/dev/null 2>&1 || {
  echo >&2 "ngrok is not installed.";
  brew install homebrew/binary/ngrok2;
}

# Download project source code
cd ~;
git clone git@github.com:andrewnelder/webhooks101-sample.git;
cd ./webhooks101-sample;

# Install dependencies
mkvirtualenv wh101; workon wh101;
pip install -r requirements.txt;

# Dump instructions
echo "Installation complete!  You may now proceed with the tutorial.  Close";
echo "this window and re-open it to continue."
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

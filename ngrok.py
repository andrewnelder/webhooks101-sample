from time import sleep
import urllib2
import subprocess
import json
import os

def start_ngrok():

    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        return

    subprocess.Popen('ngrok http 5000'.split(), stdout=subprocess.PIPE)
    sleep(2)
    tnl_data = json.loads(
        urllib2.urlopen('http://localhost:4040/api/tunnels').read()
    )

    print ' * Establishing tunnel to localhost...'
    for tnl in tnl_data.get('tunnels'):
        if 'command_line' in tnl.get('name') and tnl.get('public_url'):
            print "   - {} -> localhost:5000".format(tnl.get('public_url'))
    print ''

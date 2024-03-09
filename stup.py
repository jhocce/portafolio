
import re
import subprocess
import threading
activate_env = ["source /home/jhocceco/virtualenv/portafolio/3.8/bin/activate && cd /home/jhocceco/portafolio"]
command=["pip", "install","-r", "requirements.txt"]

proc=subprocess.Popen(activate_env, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


proc=subprocess.Popen(command, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
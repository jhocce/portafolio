
# import re
# import subprocess
# import threading
# # source /home/jhocceco/virtualenv/portafolio/3.8/bin/activate && cd /home/jhocceco/portafolio
# activate_env = ["source /home/jhocceco/virtualenv/portafolio/3.8/bin/activate && cd /home/jhocceco/portafolio"]
# command=["pip", "install","-r", "requirements.txt"]

# proc=subprocess.Popen(activate_env, stdin=subprocess.PIPE,
#             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


# proc=subprocess.Popen(command, stdin=subprocess.PIPE,
#             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)





import platform
import subprocess


def myping():
    parameter = "D:\server/venv/Scripts/activate.bat" if platform.system().lower() == "windows" else "source /home/jhocceco/virtualenv/portafolio/3.8/bin/activate"
    command = [parameter]
    print(command)
    
    response = subprocess.Popen(command, stdin=subprocess.PIPE,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    if response == 0:
        return True
    else:
        return False


print(myping())
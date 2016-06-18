import subprocess

lines = subprocess.check_output(('ls'))
line_list = lines.split('\n')
print line_list



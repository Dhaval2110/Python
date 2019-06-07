#The easiest way to copy files from one server to another over ssh is to use the scp command. For calling scp you'd need the subprocess module. For example,

import subprocess
p = subprocess.Popen(["scp", "my_file.txt", "username@server:path"])
sts = os.waitpid(p.pid, 0)
#You need the waitpid call to wait for the copying to complete.

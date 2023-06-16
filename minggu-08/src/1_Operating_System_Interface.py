import os
os.getcwd()      # Return the current working directory
'C:\\Python311'
os.chdir('/server/accesslogs')   # Change current working directory
os.system('mkdir today')   # Run the command mkdir in the system shell
0

import os
dir(os)
help(os)

import shutil
shutil.copyfile('data.db', 'archive.db')
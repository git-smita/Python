#import subprocess
#p=subprocess.Popen('ls')
#p.communicate()
#subprocess.Popen('grep -irl meena * | xargs sed -i s/meena/meena/g')
import os
os.system('grep -irl meena * | xargs sed -i s/meena/meena/g')

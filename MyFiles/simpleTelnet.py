from telnetlib import Telnet
import re

dut = Telnet()
a=raw_input().strip()
dut.open(a)
userPrompt=re.compile("[Uu]sername:")
passwordPrompt=re.compile("[Pp]assword:")
execPrompt= re.compile(".*>$")
dut.expect([userPrompt])
dut.write("adtran\n")
dut.expect([passwordPrompt])
dut.write("adtran"+"\n")
dut.expect([execPrompt])
dut.write("show version\r\n")
dut.write("show arp\n")
dut.write("exit\n")
o=dut.read_all()
print o
dut.close()




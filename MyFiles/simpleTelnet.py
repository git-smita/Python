from telnetlib import Telnet
import re

dut = Telnet()
dut.open("1.1.1.1")
# match pattern for prompts
userPrompt=re.compile("[Uu]sername:")
passwordPrompt=re.compile("[Pp]assword:")
execPrompt= re.compile(".*>$")
#match username prompt and enter username
dut.expect([userPrompt])
dut.write("adtran\n")
# match password prompt and enter password
dut.expect([passwordPrompt])
dut.write("adtran\n")
#match basic prompt
dut.expect([execPrompt])
# enter commands
dut.write("show ntp status\n")
# match the basic prompt and read the output
out= dut.expect([execPrompt])
print out[2]
dut.write("show arp\n")
out= dut.expect([execPrompt])
print out[2]
dut.write("exit\n")
out= dut.expect([execPrompt])
print out[2]
dut.close()




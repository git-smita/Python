from telnetlib import Telnet, IAC, WILL, ECHO
import re

passwordPrompt = re.compile(".*Password:")
userPrompt = re.compile(".*Username:")
execPrompt = re.compile(">$")
enablePrompt = re.compile("#$")
loginPrompt = re.compile(".*Login:")
prompt = ""


class TelnetUnit(Telnet):
    def __init__(self, host, port=0 , timeout=10, mode="user"):
        self._host = host
        unit=Telnet.__init__(self, host)
        print type(unit)

    def login(self, userName="", password="",prompt=""):
        print "in login"
        answer = self.expect([userPrompt,loginPrompt,passwordPrompt])
        print answer
        if answer[0]= -1:
            print "No Response from device"
            return False

        if answer[0]== 0 or answer[0]==1:
            print "enter username"
            self.write(userName + "\n")
        elif answer[0]== 2:
            self.write(password + "\n")

        answer = self.expect([passwordPrompt,execPrompt])

        if answer[0]== 0 :
            print "enter password"
            self.write(password + "\n")
        answer = self.expect([execPrompt])
        self.prompt=str(answer[2]).lstrip()


    def


    def closeConnecttion(self):
        self.close()

if __name__ == '__main__':
    dut=TelnetUnit("10.49.203.11")
    print type(dut)
    dut.login("adtran","adtran")
    dut.close()

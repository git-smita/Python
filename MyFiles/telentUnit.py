from telnetlib import Telnet
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
        Telnet.__init__(self, host)


    def login(self, userName="", password="", prompt=""):
      while (1):
        answer = self.expect([userPrompt,loginPrompt,passwordPrompt,execPrompt])
        if answer[0]== -1:
          print "No Response from device"
          return False
          # Enter Username at Username: or Login: prompt
        elif answer[0]== 0 or answer[0]==1:
          print answer
          print "Enter username"
          self.write(userName + "\n")
          print "Entered username"
          # Enter Password at Password: prompt
        elif answer[0]== 2:
          self.write(password + "\n")
        else:
          self.prompt = str(answer[2]).strip()
          print self.prompt
          break

    def dut_execute_command(self,cmd):
      try:
        self.write(cmd+"\n")
        out=self.expect([self.prompt])
        return out[2]
      except:
        AssertionError("Unable to execute command")

    def dut_interact(self):
      self.interact()

    def closeConnecsttion(self):
      self.close()

    def dut_enable_mode(self,password):
      self.write("enable\r\n")
      output = self.expect([passwordPrompt, enablePrompt])
      print output
      if output[0] == -1:
        print "Unable to enter enable prompt"
        return false
      elif output[0] == 0:
        self.write(password + '\n')
      output = self.expect([enablePrompt])
      self.prompt = str(output[2]).strip()
      print self.prompt


if __name__ == '__main__':
    try:
        dut=TelnetUnit("10.49.203.11")
    except:
        AssertionError("Unable to open connecyion.")
    try:
        dut.login("adtran","adtran")
        dut.dut_enable_mode('adtran')
    except:
        AssertionError("Unable to login to device")

    try:
      output = dut.dut_execute_command("show version")

    except:
      AssertionError("Unable to execute command")

    dut.dut_interact()

    dut.close()




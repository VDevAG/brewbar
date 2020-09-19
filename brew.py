from subprocess import Popen, PIPE, STDOUT, call

class BrewManager:

    def install_software(self, brew_command):
        call(["brew cask uninstall", brew_command, "--force"], shell=True)
    
    def update_software(self):
        call(["brew upgrade --force"], shell=True)

### Setting up a Windows Ansible Node

1. You may create a T2 - Medium ec2 instance with Windows 2019 base AMI

2. Windows Node Ansible Requirments	
     - PowerShell 3.0 or latest
     - .Net Framework 4.5 or latest

### Finding PowerShell version

$PSVersionTable

### Finding .Net Framework Version

1. Open regedit

2. HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full

### Configuring WinRM on Windows machine

$url = "https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"

$file = "$env:temp\ConfigureRemotingForAnsible.ps1"

(New-Object -TypeName System.Net.WebClient).DownloadFile($url, $file)

powershell.exe -ExecutionPolicy ByPass -File $file

### Configuring Windows node with Basic authentication

Set-Item -Path WSMan:\localhost\Service\Auth\Basic -Value $true

### Verify if WinRM Listeners are running ( 2 listerners one for Http and other for Https expected )

winrm enumerate winrm/config/Listener

### On the Ansible Controller machine, make sure pywinrm is installed

pip install "pywinrm>=0.3.0"

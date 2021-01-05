import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("10.10.20.175", username="developer", password="C1sco12345")
status =  ssh.get_transport().is_active()
channel = ssh.invoke_shell()
stdin = channel.makefile('wb')
stdout = channel.makefile('rb')
stdin.write('''
  show version
  ''')

print stdout.read()
print(stderr)
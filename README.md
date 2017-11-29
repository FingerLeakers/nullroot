# nullroot

When the `root` account is not enabled in macOS High Sierra 10.13.1, it is possible to create a root account with a known password that you can then use for whatever you want. This is a PoC `python3` script for exploiting that vulnerability. Please use only on systems that you own or have permission to test on.

This is available as this standalone script or as part of my [kernelpop](https://github.com/spencerdodd/kernelpop) kernel exploitation framework.

### usage

`python3 NULLROOT.py`

[![null-root](https://asciinema.org/a/ZUjyKCfXBgtQUgVCeeC1lr6u6.png "null-root")](https://asciinema.org/a/ZUjyKCfXBgtQUgVCeeC1lr6u6)

### fix

Enable the `root` account (if it is not already enabled) and set the password to a strong password

`System Preferences>Users & Groups>Login Options>Network Account Server (Join)>Open Directory Utility>Edit>Enable Root`

`System Preferences>Users & Groups>Login Options>Network Account Server (Join)>Open Directory Utility>Edit>Change Root Password`
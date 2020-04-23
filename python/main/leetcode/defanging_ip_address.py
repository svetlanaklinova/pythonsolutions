'''Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
https://leetcode.com/problems/defanging-an-ip-address/
'''


def defangIPaddr(address: str) -> str:

    return address.replace('.','[.]')


assert defangIPaddr("255.100.50.0") == "255[.]100[.]50[.]0"
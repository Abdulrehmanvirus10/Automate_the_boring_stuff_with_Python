#! python3
# Password locker program

import sys
import pyperclip
PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}


if len(sys.argv) < 2:
    print('Usage: python password_locker.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account na

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for' + account + "copied to clipboard")
else:
    print('There is no account named ' + account)

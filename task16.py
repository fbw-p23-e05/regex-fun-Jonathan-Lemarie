
# - Task 16 -- Write a Python program to remove leading zeros from an IP address.

import re

pattern = '0*'


ip = '24.055.001.080'

new_ip = re.split(pattern, ip)

#print(new_ip)

#  ---- -----  correction : 

pattern_1 = '0*(\d*)'

ip_address = '024.550.001.080'

new_ip_1 = re.sub(pattern_1, r'\1',ip_address )

print(new_ip_1)


# another option is .. 
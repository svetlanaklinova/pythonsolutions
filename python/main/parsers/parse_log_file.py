'''
parse timestamp from log and record repeatable in new file
'''

import re
from collections import Counter

location = "/Users/svetlanaklinova/box-with-toys/ready-to-cook-recipes/python/main/parsers/"
fname = 'log_file.txt'
outputfileprefix = 'out_'
regex_pattern = "\[(.*)\\s+.*\]"
records = []



    #extract timestamp
with open(f'{location}{fname}',"r") as f:
        for line in f:
            m = re.search(regex_pattern,line.strip())
            if m and m.group(1):
                records.append(m.group(1))
        #print('\n'.join(records)) #debug

records_size = len(records)
if records_size and records_size > len(set(records)): # continue if duplicates exist

        dCounter = Counter(records)
        #print(dCounter)    #debug

        outputfile = f'{location}{outputfileprefix}{fname}'

        # record none-unique records in file
        with open(outputfile, "w") as f:
            for key, value in dCounter.items():
                    if value > 1:
                        f.write(f'{key} {value}\n')

        '''Expected Output:
        31/Mar/2002:19:19:41 2
        31/Mar/2002:19:26:41 2
        31/Mar/2002:19:31:41 3
        '''
else:
    print('no duplicates found')





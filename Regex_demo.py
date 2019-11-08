


import re

tmp = ''
list_tmp = []


''' 
open a file with entries
store them into list_tmp
'''


# =-=--=-=-=-=--=-=-=-=--=-=-=-=--=- read data from a file =-=--=-=-=-=--=-=-=-=--=-=-=-=--=-
with open("test.txt", 'r') as f:
    for line in f:
        for word in line.split():
            list_tmp.append(word)

# trim list by words that describe data
del list_tmp[0:8]

print('\n ALL data ')
print(list_tmp)

Mac_lst = []


print('\n ALL MAC addresses ')
# =-=--=-=-=-=--=-=-=-=--=-=-=-=--=- store mac addresses in list  =-=--=-=-=-=--=-=-=-=--=-=-=-=--=-
# Mac is every 4th entry in list_tmp
for x in range(0,len(list_tmp),4):
    Mac_lst.append(list_tmp[x])

print(Mac_lst)


print('\n MAC addresses follow pattern ')
# =-=--=-=-=-=--=-=-=-=--=-=-=-=--=-  check if MAC address follow pattern  -=-=--=-=-=-=--=-=-=-=--=-=-=-=--=-

#use regex to find MAC adresses according to the pattern
pattern = r'(?:[0-9a-fA-F]:?){12}'

correct_MAC_list = []

correct_MAC_list = re.findall(pattern, str(Mac_lst))

print(correct_MAC_list)

'''

You can use this regex. It checks that the start mark ^ is not followed by abc or def until the end $.

^(?!(abc|def)$).*


'''
'''
this is for gettinga  key for submissions
'''

from microprediction import new_key, MicroWriter

write_key = new_key(difficulty=9)

mw = MicroWriter(write_key=write_key)

print(write_key)

print(mw)

# or just save to file
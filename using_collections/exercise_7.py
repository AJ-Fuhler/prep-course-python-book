info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
new_info = info.split(':')
print('+'.join(new_info))

# found str.replace() method in Python Documentation:

print(info.replace(':', '+'))
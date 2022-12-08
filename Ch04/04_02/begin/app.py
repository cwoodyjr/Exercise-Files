first_name = 'malala'
last_name = 'yousafzai'
note = 'award: Nobel Peace Prize'

firstNameCaps = first_name.capitalize()
lastNameCaps = last_name.capitalize()
# note.capitalize()

print(firstNameCaps)
print(lastNameCaps)

awardLocation = note.find('award:')
print(awardLocation)

awardText = note[7:]
print(awardText)

print('First Name = ' + first_name.capitalize())
print('Last Name = ' + last_name.capitalize())
print(note.capitalize())

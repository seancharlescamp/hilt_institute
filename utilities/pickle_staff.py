import pickle

f = open('staff_info.txt', 'r')
raw_data = f.read()
f.close()

staff = raw_data.split('=++=')

for i, member in enumerate(staff):
    staff[i] = member.split('++')

staff_dict = {}

for member in staff:
    name = member[0].strip()
    full_name = member[1].strip()
    position = member[2].strip()
    description = member[3].strip()
    staff_dict[name] = {'full_name': full_name, 'position': position,
                        'description': description}

pickle.dump(staff_dict, open('staff_info.dat', 'wb'))

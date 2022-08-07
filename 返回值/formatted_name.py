# formatted_name
def get_formatted_name(fist_name, last_name):
    full_name = f"{fist_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# alien
# alien_0 = {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#
# print(alien_0['color'])
# print(alien_0['points'])
# new_points = alien_0['points']
# print(f"You just earned_{new_points} points.")
# print(alien_0)
# alien_0 = {'color': 'green', 'points': 5}
# print(f"The alien is {alien_0['color']}.")
#
# alien_0['color'] = 'yellow'
# print(f"The alien is {alien_0['color']}.")
#
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position:{alien_0['x_position']}")

alien_0['color'] = 'green'
alien_0['points'] = 5
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的移动速度肯定很快
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position:{alien_0['x_position']}")
print(alien_0)
del alien_0['points']
print(alien_0)
# 外星人颜色
green = "green"
red = "red"
yellow = "yellow"
green_fraction = 5
yellow_fraction = 10
red_fraction = 15


alien_color = yellow
if alien_color == green:
    print("恭喜你获得了5分")
if alien_color == red:
    print("恭喜你获得了5分")
if alien_color == green:
    print(f"你因射杀{green}外星人获得了{green_fraction}分")
else:
    print(f"你获得了{10}分")

if alien_color == green:
    print(f"你获得了{green_fraction}分")
if alien_color == yellow:
    print(f"你获得了{yellow_fraction}分")
if alien_color == red:
    print(f"你获得了{red_fraction}分")

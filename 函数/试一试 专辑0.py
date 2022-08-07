def make_album(name, album, song_num=''):
    dict_album = {}
    # 可选参数选择
    if song_num:
        dict_album[name] = album
        dict_album['song_num'] = song_num
    else:
        dict_album[name] = album
    return dict_album


# while循环
while True:
    print("请输入歌手姓名:(输入q退出)")
    name = input()
    if name == 'q':
        break
    print("请输入专辑名称:(输入q退出)")
    album = input()
    if album == 'q':
        break
    # 是否输入可选参数
    print("请选择输入歌曲的编号(Y/N):")
    select_result = input()
    if select_result == 'Y' or 'y':
        print("请输入歌曲编号:")
        song_num = input()
        a = make_album(name, album, song_num)
        print(a)
    elif select_result == 'N' or 'n':
        aa = make_album(name, album)
        print(aa)
    elif select_result == 'q':
        break
    else:
        print("错误的指令")
        continue

# 试一试 专辑
def make_alibum(name, album, song_num=''):
    dict_album = {}
    if song_num:
        dict_album[name] = album
        dict_album['song_num'] = song_num
    else:
        dict_album[name] = album
    return dict_album


a = make_alibum('Jay Chou', 'Mojito')
print(a)

b = make_alibum('Eason Chan', 'The key', '3')
print(b)

c = make_alibum('Li Zhongsheng', 'fanrenge')
print(c)

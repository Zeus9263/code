# 城市
cities = {
    '北京': {
        '简称': '京',
        '人口': '2.19千万人',
        'GDP': 4.03,
    },
    '上海': {
        '简称': '沪',
        '人口': '2.49千万人',
        'GDP': 4.32,
    },
    '广东': {
        '简称': '粤',
        '人口': '1.26亿人',
        'GDP': 12.44,
    },
}
for citie, info in cities.items():
    print(f"城市名:{citie}")
    for ms,ns in info.items():
        print(f"{ms} : {ns}")
    print("\n")

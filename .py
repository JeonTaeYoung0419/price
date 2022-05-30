def shopping(shop_file):
    with open(f'data/{shop_file}') as f:
      shop_list = list((f.read()).split("\n"))
    shop_dict = {} # 생성할 사전 객체
    
    for a in range(2,len(shop_list)-1):
      key,value = list(shop_list[a].split())
      value.replace("원","")
      shop_dict[key] = int(value[:-1])

    return shop_dict
def item_price(shop_file, item):
    return shopping(shop_file)[item]

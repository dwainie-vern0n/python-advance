import requests

so_luong = int(input('Nhập số lượng công việc bạn muốn tạo: '))

keylist = list()

def worklist():
    url = 'https://www.boredapi.com/api/activity'

    res = requests.get(url)
    data = res.json()

    return(data)

# data2 = worklist()
# key = data2['key']
# print(key)

for i in range(0,so_luong):
    data2 = worklist()
    key = data2['key']
    type = data2['type']
    activity = data2['activity']
 

    # truong hop trung
    if key in keylist: 
        so_luong += 1
      
    else:
        keylist.append(key)
        print(type+': '+activity)


from datetime import datetime
giay=0
phut = 0
giayquakhu =0
def dem_thoigian():
    global giayquakhu, giay, phut
    now = datetime.now()
    giayhientai = now.strftime("%S")
    if giayhientai != giayquakhu:
        giayquakhu = giayhientai
        giay = giay + 1
        if giay ==60:
            phut +=1
            giay = 0
            if phut == 60:
                phut=0
    return giay, phut

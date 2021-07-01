import zlib


def get_table_index(plat_openid):
    mod = zlib.crc32(plat_openid.encode('utf8')) % 128
    if mod < 10:
        print("00" + mod.__str__())
    elif mod < 100:
        print("0" + mod.__str__())
    else:
        print(mod.__str__())


if __name__ == '__main__':
    get_table_index("51E3C765B4DEECA663A9EA294703B99F")

from hashlib import md5

secret_key = "yzbqklnj"
running = True


for num in range(10000000):
    key = secret_key + f"{num}"

    res = md5(key.encode())
    pes = res.hexdigest()

    if "000000" in pes[:6]:
        print(key)
        print(num)
        print(pes)
       
        break
    
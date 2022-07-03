from hashlib import md5

#secret_key = "abcdef"
secret_key = "yzbqklnj"
running = True


for num in range(1000000):
    key = secret_key + f"{num}"

    res = md5(key.encode())
    pes = res.hexdigest()

    if "00000" in pes[:5]:
        print(key)
        print(num)
        print(pes)
       
        break
    

        

        
        
    
        






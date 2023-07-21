import random

print("be barname addad random khosh amadid")
AdAval=int(input("addadi ke mikhahid az in baze shorow she: "))
AdAkhar=int(input("addadi ke mikhahid to in baze tamom she: "))
Tedad=int(input("tedad addad ra vared konid: "))
TeddadKol=int(AdAkhar-AdAval-2)
if Tedad>TeddadKol :
    print("error!teddad entekhab shode ba addad bein do addad azal va akhar yeki nist")
else :
    arraye=[]
    while Tedad > 0:
        RandAd=random.randint(AdAval,AdAkhar)
        if not(RandAd in arraye):
            arraye.append(RandAd)
            Tedad -= 1
print(arraye)
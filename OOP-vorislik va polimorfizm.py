class Shaxs:
    def __init__(self,ism,familya,passport,tyil):
        self.name=ism
        self.surname=familya
        self.passport=passport
        self.byear=tyil

    def get_info(self):
        info=f"{self.name.title()} {self.surname.capitalize()}."
        info +=f"Passport :{self.passport},{self.byear}-yilda tug'ilgan"
        return info
    def get_age(self,yil):
        return yil-self.byear

inson=Shaxs('ahmad','ochilov','AB93233434',2006)
print(f"{inson.get_info()}.{inson.get_age(2024)} yoshda")

class Talaba(Shaxs):
    def __init__(self,name,surname,passport,byear):#xususiyat
        super().__init__(name,surname,passport,byear)
        #super klassdan xususiyatlarni meros olyabmiz
        #argumentlar bilan xususiyatlarni bog'lash shart emas

talaba=Talaba('abbos','xidirov','AA3421212',2007)
print(talaba.get_info())
print(talaba.get_age(2022))

class Talaba(Shaxs):
    def __init__(self,name,surname,passport,byear,idraqam):#xususiyat
        super().__init__(name,surname,passport,byear)
        self.idraqam=idraqam
        self.bosqich=1

    def get_id(self):# bu metod voris klassni o'zini metodi hisoblanadi
        return f"Idraqam:{self.idraqam}"

    def get_bosqich(self):
        return f"{self.bosqich} bosqich talabasi"
    def update_bosqich(self):
       self.bosqich += 1

talaba1=Talaba('mahmud','akbarov',"AC3492002",2006,'333012')

print(talaba1.get_info())
print(talaba1.get_id())
print(talaba1.get_bosqich())
talaba1.update_bosqich()
print(talaba1.get_bosqich())

class Sportchi(Shaxs):
    def __init__ (self,name,surname,passport,byear,vazn):
        super().__init__(name,surname,passport,byear)
        self.vazn=vazn
        self.tajriba=2
    def get_vazn(self):
        return f"{self.vazn} kg"
    def get_tajriba(self):
        return f"{self.tajriba} yillik tajribaga ega"

odam=Sportchi('murod','azimov',"AB784424",2003,79)
print(odam.get_vazn())
print(odam.get_tajriba())

class Kurash(Sportchi):
    def __init__(self,name,surname,passport,byear,vazn,boy):
        super().__init__(name,surname,passport,byear,vazn)
        self.length=boy
bola=Kurash('javohir','odilov',"AB453240",2007,59,170)
print(bola.get_info())
# bu HOLATDA VORIS KLASSDAN SUPER KLASS SIFATIDA FOYDALANIB VORIS KLASS YARATDIK
#VA UNDAN OBYEKT YARATDIK

#POLIMARFIZM
print(talaba.get_info())


class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
    def get_id(self):
        return self.idraqam
    def get_bosqich(self):
        return self.bosqich

    def get_info(self):#NOMI SAQLANIB ICHI O'ZGARTIRILADI
        info=f"{self.name.title()} {self.surname.title()}. "
        info+=f"{self.get_bosqich()}-bosqich.ID raqam:{self.get_id()}"
        return info

talaba=Talaba('ahmad','ochilov',"Ab54248480",2006,'4342201')
print(talaba.get_info())

class Manzil:
    def __init__(self,uy,kocha,tuman,viloyat):
        self.uy=uy
        self.kocha=kocha
        self.tuman=tuman
        self.viloyat=viloyat

    def get_manzil(self):
        manzil=f"{self.viloyat.title()} viloyati {self.tuman} tumani,"
        manzil+=f" {self.kocha} kochasi,{self.uy}-uy"
        return manzil

class Talaba(Shaxs):
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam=idraqam
        self.manzil=manzil
        self.bosqich=1

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.name} {self.surname}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info

talaba_manzil=Manzil(7,'zarafshon','paxtakor','samarqand')
talaba2=Talaba('Akmal','Berdiyev',"AA7534221",1993,'432313',talaba_manzil)

print(talaba2.manzil.get_manzil())
print(talaba2.manzil.tuman)


class People:
    def __init__(self,info,pnumber):
        self.info=info
        self.number=pnumber
    def get_phonenumber(self):
        return self.number

class Information:
    def __init__(self,name,surname,byear,):
        self.name=name
        self.surname=surname
        self.byear=byear

    def get_age(self,year):
        return year-self.byear
    def get_info(self,year):
        mal=f"{self.name.title()} {self.surname.title()}"
        mal+=f" is {self.get_age(year)} years old"
        return mal
infm=Information('abbos','rustamov',2005)
print(infm.get_age(2024))
print(infm.get_info(2024))

person=People(infm,'232311782')
print(person.get_phonenumber())
print(person.info.get_info(2025))
print(person.info.name)






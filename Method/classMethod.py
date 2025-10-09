class Mobil:
    def  __init__ (self, merek):
        self.merek = merek

    @classmethod
    def intro_mobil():
        print ("Ini adalah metode dari class mobil")

Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
Mobil.intro_mobil()
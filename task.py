class BankHesabi:
    def __init__(self, hesab_nomresi, balans):
        self.hesab_nomresi = hesab_nomresi
        self.balans = balans

    def pul_elave_et(self, mebleq):
        self.balans += mebleq
        print(f"{mebleq} AZN pul hesaba əlavə edildi. Yeni balans {self.balans} AZN.")

    def pul_cek(self, mebleq):
        if self.balans >= mebleq:
            self.balans -= mebleq
            print(f"{mebleq} AZN pul çıxarıldı! Yeni balans {self.balans} AZN.")
        else:
            print("Kifayət qədər vəsait yoxdur!")

    def balans_goster(self):
        print(f"Hesab Nömrəsi: {self.hesab_nomresi}\nCari Balans: {self.balans} AZN")

class KreditHesabi(BankHesabi):
    def __init__(self, hesab_nomresi, balans, kredit_meblegi):
        super().__init__(hesab_nomresi, balans)
        self.kredit_meblegi = kredit_meblegi

    def kredit_al(self):
        self.balans += self.kredit_meblegi
        print(f"{self.kredit_meblegi} AZN kredit hesabınıza əlavə olundu. Yeni balans {self.balans} AZN.")

    def kredit_odeme(self):
        ayliq_odenis = self.kredit_meblegi // 12
        if self.balans >= ayliq_odenis:
            self.balans -= ayliq_odenis
            print(f"{ayliq_odenis} AZN kreditin ödənişi uğurla tamamlandı. Yeni balans {self.balans} AZN.")
        else:
            print("Krediti ödəmək üçün kifayət qədər vəsait yoxdur!")

if __name__ == "__main__":
    hesab1 = BankHesabi(1122334455, 5500)
    hesab1.balans_goster()
    hesab1.pul_elave_et(500)
    hesab1.pul_cek(200)
    hesab1.balans_goster()

    hesab2 = KreditHesabi(5511223344, 100, 5510)
    hesab2.balans_goster()
    hesab2.kredit_al()
    hesab2.balans_goster()
    hesab2.kredit_odeme()
    hesab2.balans_goster()
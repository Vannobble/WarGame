class Hero:
    def __init__(self, name, health, power, armor):
        self.name = name
        self.health = health
        self.power = power
        self.armor = armor
        self.base_power = power 

    def attack(self, enemy):
        print(f"{self.name} menyerang {enemy.name}")
        enemy.defend(self, self.power)

    def defend(self, enemy, attack_power):
        damage = attack_power / self.armor
        self.health -= damage
        print(f"{self.name} bertahan dari {enemy.name}. Serangan diterima: {damage:.2f}. Darah tersisa: {self.health:.2f}")

    def heal(self):
        self.health += 20
        print(f"{self.name} memulihkan 20 Health. Health sekarang: {self.health:.2f}")

    def buff(self):
        self.power *= 1.5
        print(f"{self.name} mendapatkan Buff! Power sekarang: {self.power:.2f}")

    def reset_power(self):
        self.power = self.base_power


heroes = [
    Hero("Colossus", 200, 10, 300),
    Hero("Banshe", 150, 70, 150),
    Hero("Dagon", 100, 150, 10),
    Hero("Clover", 100, 100, 100),
    Hero("Succubus", 130, 200, 20),
    Hero("Elf", 50, 100, 20),
    Hero("Bear", 50, 100, 20)
]


def player_action(hero1, hero2):
    actions = {1: hero1.attack, 2: hero1.heal, 3: hero1.buff}
    choice = int(input("\n1. Menyerang\n2. Mengheal\n3. Buff\nPilih aksi: "))
    actions.get(choice, lambda: print("Input salah"))(hero2)


def select_hero(player_num):
    print(f"Pilih karakter pemain {player_num}:")
    for i, hero in enumerate(heroes, 1):
        print(f"{i}. {hero.name} - Health: {hero.health}, Power: {hero.power}, Armor: {hero.armor}")
    
    while True:
        choice = int(input("Masukkan nomor hero pilihan Anda: ")) - 1
        if 0 <= choice < len(heroes):
            return heroes[choice]
        print("Pilihan tidak valid. Silahkan pilih lagi.")


def main():
    print("Selamat datang di War Game\n")
    hero1, hero2 = select_hero(1), None
    while hero2 is None or hero2 == hero1:
        hero2 = select_hero(2)
        if hero2 == hero1:
            print("Hero sudah dipilih oleh pemain pertama. Silahkan pilih hero lain.")

    while hero1.health > 0 and hero2.health > 0:
        print("\n--- Giliran Pemain Pertama ---")
        player_action(hero1, hero2)
        if hero2.health <= 0:
            print(f"{hero2.name} kalah! {hero1.name} menang!")
            break
        print("\n--- Giliran Pemain Kedua ---")
        player_action(hero2, hero1)
        if hero1.health <= 0:
            print(f"{hero1.name} kalah! {hero2.name} menang!")
            break

    hero1.reset_power()
    hero2.reset_power()


if __name__ == "__main__":
    main()

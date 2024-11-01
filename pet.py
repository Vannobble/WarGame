#!/usr/bin/env python3
import random
import time

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50
        self.happiness = 50
        self.energy = 50

    def feed(self):
        if self.hunger < 100:
            self.hunger += 10
            self.happiness += 5
            print(f"{self.name} makan dan merasa lebih baik!")
        else:
            print(f"{self.name} sudah kenyang!")
        self.status()

    def play(self):
        if self.energy > 0:
            self.happiness += 10
            self.hunger -= 5
            self.energy -= 10
            print(f"{self.name} bermain dan terlihat bahagia!")
        else:
            print(f"{self.name} terlalu lelah untuk bermain.")
        self.status()

    def rest(self):
        if self.energy < 100:
            self.energy += 20
            self.hunger -= 5
            print(f"{self.name} beristirahat dan energinya pulih.")
        else:
            print(f"{self.name} sudah cukup beristirahat!")
        self.status()

    def status(self):
        print(f"\nStatus {self.name}:")
        print(f"Hunger: {self.hunger}/100")
        print(f"Happiness: {self.happiness}/100")
        print(f"Energy: {self.energy}/100")
        print("")

    def auto_decrease(self):
        """Simulasikan penurunan status secara otomatis untuk setiap 'waktu'."""
        self.hunger -= random.randint(5, 15)
        self.happiness -= random.randint(3, 8)
        self.energy -= random.randint(5, 10)

        if self.hunger < 0:
            self.hunger = 0
        if self.happiness < 0:
            self.happiness = 0
        if self.energy < 0:
            self.energy = 0

        self.check_status()

    def check_status(self):
        if self.hunger <= 10:
            print(f"{self.name} sangat lapar!")
        if self.happiness <= 10:
            print(f"{self.name} merasa sedih.")
        if self.energy <= 10:
            print(f"{self.name} sangat lelah.")

# Main loop
def main():
    name = input("Berikan nama untuk hewan peliharaan Anda: ")
    species = input("Jenis hewan peliharaan (misal: anjing, kucing, dll.): ")

    pet = Pet(name, species)

    print(f"\nAnda sekarang memiliki {species} bernama {name}!")
    pet.status()

    actions = {
        "1": pet.feed,
        "2": pet.play,
        "3": pet.rest
    }

    while True:
        print("\nPilih aksi:")
        print("1. Beri makan")
        print("2. Bermain")
        print("3. Istirahatkan")
        print("4. Keluar")

        choice = input("Masukkan pilihan Anda (1-4): ")

        if choice == "4":
            print(f"Sampai jumpa, {name} akan merindukanmu!")
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Pilihan tidak valid. Coba lagi.")
        
        time.sleep(1)  # Pause untuk simulasi waktu
        pet.auto_decrease()

main()

print("=====================================")
print("   PROGRAM HITUNG BANGUN RUANG")
print("=====================================")
print("1. Balok (20, 4, 8)")
print("2. Kubus (15)")
print("3. Limas Segi Empat (6, 8)")
print("4. Tabung (3, 12)")
print("5. Bola (1)")
print("=====================================")

pilihan = int(input("Masukkan pilihan (1-5): "))

match pilihan:
    case 1:
        print("\n--- Balok ---")
        print("Volume = 640")
        print("Luas Permukaan = 544")

    case 2:
        print("\n--- Kubus ---")
        print("Volume = 3375")
        print("Luas Permukaan = 1350")

    case 3:
        print("\n--- Limas Segi Empat ---")
        print("Volume = 96")
        print("Luas Permukaan = 132")

    case 4:
        print("\n--- Tabung ---")
        print("Volume = 339.12")
        print("Luas Permukaan = 282.6")

    case 5:
        print("\n--- Bola ---")
        print("Volume = 4.19")
        print("Luas Permukaan = 12.56")

    case _:
        print("\nPilihan tidak tersedia!")
def deviation(filename):
    # Array untuk menyimpan semua angka
    numbers = []

    # Inisialisasi total dan jumlah data
    total = 0
    count = 0

    # Membuka file
    with open(filename, "r") as file:

        # Loop sampai akhir file
        for line in file:
            # Membaca angka dari file
            number = float(line.strip())

            # Menyimpan angka ke dalam array
            numbers.append(number)

            # Menambahkan angka ke total
            total += number

            # Menambah jumlah data
            count += 1

    # Menghitung rata-rata
    average = total / count

    # Menampilkan rata-rata
    print("Average:", average)

    print()
    print("Number\tDeviation from Average")
    print("--------------------------------")

    # Loop untuk menghitung deviasi setiap angka
    for number in numbers:
        # Menghitung deviasi dari rata-rata
        dev_from_ave = number - average

        # Menampilkan angka dan deviasinya
        print(number, "\t", dev_from_ave)


# Main program
if __name__ == "__main__":
    deviation("numbers.txt")
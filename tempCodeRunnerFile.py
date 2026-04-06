#Simple Library Manager

jumlahBuku = 0
listjudulBuku = []

def tambah_buku(banyakBuku):
    for i in range (banyakBuku):
        judulBuku = input("Input judul buku: ").lower()
        listjudulBuku.append(judulBuku)
    return True 

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1

while True:
    print("Hello, there.\n")
    print("We got your list: \n")
    print("1. Input your data (and program will automatically sort 'em all)\n")
    print("2. Search a title\n")
    print("3. Delete 'em from your list\n")
    print("4. Print your sorted list, huh?\n")
    print("5. Exit the program")
    userChoice = int(input("Wanna go? Type here the number you pick: "))

    if userChoice == 1:
        banyakBukuUser = int(input("Berapa banyak buku Anda ingin tambahkan? "))
        variabel_penampung = tambah_buku(banyakBukuUser)
        listjudulBuku.sort()
    elif userChoice == 2:
        searchingABook = input("What is the title of the book you're searching for? ").lower()
        isFound = binary_search(listjudulBuku, searchingABook)

        if isFound != -1:
            print("In the list you created, it's found!\n")
        else:
            print("Sorry, we do afford yet we can't find it for you for now.\n")
    elif userChoice == 3:
        deletingABook = input("What is the title of the book you'd like to delete from? ").lower()
        if deletingABook in listjudulBuku:
            listjudulBuku.remove(deletingABook)
            print("The book is already deleted from the list!\n")
        else:
            print("Can't find the book you'd like to delete from the list, sorry.\n")
    elif userChoice == 4:
        print(f"This is your sorted list: {listjudulBuku}")
    elif userChoice == 5:
        print("Thank you for using this program, see ya in the future!\n")
        break
    else:
        print("Hey, error input detected. Stay aware, please in inputting the number menu you pick.\n")
        continue
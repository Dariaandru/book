import psycopg2
conn = psycopg2.connect(database="books", user="postgres",
    password="123", host="localhost", port=5432)

cur = conn.cursor()

# cur.execute("CREATE TABLE book (id SERIAL PRIMARY KEY, " +
#     "name VARCHAR(100), author VARCHAR(100), year INTEGER, genre VARCHAR(100), pages INTEGER)")
# conn.commit()

def error(per):
    try:
        per = int(per)
    except ValueError:
        print("Input the number")
        return False
    return True



def add():
    book_name = input("Name:    ")
    book_author = input("Author:    ")
    while True:
        book_year = input("Year:    ")
        if (error(book_year)):
            break
    
    book_genre = input("Genre:  ")
    while True:
        book_pages = input("Pages:  ")
        if (error(book_pages)):
            break

    cur.execute("INSERT INTO book (name, author, year, genre, pages) VALUES (%s, %s, %s, %s, %s)", (book_name, book_author, book_year, book_genre, book_pages))
    conn.commit()
    
def print_all():
    print("\nALL BOOKS:\n")
    cur.execute("SELECT * FROM book")
    for row in cur:
        print(f" Book #{row[0]}\n Name: {row[1]}\n Author: {row[2]}\n Year: {row[3]}\n Genre: {row[4]}\n Pages: {row[5]}\n\n")


def delete():
    while True:
        id_book = input("Id:    ")
        if (error(id_book)):
            break
    cur.execute("DELETE FROM book WHERE id = %s", (id_book,))
    conn.commit()

def search_by_name():
    book_name = input("Name:    ")
    print(f"\nBooks named {book_name}")
    cur.execute("SELECT * FROM book WHERE name = %s", (book_name,))
    for row in cur:
        print(f" Book #{row[0]}\n Author: {row[2]}\n Year: {row[3]}\n Genre: {row[4]}\n Pages: {row[5]}\n\n")


def search_by_author():
    book_author = input("Author:    ")
    print(f"\nBooks of {book_author}")
    cur.execute("SELECT * FROM book WHERE author = %s", (book_author,))
    for row in cur:
        print(f" Book #{row[0]}\n Name: {row[1]}\n  Year: {row[3]}\n Genre: {row[4]}\n Pages: {row[5]}\n\n")

def update():
    while True:
        id_book = input("Id:    ")
        if (error(id_book)):
            break
    cur.execute("SELECT id FROM book WHERE id = %s", (id_book,))
    # print(cur.rowcount)
    if (cur.rowcount == 0):
        print("Id is not exists")
        return

    book_name = input("Name:    ")
    book_author = input("Author:    ")
    while True:
        book_year = input("Year:    ")
        if (error(book_year)):
            break
    
    book_genre = input("Genre:  ")
    while True:
        book_pages = input("Pages:  ")
        if (error(book_pages)):
            break

    cur.execute("UPDATE book SET name = %s, author = %s, year = %s, genre = %s, pages = %s WHERE id = %s", (book_name, book_author, book_year, book_genre, book_pages, id_book))
    conn.commit()



def menu():
    print("--------------------------------------")
    print("1. Add book\n2. Delete book\n3. Search by author\n4. Search by name\n5. Update book by id\n6. Print all books\n7. Exit")
    print("--------------------------------------")


while True:
    menu()
    choice = input("Enter your choice:  ")
    try:
        choice = int(choice)
    except ValueError:
        print("Incorrect input")
    if (choice == 1):
        add()
    elif (choice == 2):
        delete()
    elif (choice == 3):
        search_by_author()
    elif (choice == 4):
        search_by_name()
    elif (choice == 5):
        update()
    elif (choice == 6):
        print_all()
    elif (choice == 7):
        break
    else:
        print("Choice is not exists")
    
conn.close()

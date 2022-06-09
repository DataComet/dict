#from gettext import translation
import psycopg2
conn = psycopg2.connect(
   host="localhost",
   database="dict",
   user="dic",
   password="abc123"
)
#Reads dictionary
def read_dict(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, word, translation FROM dictionary;")
    rows = cur.fetchall()
    cur.close()
    return rows
#Adds words into the dictionary
def add_word(conn, word, translation):
    cur = conn.cursor()
    cur.execute(f"INSERT INTO dictionary (word, translation) VALUES ('{word}', '{translation}');")
    cur.close()
#Deletes words from the dictionary
def delete_word(conn, ID):
    cur = conn.cursor()
    cur.execute(f"DELETE FROM dictionary WHERE id = '{ID}';")
    cur.close()
#Saving down the changes
def save_dict(conn):
    cur = conn.cursor()
    cur.execute("COMMIT;")
    cur.close()

help = '''Hello and welcome to the dictionary, available commands:
  add    - add word
  delete - delete word
  list   - list all in the dictionary
  quit   - quit the program'''
print(help)

def main():
    while True: ## REPL - Read Execute Program Loop
        cmd = input("Command: ").lower().strip()
        if cmd == "list":
            print('Here is the list: ')
            print(read_dict(conn))
        elif cmd == "add":
            word = input("  Word: ")
            translation = input("  Translation: ")
            add_word(conn, word, translation)
            print(f" The word: {word} is added, and the is translation is {translation}.")
        elif cmd == "delete":
            ID = input("  ID: ")
            delete_word(conn, ID)
            print(f" Deleted ID {ID}")
        elif cmd == "quit":
            save_dict(conn)
            print('It is saved!')
            exit()
main()


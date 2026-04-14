import sqlite3
<<<<<<< HEAD
conn=sqlite3.connect('finance.db')
c=conn.cursor()

def main():
    
    c.execute("""

CREATE TABLE IF NOT EXISTS finances(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              Transaction_type TEXT,
              Amount INTEGER,
              Category TEXT,
              Date TEXT,
              Note TEXT)

""" )
   
=======


def main():
    conn=sqlite3.connect(':memory:')
    c=conn.cursor()
    c.execute("""
         CREATE TABLE IF NOT EXISTS customers(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          Income INTEGER,
          Expence INTEGER,
          Amount INTEGER,
          Category TEXT,
          Date TEXT,
        Any Note TEXT
          
        
          )
          """)
>>>>>>> b42c4a5 (New projet direction , now it's a movie tracking system)
    print("Welcome to Finance CLI")
    Option_number=0
    print("1: Add transaction")
    print("2: Calculate Balance")
    print("3: List Transactions")
    print("4: Exit")
    while(Option_number!=4):
<<<<<<< HEAD
        while True:
            try:
                Option_number=int(input("Enter a choice by typing 1 , 2 , 3 , 4 :"))
                if Option_number in range(1,5):
                    break
                else:
                    print("Enter a number between 1-4.")
            except ValueError:
                print("Enter an integer.")
=======

        Option_number=int(input("Enter a choice by typing 1 , 2 , 3 , 4 :"))
        
>>>>>>> b42c4a5 (New projet direction , now it's a movie tracking system)
        match Option_number:
            case 1:
                add_transaction()
            case 2:
                calculate_balance()
            case 3:
                list_transactions()
<<<<<<< HEAD

def add_transaction():
    while True:
        try:
            Transaction_type=input("Type of transaction.(Income or Expense): ").lower()
            if Transaction_type!="income" and Transaction_type!="expense":
                print("Enter either income or expense.")
            else:
                break
        except ValueError:
            print("Enter a string , either income or expense.")
    while True: 
        try:
            Amount=int(input("Enter the Amount: "))
            break
        except ValueError:
            print("Enter an integer amount.")
    Date=input("Enter a date (dd/mm/yyyy): ")
    Note=input("Enter a note: ")
    Category=input("What was the category: ")
    
   
        

    finances=[(Transaction_type ,Amount,Category,Date, Note)]
    c.executemany("""
    INSERT INTO finances (Transaction_type ,Amount , Category , Date , Note)
           
           VALUES (?,?,?,?,?)
           """,finances
          )
    conn.commit()

=======
            
        
        


def add_transaction():
    
>>>>>>> b42c4a5 (New projet direction , now it's a movie tracking system)
    


def calculate_balance():
 
    c.execute("""
              SELECT SUM(Amount) FROM finances
              WHERE Transaction_type='income'

                """)
    income=c.fetchone()
    income_total = income[0] if income[0] is not None else 0
################################################################

    c.execute("""SELECT SUM(Amount) FROM finances
                WHERE Transaction_type='expense'
""")
    expense=c.fetchone()
    expense_total = expense[0] if expense[0] is not None else 0
      

    balance=income_total-expense_total
    print("\nYour Balance: ₹", balance)
    
    

def list_transactions():
    pass


if __name__ == "__main__":
    main()  
                  
                  
                     


    
    






        


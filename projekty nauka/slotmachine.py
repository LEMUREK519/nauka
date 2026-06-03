
def spin():
   pass

def row():
   pass

def get_payout():
   pass

def main():
    balance = 100

    print("-----------SLOT MACHINE------------") 
    print("Welcome to the slot machine!")
    print("symbols: 🍒, 🍉, 🥒, 🦴, 🍌")
    print("--------------------------------")

    while balance > 0:
        print (f"Your current balance is: ${balance:.2f}")
        
        bet = input("Enter your bet (q to quit): ")

        if not bet.isdigit():
            print("Please enter a valid number.")
            continue
           

if __name__ == "__main__":
   main()test
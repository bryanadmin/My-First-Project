s = []

while True:
    start = input("1. I have SQB Card:\n2. Create new SQB Card:\n3. To quit:\n:")
    if start.isalpha():
      print("\nPut number !\n")

    elif start == '2':
        a = []
        b = []
        new_card = int(input("Write your new card: "))
        new_card_password = int(input("Write your new code: "))
        for_card = str(new_card)
        for_password = str(new_card_password)
        if len(for_card) != 10 or len(for_password) != 4:
            print("\nWrite 10 digit number and 4 digit password!\n")
        else:
          d = new_card, new_card_password
          s.append(d)
          print("\nSuccesfully created new SQB card\n")
    elif start == '1':
        card = input("Write your card: ")
        card_password = input("Card password: ")
        test = int(card), int(card_password)
        if test in s:
          class something():

            def __init__(self, balans = 0.0):
              self.balans = balans

            def put(self):
              put = int(input("How much money do you want to put: "))
              self.balans = self.balans + put
              print(f"\nYour balans {self.balans}")

            def take(self):
              print("Commission 1%")
              take = int(input("How much money do you want to take: "))
              if take*1.01 > self.balans:
                  print("\nYou do not have enough money")
              else:
                self.balans = self.balans - take*1.01
                print(f"\nYour balans {self.balans}")

            def send(self):
              print("Commission 1%")
              id_card = int(input("Put the recipient's card: "))
              card_id = str(id_card)
              len_ = len(card_id)
              if len(card_id) != 10:
                  print(f"\n{len_} digit number does not exist !\n")
              else:
                send = int(input("How much money do you want to send: "))
                if send*1.01 > self.balans:
                  print("\nYou do not have enough money")
                else:
                  self.balans = self.balans - send*1.01
                  print(f"\nSuccesfully sended to this {id_card} user !")
                  print(f"\nYour balans {self.balans}")

          t = something()

          
          while True:
              print("""
   1. To check your balans
   2. To put the money
   3. To take the money
   4. To send the money
   5. Go back """)

              x = input("Select an item: ")
              if x.isalpha():
                print("\nPut number !\n")

              elif x == '1':
                  print(f'Your balans {t.balans}')

              elif x == '2':
                  t.put()

              elif x == '3':
                  t.take()


              elif x == '4':
                  t.send()

              elif x == '5':
                print("")
                break

              else:
                print("\nNo module\n")
        
        elif test not in s:
            print("")
            print("No SQB card !\n")
    
    elif start == '3':
      print("Thanks for using SQB Bank !")
      break
    
    else:
      print("\nNo module\n")
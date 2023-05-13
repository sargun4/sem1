# address_book = {'Aditya': [{'address': 'gurugram', 'phone_no': '9998801243', 'email': 'adityag454@gmail.com'}, 
                # {'address': 'a', 'phone': 'd', 'email': 's'}], 
                # 'Abhisheikh': [{'address': 'pune', 'phone_no': '9123651921', 'email': 'abhiben111@gmail.com'}], 
                # 'Ayushman': [{'address': 'delhi', 'phone_no': '9197903945', 'email': 'bi2342@gmail.com'}], 
                # 'Sudan': [{'address': 'noida', 'phone_no': '9197881953', 'email': 'suddas911@gmail.com'}, 
                # {'address': 'a', 'phone': 's', 'email': 'd'}],
                #  'Dev': [{'address': 'raipur', 'phone': '9845637283', 'email': 'aw@gmail.com'}]}

address_book={}  #name as key & list of dicts as values-to handle multiple ppl w same name
def add_entry(name, address, phone, email):
    if name in address_book:
        # If there are multiple persons with the same name, append to list
        address_book[name].append({'address': address, 'phone': phone, 'email': email})
    else:
        #else, add a new key-value pair to dict
        address_book[name] = [{'address': address, 'phone': phone, 'email': email}]
    return None

# Function to delete an entry
def del_entry(name):
    if name in address_book:
        del address_book[name]
        print(name + " has been deleted from the address book.")
    else:
        print(name + " not found in the address book.")
    return None

# Function to find all matching entries
# def find_matches(partial_name):
#     matches = {}
#     for name in address_book:
#         if partial_name in name:
#             matches[name] = address_book[name]
#     return matches


def partial(dict, partial_name):
    return ("Matching entries : ", [s.lower() for s in dict if partial_name in s])

# Function to find an entry by phone or email
def search_phone_or_email(phone_or_mail_entry):
    for name in address_book:
        for entry in address_book[name]:
            if phone_or_mail_entry in entry.values():
                return name, entry
    return None

with open('addrbook.txt', 'r') as f:
    address_book=eval(f.read())
    print(address_book)

print("Select an option:")
print("1. Insert a new entry.")
print("2. Delete an existing entry.")
print("3. Find all matching entries given a partial name.")
print("4. Find an entry by phone or email.")
print("5. Exit.")

while 1:
    d = (input("Press 1 for more options or enter to exit : "))
    if d == "":
        with open('addrbook.txt', 'w') as f:
            f.truncate()
            f.write(str(address_book))
            # address_book=eval(f.read())
            # print(address_book)

        print("Enter pressed")
        print("-----END-----")
        break
    else:
        pass

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter the name: ")
        address = input("Enter the address: ")
        phone = input("Enter the phone number: ")
        email = input("Enter the email address: ")
        add_entry(name, address, phone, email)
    elif choice == "2":
        name = input("Enter the name: ")
        del_entry(name)
    elif choice == "3":
        partial_name = input("Enter the partial name: ")
        matches = partial(address_book,partial_name)
        print(matches)
    elif choice == "4":
        phone_or_mail_entry = input("Enter the phone number or email: ")
        entry = search_phone_or_email(phone_or_mail_entry)
        if entry:
            print(entry[0] + ": " + str(entry[1]))
        else:
            print("Next operation")
            pass
    elif choice == "5":
        print("-----END-----")
        break


contacts = {}
count = int(input("Enter number of contacts: "))
for i in range(count):
    print(f"\nEnter details for Contact {i + 1}")

    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone
print("\n========== Contact Book ==========")
for person, number in contacts.items():
    print("\n-------------------")
    print("Name  :", person)
    print("Phone :", number)
import json

def save_file(contact:dict, filename:str):
    with open(filename, "a")as f:
        json.dump(contact, f)

name= input("What is your contact name:")
email= input("What is your contact's email?")
phone= input("What is your contact's phone number?")
relationship = input("What is your relationship with contact?")
contact = {
    "name": name,
    "email":email,
    "phone":phone,
    "relationship":relationship

}
save_file(contact, "contact.json")

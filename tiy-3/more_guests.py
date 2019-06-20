guest_list = ["Great Grand Dad Cap", "Auntie Helen", "My Mother's Father", "Myrakle", "Martae"]

def display_invitation(message_key):
    for guest in guest_list:
        messages = {"invitation" : "Shalom " + guest + " I am inviting you to dinner, God has blessed me to be connected to you and I would like to spend time with you.",
        "update_notice": "Hello Again " + guest + " I am sending a message to give you a brief update that more beautiful people will be joining us. As a result, will have a bigger table for the dinner."}
        print(messages[message_key])

guest_no_go = 'Martae'
index_of_guest_no_go = guest_list.index('Martae')



if __name__ == '__main__':
    display_invitation("invitation")
    print('********************************')
    print(guest_no_go + " can't make it to the dinner.")
    print(index_of_guest_no_go)
    guest_list.remove(guest_no_go)
    display_invitation("update_notice")
    guest_list.insert(0, "Dominica")
    guest_list.insert(3, "Marcus")
    guest_list.append("Grant Grandmother")
    print('********************************')
    display_invitation("invitation")

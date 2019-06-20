guest_list = ["Great Grand Dad Cap", "Auntie Helen", "My Mother's Father", "Myrakle", "Martae"]
guest_message_1 = "Shalom " + guest_list[0] + " I am inviting you to dinner, God has blessed me to be connected to you and I would like to spend time with you."
guest_message_2 = "Shalom " + guest_list[1] + " I am inviting you to dinner, God has blessed me to be connected to you and I would like to spend time with you."
guest_message_3 = "Shalom " + guest_list[2] + " I am inviting you to dinner, God has blessed me to be connected to you and I would like to spend time with you."
guest_message_4 = "Shalom " + guest_list[3] + " I am inviting you to dinner, God has blessed me to be connected to you and I would like to spend time with you."
guest_message_5 = "Shalom " + guest_list[4] + " I am inviting you to dinner, God has blessed me to be connected to you and I would like to spend time with you."

guest_no_go = 'Martae'
index_of_guest_no_go = guest_list.index('Martae')


# index_of_guest_no_go = guest_list[guest_no_go]
def display_invitation():
    for guest in guest_list:
        print("Shalom " + guest + " I am inviting you to dinner, God has blessed me to be connected to you and I would like to spend time with you.")

if __name__ == '__main__':
    print(guest_message_1)
    print(guest_message_2)
    print(guest_message_3)
    print(guest_message_4)
    print(guest_message_5)
    print(guest_no_go + " can't make it to the dinner.")
    print(index_of_guest_no_go)
    display_invitation()

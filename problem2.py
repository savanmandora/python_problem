def process_cred_card(cred_card):
    cred_num_list = []

    # doubling the value
    tmp_toggle = False

    for i in range(len(cred_card)):
        x = cred_card[i]

        if not tmp_toggle:
            x = int(x) * 2
            tmp_toggle = True
        else:
            tmp_toggle = False

        cred_num_list.append(int(x))

    # check 1
    index = 0
    for i in cred_num_list:
        if i > 9:
            a = str(i)[0]
            b = str(i)[1]
            cred_num_list[index] = int(a) + int(b)
        
        index = index + 1

    # check 2
    cred_sum = 0
    for i in cred_num_list:
        cred_sum = cred_sum + i

    # check 3
    tmp = str(cred_sum)
    if tmp[len(tmp) - 1] == "0":
        return 'valid'
    else:
        return [cred_num_list,cred_sum]

if __name__ == "__main__":
    cred_card = str(input("Enter cred number: "))
    card_status = process_cred_card(cred_card)
    
    if card_status == 'valid':
        print("It's a valid credit card")
    else:
        print(card_status)

phone={"maria":[12345,45634], "jean":[], "marc":[56789]}

for e in phone:
    print(e, "->", phone[e])
    print(e, "->", phone.get(e))
    
phone["jean"].append(34566)

print(phone)
color = ""

# if
if color == "red":
    print("Color is red")
elif color == "blue":
    print("Color is blue")
else:
    print("Color is green")
    
# match-case, introduced in v3.10
match color:
    case "red":
        print("Color is red")
    case "blue":
        print("Color is blue")
    case _:
        print("Color is green")

magnitude = -1
while magnitude <0:
    try:
        magnitude = float(input("Enter your scale: "))
    except:
        print("Please enter a valid number")


def scale(magnitude):
    if magnitude >= 8:
        return "Great"
    elif magnitude >= 7:
        return "Major"
    elif magnitude >= 6:
        return "Strong"
    elif magnitude >= 5:
        return "Moderate"
    elif magnitude >= 4:
        return "Light"
    elif magnitude >= 3:
        return "Minor"
    else:
        return "Micro"


advices = {
    "Great": "Stay inside, stay safe",
    "Major": "Houses can break, stay inside, stay safe",
    "Strong": "Severe, stay inside, stay safe",
    "Moderate": "A normal earthquake Stay inside, stay safe",
    "Light": "Stay inside, stay safe",
    "Minor": "Some things can break",
    "Micro": "Not to severe, but stay inside, stay safe"
}

print(scale(magnitude),advices[scale(magnitude)])







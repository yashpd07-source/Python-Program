medical_cause = input("Did you have any medical causes? (Y/N): ").strip().upper()
if medical_cause =='Y': 
    print("You're allowed!")
else:
    atten = int(input("Enter the attendance of the student taking the exam: "))
    if atten >= 75:
        print("Allowed!")
    else:
        print("Not allowed.") 
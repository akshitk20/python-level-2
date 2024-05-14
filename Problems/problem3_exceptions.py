"""
Given a temperature (in Celsius), print the state of water at that temperature
"""

# Todo: Handle invalid inputs
while True:
    try:
        temp = float(input("What's the H20 temperature? "))
        if temp <= 0:
            print("  It’s ice")
            break
        elif temp >= 100:
            print("  It’s steam")
            break
        else:
            print("  It's water")
            break
    except ValueError as e:
        print(f"Invalid temp ")
        raise ValueError("Invalid temp!!!!")
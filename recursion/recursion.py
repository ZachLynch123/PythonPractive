

def countdown(x):
    if x == 0:
        print("Done!")
        return
    else: 
        print(x, "...")
        countdown(x - 1)
        return

countdown(5)
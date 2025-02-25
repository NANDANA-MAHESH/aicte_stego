import cv2

img = cv2.imread("encryptedImage.png")  # Load the encrypted image

c = {i: chr(i) for i in range(256)}  # Reverse mapping for decryption

# Read saved passcode and message
try:
    with open("secret_info.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        password = lines[0].strip()
        msg = lines[1].strip()  # Retrieve original message
except FileNotFoundError:
    print("Error: Required file 'secret_info.txt' not found!")
    exit()

pas = input("Enter passcode for Decryption: ")
if pas == password:
    n, m, z = 0, 0, 0
    message = ""

    for _ in msg:  # Use original message length
        message += c[img[n, m, z]]
        n += 1
        m += 1
        z = (z + 1) % 3

    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")


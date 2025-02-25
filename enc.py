import cv2
import os

img = cv2.imread("mypic.jpg")  # Load the original image

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {chr(i): i for i in range(256)}  # Ensure full ASCII mapping

n, m, z = 0, 0, 0

# Store message in image pixels
for char in msg:
    img[n, m, z] = d[char]
    n += 1
    m += 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.png", img)  # Use PNG to prevent corruption

# Save passcode and message separately
with open("secret_info.txt", "w", encoding="utf-8") as f:
    f.write(f"{password}\n{msg}")  

print("Encryption complete. Encrypted image saved as 'encryptedImage.png'.")



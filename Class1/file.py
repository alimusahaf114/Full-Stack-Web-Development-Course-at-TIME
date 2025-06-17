# Rail Fence Cipher attempt 

def encrypt_rail_fence(myText, rails):
    # First tried 1D list but got stuck, now using 2D list like table
    fence = [['' for i in range(len(myText))] for j in range(rails)]

    down = False
    row = 0
    col = 0

    for ch in myText:
        if row == 0 or row == rails - 1:
            down = not down  # toggle direction at top and bottom

        fence[row][col] = ch
        col += 1

        if down:
            row += 1
        else:
            row -= 1

    # Now read row-wise
    encrypted = ''
    for i in range(rails):
        for j in range(len(myText)):
            if fence[i][j] != '':
                encrypted += fence[i][j]
    return encrypted


def decrypt_rail_fence(encryptedText, rails):
    # Make the empty grid
    fence = [['' for i in range(len(encryptedText))] for j in range(rails)]

    # Mark with *
    down = None
    row, col = 0, 0
    for i in range(len(encryptedText)):
        if row == 0:
            down = True
        if row == rails - 1:
            down = False

        fence[row][col] = '*'
        col += 1

        if down:
            row += 1
        else:
            row -= 1

    # Fill the marked * with actual letters from encryptedText
    index = 0
    for i in range(rails):
        for j in range(len(encryptedText)):
            if fence[i][j] == '*' and index < len(encryptedText):
                fence[i][j] = encryptedText[index]
                index += 1

    # Now read in zigzag to get original
    result = ''
    row, col = 0, 0
    for i in range(len(encryptedText)):
        if row == 0:
            down = True
        if row == rails - 1:
            down = False

        result += fence[row][col]
        col += 1

        if down:
            row += 1
        else:
            row -= 1

    return result


# --- Trying it out below ---
msg = "SecurityTest"  # trying with longer text
myKey = 3  # tried 2 first but output looked weird

cipherText = encrypt_rail_fence(msg, myKey)
print("Encrypted text is:", cipherText)

# forgot to pass right var name first time 🤦
original = decrypt_rail_fence(cipherText, myKey)
print("Decrypted back:", original)

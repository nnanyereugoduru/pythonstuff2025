import hashlib

# -----------------------------
# Function: Hash a plaintext key
# -----------------------------
# Instead of storing the real key in plain text (which is insecure),
# we hash it. Hashing is one-way: you can verify a key, but you cannot
# reverse the hash to find the original key.
def hash_key(plaintext):
    return hashlib.sha256(plaintext.encode()).hexdigest()


# -----------------------------
# Function: Scramble the array
# -----------------------------
# This applies a reversible transformation to each number.
def scramble(array):
    for i in range(len(array)):
        array[i] = array[i] - 12   # 3 * 4 simplified
    return array


# -----------------------------
# Function: Unscramble the array
# -----------------------------
def unscramble(array):
    for i in range(len(array)):
        array[i] = array[i] + 12
    return array


# -----------------------------
# Function: Store hashed key
# -----------------------------
# The real key is "randomkey123", but we never store it directly.
def get_stored_key():
    stored = hash_key("randomkey123")
    return stored


# -----------------------------
# MAIN PROGRAM STARTS HERE
# -----------------------------

newArray = []
stored_key = get_stored_key()

# Limit login attempts for better security
attempts = 3
authenticated = False

while attempts > 0:
    inputKey = input("Enter the key: ")
    if hash_key(inputKey) == stored_key:
        print("Access granted")
        authenticated = True
        break
    else:
        attempts -= 1
        print("Access denied. Attempts left:", attempts)

# If authentication failed, exit early
if not authenticated:
    print("Too many failed attempts. Program locked.")
    exit()

# -----------------------------
# Collect numbers from the user
# -----------------------------
while True:
    user_input = input("Enter a number to add to the array (or type 'done' to finish): ")

    # If user types "done", stop collecting numbers
    if user_input.lower() == "done":
        break

    # Try converting input to integer
    try:
        num = int(user_input)
        newArray.append(num)
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

print("Your array:", newArray)

# -----------------------------
# Ask user if they want to scramble
# -----------------------------
choice = input("Would you like to scramble the array? (yes/no): ").lower()

if choice == "yes":
    newArray = scramble(newArray)
    print("Scrambled array:", newArray)
elif choice == "no":
    print("Array not scrambled.")
else:
    print("Invalid choice.")

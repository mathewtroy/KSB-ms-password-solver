# Substitution Cipher with a keyword
def create_substitution_alphabet(keyword):
    """
       Creates a substitution alphabet based on a keyword.
       Parameters:
       - keyword: The keyword to build the substitution alphabet
       Returns:
       - A dictionary mapping original alphabet letters to substitution letters
   """
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    key_letters = []

    # Remove duplicates in the keyword and create the substitution list
    for char in keyword.upper():
        if char not in key_letters:
            key_letters.append(char)
    # Create substitution alphabet starting with the keyword letters
    substitution_alphabet = key_letters.copy()
    # Add remaining letters of the alphabet
    for char in alphabet:
        if char not in substitution_alphabet:
            substitution_alphabet.append(char)
    return dict(zip(alphabet, substitution_alphabet))


def decrypt_with_keyword(text, keyword):
    """
       Decrypts a text encrypted using a substitution cipher with a given keyword.
       Parameters:
       - text: The encrypted text
       - keyword: The keyword used to build the substitution alphabet
       Returns:
       - Decrypted text
   """
    substitution_alphabet = create_substitution_alphabet(keyword)
    # Invert the substitution dictionary for decryption
    inverse_substitution_alphabet = {v: k for k, v in substitution_alphabet.items()}
    decrypted = []
    for char in text:
        if char.isalpha() and char.isupper():
            decrypted.append(inverse_substitution_alphabet[char])
        else:
            decrypted.append(char)
    return ''.join(decrypted)


def try_decrypt_with_popular_words(text):
    """
       Attempts to decrypt a text using a list of popular keywords for a substitution cipher.
       Parameters:
       - text: The encrypted text
       Prints:
       - Possible decrypted texts that contain common words
   """
    # Read popular_keywords from test.txt
    with open('test.txt', 'r') as f:
        content = f.read()
        # Execute the content to get popular_keywords variable
        local_vars = {}
        exec(content, {}, local_vars)
        popular_keywords = local_vars['popular_keywords']

    # List of common words to help identify correct decryption
    common_words = ["THE", "AND", "THAT", "WITH", "THIS", "HAVE", "FROM", "YOUR", "DOES", "BUT", "ALL", "FORM", "TION",
                    "NION", "TURNED", "PUBLIC", "DATA", "WAY", "DOES", "BEEN", "TIAL", "ITY", "OFTH", "OFYUO", "FOR",
                    "TURN", "ITS", "ATTH", "INTO", "ING", "MOTION"]

    for keyword in popular_keywords:
        decrypted_text = decrypt_with_keyword(text, keyword)
        # Check how many common words are in the decrypted text
        match_count = sum(1 for word in common_words if word in decrypted_text)
        if match_count >= 5:
            print(f"Possible match with keyword '{keyword}':")
            print(decrypted_text)
            print("\n")


if __name__ == "__main__":
    substitution_text = "LRHWLQRRCWJCWDKSHOULQWCEQAWLPQKJQKIWRCEJBQKHEORCWYCLOWXMWDRWOCEIRKLQGUWAKPWJKVCWDKSHOPWLOEREJRCWEPWYWQRCWYCLODWPRLEJVLYQKAGWWMEJBRCEJBQAPKIYKSEJCKQMERLHQ"

    # Substitution Cipher with keyword
    print("\n----------------------------------------------------------------------")
    print(" Substitution Cipher with a keyword:")
    print("\nTrying to decrypt using popular keywords:")
    try_decrypt_with_popular_words(substitution_text)

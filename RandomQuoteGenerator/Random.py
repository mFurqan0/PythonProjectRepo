import random

def get_random_quote():
    quotes = [
        "Believe you can and you're halfway there.",
        "Do what you can, with what you have, where you are.",
        "It does not matter how slowly you go as long as you do not stop.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "Act as if what you do makes a difference. It does.",
        "Happiness depends upon ourselves."
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    print("Random Inspirational Quote:")
    print(get_random_quote())
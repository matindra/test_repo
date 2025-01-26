import random

def generate_random_mobile_number():
    prefix = random.choice(['070', '080', '090'])
    number = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    return prefix + number

if __name__ == "__main__":
    print(generate_random_mobile_number())
    
    
    
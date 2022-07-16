# brute force attack
import time


class PasswordGenerator:

    def __init__(self, patterns: str):
        self.__patterns: list[str] = [pattern for pattern in patterns]

    def generate_all(self, predicted_passwords: list[str], digits: int) -> list[str]:
        results: list[str] = []
        if digits < 2:
            return predicted_passwords
        for password in predicted_passwords:
            for pattern in self.__patterns:
                results.append(password + pattern)
        return self.generate_all(results, digits - 1)

def find_password(password: str, patterns: str, digits: int) -> bool:
    patterns = [pattern for pattern in patterns]
    predicted_passwords: list[str] = PasswordGenerator(patterns).generate_all(patterns, digits)
    for predicted_password in predicted_passwords:
        print(f"Searching: {predicted_password}")
        if predicted_password == password:
            print(f"Found the password: {predicted_password}")
            return True
    return False

if __name__ == '__main__':
    password = input("Enter a password: ")
    password_digits: int = 1
    patterns: str = "abcdefghijklmnopqrstuvwxyz0123456789"
    found_password: bool = False
    start_time: float = time.time()
    end_time: float|None = None
    while not found_password:
        found_password = find_password(password, patterns, password_digits)
        password_digits += 1
    end_time = time.time()
    search_finished_time: float = float(format(end_time - start_time))
    print(f"Process finished in {search_finished_time:.1f}")
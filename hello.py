def greet(name: str) -> str:
    return f"Hello, {name}! 👋"

if __name__ == "__main__":
    user = input("Enter your name: ").strip() or "World"
    print(greet(user))
    print("good bye")
    print("see you again")

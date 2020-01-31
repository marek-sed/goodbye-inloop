from random import shuffle, randint

def main():
    with open("names.txt", "r") as reader:
        names = [name.strip() for name in reader.readline().split(",")]
        for _ in range(randint(5, 24)):
            shuffle(names)
        print(names)

if __name__ == "__main__":
    main()

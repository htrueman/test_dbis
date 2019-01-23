import auger

import pet
import animal


def main():
    p = pet.create_pet("Polly", "Parrot")
    print(p, p.get_name(), p.get_species())


if __name__ == "__main__":
    with auger.magic([pet.Pet]):
        main()

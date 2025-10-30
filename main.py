from character import Character


def main():
    hero = Character("Knight", 30, 10)
    enemy1 = Character("Goblin", 20, 3)
    enemy2 = Character("Orc", 25, 4)

    print(hero)
    print(enemy1)
    print(enemy2)
    print()

    while hero.is_alive() and (enemy1.is_alive() or enemy2.is_alive()):
        if enemy1.is_alive():
            hero.attack(enemy1)
        elif enemy2.is_alive():
            hero.attack(enemy2)

        if enemy1.is_alive():
            enemy1.attack(hero)
        if enemy2.is_alive():
            enemy2.attack(hero)

        print(hero)
        print(enemy1)
        print(enemy2)
        print()

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print("Enemies win!")


if __name__ == "__main__":
    main()

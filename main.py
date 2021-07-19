from random import randint

global monster_counter
global hp
global attack

attack = 0
hp = 0
monster_counter = 0


def started_stats() -> None:
    """Генерация начальных статов персонажа."""
    global hp
    global attack
    hp = randint(10, 20)
    attack = randint(10, 20)


def choice_player() -> str:
    """Выбор игрока."""
    pl_choice = input()
    while pl_choice != "1" and pl_choice != "2":
        pl_choice = input("Попробуйте еще")
        if pl_choice != "1" and pl_choice != "2":
            pl_choice = input("Попробуйте еще")
    return pl_choice


def spawn_monster() -> None:
    """Генерация статов встреченного монстра."""
    global attack, hp, monster_counter
    monster_hp = randint(1, 11)
    monster_attack = randint(1, 7)
    print(
        "БОЙ ! Вы встретили чудовище c {h} жизнями и с силой удара {a}, нажмите 1 сразиться, 2 убежать".format(
            a=str(monster_attack), h=str(monster_hp)
        )
    )
    choice = choice_player()
    if choice == "1":
        print("Вы атаковали монстра")
        print("Монстр атаковал вас в ответ")
        hp -= monster_attack
        print("Ваше здоровье {h}".format(h=str(hp)))
        monster_counter += 1
        in_game_action()
    else:
        print("Вы сбежали   ")
        print("Ваша атака {a}, Ваше здоровье {h}".format(a=str(attack), h=str(hp)))
        in_game_action()


def create_sword() -> None:
    """Генерация найденного меча."""
    global attack
    sword = randint(10, 25)
    print("MEЧ Вы нашли силой {s}, нажмите 1 подобрать 2 оставить.".format(s=str(sword)))
    choice = choice_player()
    if choice == "1":
        attack = sword
        print("Вы взяли меч   ")
        print("Ваша атака теперь {a}".format(a=str(attack)))
        in_game_action()
    else:
        print("Вы оставили меч   ")
        print("Ваша атака {a}".format(a=str(attack)))
        in_game_action()


def create_apple() -> None:
    """Генерация найденного яблока."""
    global hp
    apple = randint(1, 5)
    hp += apple
    print("Вы съели яблоко hp восстановлено на {n}.".format(n=str(apple)))
    in_game_action()


def give_item() -> None:
    """Выбор предмета для игрока."""
    item = randint(1, 2)
    if item == 1:
        create_sword()
    else:
        create_apple()


def check_monster_counter() -> None:
    """Проверка на колличество убитых монстров."""
    global monster_counter
    if monster_counter >= 10:
        win()


def win() -> None:
    """Победа."""
    print("ПОБЕДА")
    exit(1)


def lose() -> None:
    """Поражение."""
    print("ПОРАЖЕНИЕ")
    exit(1)


def start_new_action() -> None:
    """Случайный выбор следующего действия."""
    action = randint(1, 2)
    if action == 1:
        give_item()
    else:
        spawn_monster()


def check_hp() -> None:
    """Провека колличества хп."""
    global hp
    if hp <= 0:
        lose()


def in_game_action() -> None:
    """Набор действий каждого хода."""
    check_hp()
    check_monster_counter()
    start_new_action()


def game() -> None:
    """Основная функция, запускает игру."""
    started_stats()
    in_game_action()

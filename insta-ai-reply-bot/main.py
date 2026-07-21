from memory.database import (
    init_database
)


def start():

    init_database()

    print(
        "Instagram AI Reply Bot Started"
    )


if __name__ == "__main__":

    start()
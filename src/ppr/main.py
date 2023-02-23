import argh

from . import targets


def main():
    argh.dispatch_commands(
        [
            targets.auth,
            targets.comment,
            targets.pr,
            targets.ready,
        ]
    )


if __name__ == "__main__":
    main()

#!/usr/bin/env python
import brain_games.games.calc_cli
import brain_games.engine


def main():
    brain_games.engine.run_game(brain_games.games.calc_cli)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3

import sys
import os
import logging

log = logging.Logger("errors")


def try_to_open_a_file(filepath, retry=1) -> list:
    """Tries to open a file, if error, retries n times."""
    for attempt in range(1, retry + 1):
        try:
            return open(filepath).readline()
        except FileNotFoundError as e:
            log.error("ERRO: %s", e)
        else:
            print("Sucesso!")
        finally:
            print("Execute isso sempre!")

    return []


for line in try_to_open_a_file("names.txt", retry=5):
    print(line)

#!/usr/bin/env python3

import logging
from logging import handlers

# TODO: usar funcao
# TODO: usar lib (loguru)
log = logging.Logger("logs", logging.DEBUG)
ch = logging.StreamHandler()  # Console/terminal/stderr
ch.setLevel(logging.DEBUG)
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s"
)
ch.setFormatter(fmt)
log.addHandler(ch)


# log.debug("Mensagem de erro para dev, qe, sysadmin")
# log.info("Mensagem geral para usuarios.")
# log.warning("Aviso que nao causa erro.")
# log.error("Erro que afeta uma unica execucao.")
# log.critical("Erro geral, ex: banco de dados sumiu.")


try:
    1 / 0
except ZeroDivisionError as e:
    log.error("Deu erro %s", str(e))

import logging

logging.basicConfig(level=logging.INFO, filename="log_excep.log", filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")

try:
    1 / 0
except ZeroDivisionError as e:
    # logging.error("ZeroDivisionError", exc_info=True)
    logging.exception("ZeroDivisionError")

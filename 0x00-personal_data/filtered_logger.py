#!/usr/bin/env python3
"""
Module for Personal Data Logging and Redaction
"""

import logging
import os
import re
import mysql.connector
from typing import List

# Fields considered Personally Identifiable Information (PII)
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def redact_pii(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Redact specified fields in a log message.

    Args:
        fields: List of field names to redact.
        redaction: Redaction string to replace field values.
        message: Log message containing field-value pairs.
        separator: Separator used to split fields in the message.
    Returns:
        Redacted log message.
    """
    for field in fields:
        message = re.sub(rf"{field}=(.*?)\{separator}", f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """
    Custom logging formatter to redact PII fields in log records.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize formatter with PII fields to redact.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Apply redaction to the log record message.
        """
        return redact_pii(self.fields, self.REDACTION, super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Create and configure a logger with PII redaction.

    Returns:
        Configured logger instance.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db_connection() -> mysql.connector.connection.MySQLConnection:
    """
    Establish a connection to the MySQL database.

    Returns:
        MySQL database connection instance.
    """
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    username = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    name = os.getenv("PERSONAL_DATA_DB_NAME")
    
    return mysql.connector.connect(
        host=host,
        database=name,
        user=username,
        password=password
    )


def main() -> None:
    """
    Main function to retrieve and log user data with redacted PII.
    """
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM users;")
    
    for row in cursor:
        message = (
            f"name={row[0]}; email={row[1]}; phone={row[2]}; "
            f"ssn={row[3]}; password={row[4]}; ip={row[5]}; "
            f"last_login={row[6]}; user_agent={row[7]};"
        )
        print(message)
    
    cursor.close()
    db_connection.close()


if __name__ == '__main__':
    main()

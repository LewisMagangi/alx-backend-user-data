#!/usr/bin/env python3

from user import User

col_by_name = {}
for column in User.__table__.columns:
    col_by_name[column.description] = column.type

col_keys = col_by_name.keys()
for col_key in sorted(col_keys):
    print("{}: {}".format(col_key, col_by_name[col_key]))


# -*- coding: utf-8 -*-
import os

import datetime
from flask import Flask

from mehrstufendiagnostik.flaskr.start import create_app

def main():
    app = create_app()
    app.run(host="localhost", port=8080)


if __name__ == '__main__':
    main()


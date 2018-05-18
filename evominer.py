#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
App entry point
'''

import multiprocessing

from main import main

if __name__ == "__main__":
    multiprocessing.freeze_support()
    main()
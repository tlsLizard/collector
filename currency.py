#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

def monnaie():
    result=[]
    with open('Currency.txt','r') as f:
        for line in f:
            result.append(list(line.strip('\n').split(',')))
    return(result)
#!/bin/bash
dos2unix `find . -path './.git' -prune -o -type f -print|xargs`
#!/bin/bash
dos2unix `/bin/find . -path './.git' -prune -o -type f -print|xargs`
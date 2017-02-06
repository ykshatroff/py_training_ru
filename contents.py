# -*- coding: utf-8 -*-
# Date: 06.02.17
from __future__ import absolute_import
import re
import base64
import codecs
title_re = re.compile("^(#+)\s+(.+)$")


if __name__ == '__main__':
    import sys
    ifile = sys.argv[1]
    with open(ifile, 'rb') as f:
        for line in f:
            if line.startswith("#"):
                match = title_re.match(line.strip())
                level = match.group(1)
                title = match.group(2)

                print "%s* [%s](#%s)\n" % (
                    level.replace('#', '\t'),
                    title,
                    base64.b64encode(title, altchars='-_').rstrip('=')
                )

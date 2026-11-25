---
title: "Python 3.X base64.standard_b64encode encoding is required byte given str"
description: "Python 3. is required byte not string to resolve this issue we need to convert the string into UTF 8 then again after encoding we need to convert in to…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2019-04-07T04:24:55Z
legacy: true
wpId: 1631
---

Python 3.\* is required byte not string to resolve this issue we need to convert the string into UTF-8 then again after encoding we need to convert in to ascii.

**token = base64.standard\_b64encode("
samplestring ".encode('UTF-8') + ':'.encode('UTF-8') + "samplestring".encode('UTF-8')).decode('ascii')**

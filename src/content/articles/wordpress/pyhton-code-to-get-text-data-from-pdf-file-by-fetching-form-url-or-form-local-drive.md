---
title: "Pyhton Code to Get Text Data From Pdf File by fetching form URL or Form Local Drive"
description: "In this post we will explain how to fetch the text data from the pdf file using Pyhton Code. To Get Text Data From Pdf You need to in install the flowing…"
lang: python
categories: ["Python"]
author: "Shakti Das"
pubDate: 2018-05-27T16:31:52Z
legacy: true
wpId: 1156
---

In this post we will explain how to fetch the text data from the pdf file using Pyhton Code. To Get Text Data From Pdf You need to in install the flowing python library for data read form the pdf document.

#### 1.urllib
**This library will help you to download data file or pdf from the internet.By using this library we can download file from the http sites .**

**To install url library use this below command to get the data form the web.**

**pip install urllib**

**pip install urllib2**

**pip install urllib3**

import urllib

urllib.urlretrieve('http://ird.iitd.ac.in/sites/default/files/jobs/project/advtprofaksrivastava2.pdf', 'data.pdf')

2.PyPDF2

This library will help you to read the pdf and extract data

```
import PyPDF2
pdfFileObj = open('data.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print pdfReader.numPages
pageObj = pdfReader.getPage(0)
print pageObj.extractText()
```

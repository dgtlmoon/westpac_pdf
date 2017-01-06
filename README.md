Westpac PDF
===========

Simple Drupal module that uses a Python script to convert Westpac PDF's to CSV

Westpac wont let you export more than a few months of QIF/OtherFormat dates, 
so if you've been lazy in keeping up your banking, you'll need to parse their 
'eStatement' PDF's, which is really annoying that they give you a PDF but wont 
keep a few bytes for you to download directly.

And yet their main online banking website is a victim of design by committee whilst
there is no real new functionality for users.

Fortunately it is possible to parse their PDF's to generate a CSV.

This repository contains a Python script that does the actual regex work by
processing the output from `pdftotext`

The other code is the Drupal module I use on my private website and blog
https://dgtlmoon.com

### Running the script by hand not as a Drupal module

You can also run this from commandline without Drupal

```
pdftotext -layout mystatements.pdf - |python ./cleaner.py
```


Note: You will need the `pdftotext` command-line util, 
`apt-get install poppler-utils`


### To the Future...

Most likely you could remove the python step and just execute the `pdftotext` from PHP and parse it inside of PHP.

Note: No guarantee is given with this software AND it only works with the 
      PRIVATE statements not BUSINESS statements
      
Probably a million ways todo this better.

By: Leigh Morresi
    dgtlmoon@gmail.com

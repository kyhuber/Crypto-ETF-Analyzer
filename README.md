# Crypto ETF Analyzer Application 

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation-and-technologies">Installation and Technologies</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
	<!-- <li><a href="#license">License</a></li> -->
    <li><a href="#contact">Contact</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

The explosive growth of cryptocurrency prices in recent years has piqued the interest of many investors, both retail and institutional. Although individual cryptocurrencies can be purchased directly through an exchange, new crypto-related investment opportunities are becoming available in the market, such as Exchange Traded Funds (ETFs).

This app allows the user to select stocks, ETFs, and cryptocurrencies over time to view price performance over time. The app also offers a Monte Carlo simulation to forecast future performance, where the user can change the allocation of their portfolio.

The S&P 500 (SPY) will be used as a baseline throughout the entire application.

Investors will be able to use this application, with it's vizualization tools, to make decisions that are best aligned to their individual investment goals.  


---

## Getting Started

### Installation and Technologies

This was run on a pc using Windows 10

This project leverages python 3.8.8 with the following packages:
  
Python
Pandas
Jupyter Lab
Matplotlib
MCForecastTools
Yahoo Finance API
Alphavantage API
Streamlit

# Installation Guide Python (MacOS)

1.  Command + Space
2.  Enter Terminal in search bar and press enter
3.  Terminal should open
4.  Open Homebrew Installation website in browser (https://brew.sh/)
5.  Copy installation code at the bottom of the page
6.  Once Homebrew is installed, install Python
7.  Open Terminal 
8.  Enter "brew install python3" into the CLI to install Python

Installing Anaconda with Python (MacOS):

1.  Enter "conda create -n dev python=3.7 anaconda" into the command line terminal
2.  Return and type Y when prompted
3.  Open environment by entering "conda activate dev"
4.  Enable terminal commands through conda by enter "echo $ {SHELL}" to check BASH/ZSH environment
5.  Depending on if BASH/ZSH, type "conda init bash or ZSH" to activate conda terminal commands
4.  Close environment by entering "conda deactivate"
    
Installing Python Fire (MacOS):

1.  Open Terminal (Command + Space and serach terminal, press enter)
2.  Enter the following into CLI:  "pip install fire"
3.  Import as fire by entering the following into CLI: "import fire"

Installing Questionary: 

1.  Open Terminal (Command + Space and serach terminal, press enter)
2.  Enter the following into CLI:  "pip install questionary"
3.  Import by entering the following into CLI: "import questionary"

Installing Matplotlib:

1.  Open Terminal (Command + Space and serach terminal, press enter)
2.  Enter the following into CLI:  
   "import pandas as pd
   import numpy as np
   from pathlib import Path

   %matplotlib inline"

   ## Matplotlib import from application for Monte Carlo Simulation
   import os
   from sqlite3 import Date
   import pandas as pd
   import requests
   import streamlit as st
   from dotenv import load_dotenv
   from datetime import datetime
   from MCForecastTools import MCSimulation
   import matplotlib.pyplot as plt
   import yfinance as yf

Installing MCForecast Tools: 

# Import the required libraries and dependencies

import numpy as np
import pandas as pd
import os
import alpaca_trade_api as tradeapi
import datetime as dt
import pytz


# Usage

As a user, I want to learn about how the performance of newly created Bitcoin Exchange Traded Funds (ETF) compares to the performance of the S&P 500 and individual cryptocurrencies.

To use the Crypto ETF app, the user must input their initial investment, stock ticker, cryptocurrency, portfolio allocation, and number of years to simulate. The app then calls for data via API and renders plots for the user to review.



The following are investment options available to the user(s) against the S&P 500 (SPY).  

<img width="990" alt="Screen Shot 2022-02-27 at 8 04 12 PM" src="https://user-images.githubusercontent.com/96351123/155922170-92ad7311-0d5f-498e-b1bb-557a2760e6f1.png">

Closing prices of SPY, BITW (Stock ETF), and BTC (Crypto ETF) investment options.

<img width="659" alt="Screen Shot 2022-02-27 at 8 09 58 PM" src="https://user-images.githubusercontent.com/96351123/155922624-244cb021-4f53-4585-aaaf-4f5459dcd0cf.png">

Analysis of overall performance regarding Daily Profit Returns; SPY as the baseline.

<img width="449" alt="Screen Shot 2022-02-27 at 8 11 53 PM" ![Uploading Screen Shot 2022-02-27 at 8.50.04 PM.png…]()
src="https://user-images.githubusercontent.com/96351123/155922813-b6f1a592-04bd-41f3-9c04-76d888b3b743.png">

<img width="643" alt="Screen Shot 2022-02-27 at 8 50 39 PM" src="https://user-images.githubusercontent.com/96351123/155925937-f6856f7f-0710-4134-a7cd-f974a4a129b7.png">

<img width="681" alt="Screen Shot 2022-02-27 at 8 52 21 PM" src="https://user-images.githubusercontent.com/96351123/155926090-2dc8eca4-1d76-4e1c-8636-98b4c97c7eb7.png">

Risk Evaluation

<img width="995" alt="Screen Shot 2022-02-27 at 8 15 03 PM" src="https://user-images.githubusercontent.com/96351123/155923057-8ffc06e0-b8d6-4c5c-8302-37f26ddced45.png">

Monte Carlo Simulation; 40% SPY, 60% Stock ETF.

<img width="735" alt="Screen Shot 2022-02-27 at 8 16 42 PM" src="https://user-images.githubusercontent.com/96351123/155923188-4d527014-1137-4766-b57b-0174790f203e.png">

Intepretation of findings:

<img width="1065" alt="Screen Shot 2022-02-27 at 8 32 14 PM" src="https://user-images.githubusercontent.com/96351123/155924525-33b11ac9-fd85-4d69-8c93-cb60f2e40907.png">

Sharpe Ratios:

<img width="677" alt="Screen Shot 2022-02-27 at 8 54 28 PM" src="https://user-images.githubusercontent.com/96351123/155926278-6e367d42-1a0a-4adb-bb06-27e86ff43018.png">

Average Rolling Beta

<img width="675" alt="Screen Shot 2022-02-27 at 8 55 30 PM" src="https://user-images.githubusercontent.com/96351123/155926354-2ad65e96-4576-42b2-8775-ee0232cf33d0.png">

Monte Carlo Simulation

3yr SPY and ETF Porfolio 40:60 allocation Result: if you contributed to this portfolio; then for 100 dollar investment, it would grow to $309.70.

10yr SPY and BTC Porfolio 40:60 allocation Result: if you contributed to this portfolio; then for 100 dollar investment, it would grow to $620.88.

Next 3 trading years of SPY/Stock ETF

<img width="894" alt="Screen Shot 2022-02-27 at 8 36 22 PM" src="https://user-images.githubusercontent.com/96351123/155924867-a5501bb5-a312-492a-9dc7-95359b25db8f.png">

Next 3 trading years of SPY/Crypto ETF

<img width="895" alt="Screen Shot 2022-02-27 at 8 36 54 PM" src="https://user-images.githubusercontent.com/96351123/155924899-be015ec0-7c36-47b6-a6d1-c3507d3563c3.png">

Next 10 trading years of SPY/Stock ETF

<img width="921" alt="Screen Shot 2022-02-27 at 8 38 27 PM" src="https://user-images.githubusercontent.com/96351123/155925012-4e96d734-df44-419d-a384-f611fbba2370.png">

Next 10 trading years of SPY/Crypto ETF

<img width="915" alt="Screen Shot 2022-02-27 at 8 39 17 PM" src="https://user-images.githubusercontent.com/96351123/155925082-4142e595-61e1-4577-a01d-6b8dd9716faa.png">

Total 10-year earnings/returns since initial investment: SPYxETF

<img width="980" alt="Screen Shot 2022-02-27 at 8 44 42 PM" src="https://user-images.githubusercontent.com/96351123/155925481-61ad725e-a01f-4209-843d-2bb1f9c2d255.png">

Total 10-year earnings/returns since initial investment: SPYxBTC

<img width="900" alt="Screen Shot 2022-02-27 at 8 45 48 PM" src="https://user-images.githubusercontent.com/96351123/155925584-15512a47-522c-4d79-a81b-9ca5336764cd.png">

Dashboard demonstration:

![image (1)](https://user-images.githubusercontent.com/96351123/155931654-4f56fcb1-0f85-41b7-ae8e-8433070ad824.png)

<img width="856" alt="IMG_0426" src="https://user-images.githubusercontent.com/96351123/155931677-09b373f8-14d0-4282-b702-b1a5cfe68292.png">


# Contributors

Alexis Rose Garcia
Alexisg324@gmail.com
https://www.linkedin.com/in/alexis-rose-garcia

Kyle Huber 
kyhuber@gmail.com 
https://www.linkedin.com/in/huberkyle/

Sumayyah Muhammad 
sumayyahmuhammadts@gmail.com
https://www.linkedin.com/in/sumayyahmuhammadofficial

John Batarse 
jbatarse@hotmail.com
https://www.linkedin.com/in/john-a-batarse-760a26116

Saina Azimi
azimi.sainaa@gmail.com
http://linkedin.com/in/azimi-saina

# License

>>> license()
A. HISTORY OF THE SOFTWARE
==========================

Python was created in the early 1990s by Guido van Rossum at Stichting
Mathematisch Centrum (CWI, see http://www.cwi.nl) in the Netherlands
as a successor of a language called ABC.  Guido remains Python's
principal author, although it includes many contributions from others.

In 1995, Guido continued his work on Python at the Corporation for
National Research Initiatives (CNRI, see http://www.cnri.reston.va.us)
in Reston, Virginia where he released several versions of the
software.

In May 2000, Guido and the Python core development team moved to
BeOpen.com to form the BeOpen PythonLabs team.  In October of the same
year, the PythonLabs team moved to Digital Creations, which became
Zope Corporation.  In 2001, the Python Software Foundation (PSF, see
https://www.python.org/psf/) was formed, a non-profit organization
created specifically to own Python-related Intellectual Property.
Zope Corporation was a sponsoring member of the PSF.

All Python releases are Open Source (see http://www.opensource.org for
the Open Source Definition).  Historically, most, but not all, Python
Hit Return for more, or q (and Return) to quit: 
releases have also been GPL-compatible; the table below summarizes
the various releases.

    Release         Derived     Year        Owner       GPL-
                    from                                compatible? (1)

    0.9.0 thru 1.2              1991-1995   CWI         yes
    1.3 thru 1.5.2  1.2         1995-1999   CNRI        yes
    1.6             1.5.2       2000        CNRI        no
    2.0             1.6         2000        BeOpen.com  no
    1.6.1           1.6         2001        CNRI        yes (2)
    2.1             2.0+1.6.1   2001        PSF         no
    2.0.1           2.0+1.6.1   2001        PSF         yes
    2.1.1           2.1+2.0.1   2001        PSF         yes
    2.1.2           2.1.1       2002        PSF         yes
    2.1.3           2.1.2       2002        PSF         yes
    2.2 and above   2.1.1       2001-now    PSF         yes

Footnotes:

(1) GPL-compatible doesn't mean that we're distributing Python under
    the GPL.  All Python licenses, unlike the GPL, let you distribute
    a modified version without making your changes open source.  The
Hit Return for more, or q (and Return) to quit: 
    GPL-compatible licenses make it possible to combine Python with
    other software that is released under the GPL; the others don't.

(2) According to Richard Stallman, 1.6.1 is not GPL-compatible,
    because its license has a choice of law clause.  According to
    CNRI, however, Stallman's lawyer has told CNRI's lawyer that 1.6.1
    is "not incompatible" with the GPL.

Thanks to the many outside volunteers who have worked under Guido's
direction to make these releases possible.


B. TERMS AND CONDITIONS FOR ACCESSING OR OTHERWISE USING PYTHON
===============================================================

Starting with Python 3.8.6, examples, recipes, and other code in
the documentation are dual licensed under the PSF License Version 2
and the Zero-Clause BSD license.

Some software incorporated into Python is under different licenses.
Hit Return for more, or q (and Return) to quit: 
The licenses are listed with code falling under that license.


1. This LICENSE AGREEMENT is between the Python Software Foundation ("PSF"), and
   the Individual or Organization ("Licensee") accessing and otherwise using Python
   3.10.2 software in source or binary form and its associated documentation.

2. Subject to the terms and conditions of this License Agreement, PSF hereby
   grants Licensee a nonexclusive, royalty-free, world-wide license to reproduce,
   analyze, test, perform and/or display publicly, prepare derivative works,
   distribute, and otherwise use Python 3.10.2 alone or in any derivative
   version, provided, however, that PSF's License Agreement and PSF's notice of
   copyright, i.e., "Copyright © 2001-2022 Python Software Foundation; All Rights
   Reserved" are retained in Python 3.10.2 alone or in any derivative version
   prepared by Licensee.

3. In the event Licensee prepares a derivative work that is based on or
   incorporates Python 3.10.2 or any part thereof, and wants to make the
   derivative work available to others as provided herein, then Licensee hereby
   agrees to include in any such work a brief summary of the changes made to Python
   3.10.2.

4. PSF is making Python 3.10.2 available to Licensee on an "AS IS" basis.
   PSF MAKES NO REPRESENTATIONS OR WARRANTIES, EXPRESS OR IMPLIED.  BY WAY OF
   EXAMPLE, BUT NOT LIMITATION, PSF MAKES NO AND DISCLAIMS ANY REPRESENTATION OR
   WARRANTY OF MERCHANTABILITY OR FITNESS FOR ANY PARTICULAR PURPOSE OR THAT THE
   USE OF PYTHON 3.10.2 WILL NOT INFRINGE ANY THIRD PARTY RIGHTS.

5. PSF SHALL NOT BE LIABLE TO LICENSEE OR ANY OTHER USERS OF PYTHON 3.10.2
   FOR ANY INCIDENTAL, SPECIAL, OR CONSEQUENTIAL DAMAGES OR LOSS AS A RESULT OF
   MODIFYING, DISTRIBUTING, OR OTHERWISE USING PYTHON 3.10.2, OR ANY DERIVATIVE
   THEREOF, EVEN IF ADVISED OF THE POSSIBILITY THEREOF.

6. This License Agreement will automatically terminate upon a material breach of
   its terms and conditions.

7. Nothing in this License Agreement shall be deemed to create any relationship
   of agency, partnership, or joint venture between PSF and Licensee.  This License
   Agreement does not grant permission to use PSF trademarks or trade name in a
   trademark sense to endorse or promote products or services of Licensee, or any
   third party.

8. By copying, installing or otherwise using Python 3.10.2, Licensee agrees
   to be bound by the terms and conditions of this License Agreement.

ZERO-CLAUSE BSD LICENSE FOR CODE IN THE PYTHON DOCUMENTATION
----------------------------------------------------------------------

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
Hit Return for more, or q (and Return) to quit: 
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.

>>> 
>>> 

# Workcited: 

## Financial Technology Bootcamp
UCB-Coding-Bootcamp (2021-2022).  Module 1-8. UC Berkeley Fintech Extension.  https://courses.bootcampspot.com/
## BITO (Bitcoin Strategy ETF)
Proshares.com (1999-11-01).  BITO.  https://www.proshares.com/our-etfs/strategic/bito
## Valkyrie-Funds (BTF - Bitcoing Strategy ETF)
Valkyrie-funds.com (2021-10-22).  Valkyrie BTF.  https://valkyrie-funds.com/btf/
## Global X BITS (Bloockchain & Crypto Strategy ETF)
globalxetfs.com (2021-11-16).  Bloockchain & Crypto Strategy ETF.  https://www.globalxetfs.com/funds/bits/
## How to Get Historical Market Data Through Python Stock API for SPY 
blog.quantinsti.com (2022).  How to Get Historical Market Data Through Python Stock API.  https://blog.quantinsti.com/historical-market-data-python-api/
## BITW (Bitwise 10 Crypto Index Fund)
bitwiseinvestments.com (2022).  Bitwise 10 Crypto Index Fund.  https://bitwiseinvestments.com/crypto-funds/bitw/

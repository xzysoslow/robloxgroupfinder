# Roblox Empty & Open Group Finder

A Python script to find Roblox groups that are empty, ownerless, and open to join.

## Features

* Searches random Roblox group IDs
* Filters groups with **no owner**, **0 members**, and **open to join**
* Optionally **save results** to a file

## Requirements

* Python 3.x [Download Here](http://python.org/downloads/)
* `requests` library
* `colorama` library
* Install the required libraries using pip:

      pip install requests colorama
  
## Installation

* Clone the repository or download the script.
* Navigate to the script folder in your terminal/command prompt.
* Install the required libraries (see above).

**Optional:** If you don’t want to install Python, simply open the `dist` folder and run the pre-built executable.
## Usage

### Run the script using Python:

       python groupfinder.py

**The script will prompt you to:**

* Set the minimum and maximum group IDs to search.
* Choose how many groups to check.
* Set the delay between checks to prevent rate-limiting.
* Optionally save found groups to a file.

## Notes

* The script uses random group IDs, so not all searches will return results.
* Adding a delay between requests is highly recommended to avoid temporary blocking by Roblox.
* Depending on the number of groups checked and the delay set, the process may take a **long time.**

## Screenshot

*nothing yet*


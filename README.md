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

```bash
pip install requests colorama
```

## Installation

* [Clone the repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) or download the script.
* Navigate to the script folder in your command prompt/Terminal.
* Install the required libraries (see above).

## Usage

<details>
<summary>How to run the script</summary>

### Using Python

1. Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux).
2. Navigate to the folder containing `groupfinder.py`. For example:

```bash
cd path\to\your\script   # Windows
cd /path/to/your/script   # Mac/Linux
```

3. Run the script:

```bash
python groupfinder.py
```

4. Follow the prompts to set group IDs, number of checks, delay, and optionally save results.

### Using the executable

* Open the `dist` folder and run `groupfinder.exe`.
* Follow the same prompts as the Python script.

</details>

## Notes

* The script uses random group IDs, so not all searches will return results.
* Adding a delay between requests is highly recommended to avoid temporary blocking by Roblox.
* Depending on the number of groups checked and the delay set, the process may take a **long time**.

## Screenshot

*nothing yet*


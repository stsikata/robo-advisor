# robo-advisor
A program to help you decide whether to sell stock or not.

### Setup

Clone this repo: https://github.com/stsikata/robo-advisor.git

Navigate to the repo from the command-line

```sh
cd ~/robo-advisor
```

### Environment Setup

Create and activate a now Anaconda virtual environment"

```sh
conda create -n stocks-env python=3.8 # (first time only)
conda activate stocks-env
```

From within the environment, install the required packages from the "requirements.txt" file:

```sh
pip install -r requirements.txt
```

Run the python script from the command-line:

```sh
python app/robo_advisor.py
```


Add your AlphaVantage key to a new file called ".env"
```
# this is the ".env" file
ALPHAVANTAGE_API_KEY="abc123"
```
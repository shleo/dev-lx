# ETF Arbitrage

ETF套利

## Setup
To facilitate development, we will use `conda` to manage our python environment.
1. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html)

2. Check if conda is installed properly by running `conda --version`. The output should be like:
 ```
 conda 4.11.0
 ```

3. Change the working directory to etf-arbitrage folder.

4. Install python environment
 ```
 conda env create -f environment.yml
 ```
 This should create a conda environment named **etf-arbitrage** that includes Python 3.6 and necessary libraries for this project.

5. Activate **etf-arbitrage** environment
 ```
 conda activate etf-arbitrage
 ```

6. Run the project
 ```
 python src/main.py
 ```


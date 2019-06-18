# SIR models - Modelling the spread of epidemics

This script runs a standard SIR model with additional parameters allowing for disease relapse, deaths, and vaccine intervention along the way. This was built for a [blog post](https://btmathic.github.io/read/-LhC7g-Ni3ocrcZ-RYuF) .

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for use and/or development purposes.

### Prerequisites

If you have [Python 3](https://www.python.org/downloads/) and [pip3](https://pip.pypa.io/en/stable/) already installed, you are good to go. If not, you will need to install these.

The plots returned use the matplotlib library, which you can install with
```
sudo apt-get install python3-matplotlib
```
on Ubuntu, or if not using Ubuntu, see the recommended approach for your OS [here](https://matplotlib.org/3.1.0/users/installing.html).

From here, you can edit the values for any of the parameters in the model.py file, then in the directory of the file, run the command
```
python3 ./model.py
```
to see the results of your epidemic model plotted.

## Built With

* Python 3
* PIP 3
* MatPlotLib

## Author

* Alexander Molnar

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
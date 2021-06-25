# Bigeleisen_KIE
library which provides tools capable of calculating the Kinetic Isotope Effect according to the Bigeleisen equation


## Installation

Use the package manager [pip](https://pypi.org/project/Bigeleisen-KIE/) to install foobar.

```bash
pip install Bigeleisen-KIE
```
## Usage

```python
import Bigeleisen_KIE as kie

#isH is the vibration frequencies of the molecule containing the light isotope at the initial state
#isD is the vibration frequencies of the molecule containing the heavy isotope at the initial state
#tsH is the vibration frequencies of the molecule containing the light isotope at the transition state
#tsD is the vibration frequencies of the molecule containing the heavy isotope at the transition state
#T is the temperature in Kelvin


kie.KIE(isH,isD,tsH,tsD,T)
```

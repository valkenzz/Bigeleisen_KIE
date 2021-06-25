# Bigeleisen_KIE
library which provides tools capable of calculating the Kinetic Isotope Effect according to the Bigeleisen equation


## Installation

Use the package manager [pip](https://pypi.org/project/Bigeleisen-KIE/) to install foobar.

```bash
pip install Bigeleisen-KIE
```
## Usage

```python
#we inport the library
import Bigeleisen_KIE as kie

#isH is the vibration frequencies of the molecule containing the light isotope at the initial state
#isD is the vibration frequencies of the molecule containing the heavy isotope at the initial state
#tsH is the vibration frequencies of the molecule containing the light isotope at the transition state
#tsD is the vibration frequencies of the molecule containing the heavy isotope at the transition state
#T is the temperature in Kelvin

#function to calculate the kie
kie.KIE(isH,isD,tsH,tsD,T)
```
but you can use excel file in this repository, fill the excel, then pass the path in KieCalculationWithExcel.py then you have just to execute the script for calculate the kie



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.



## License
[MIT](https://choosealicense.com/licenses/mit/)

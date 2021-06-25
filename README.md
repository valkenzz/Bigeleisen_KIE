# Bigeleisen_KIE
library which provides tools capable of calculating the Kinetic Isotope Effect according to the Bigeleisen equation

kie is the change in the reaction rate of a chemical reaction when one of the atoms in the reactants is replaced by one of its isotopes[1].Formally, it is the ratio of rate constants for the reactions involving the light and the heavy isotopically substituted reactants.

More particularly we use the equation figur 1 [2]. this equation Neglect tunneling effect.










#### source 
 [1] Atkins P, de Paula J (2006). Atkins' Physical Chemistry (8th ed.). Oxford University Press. pp. 286–288, 816–818. ISBN 978-0-19-870072-2.
 [2]WIREs Comput Mol Sci 2016. doi: 10.1002/wcms.1268


## Installation

Use the package manager [pip](https://pypi.org/project/Bigeleisen-KIE/) to install the library.

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

## repository
Bigeleisen_KIE.py is the module, with all function for calculate the kie

KIE_Vibration.xlsx is the excel you can use for a better "user friendly" experience

KieCalculationWithExcel.py you can use with the excel for calculate the kie, that show an example


## environement/requirement

pandas and numpy


## contact

For any question or bug don't hesitate to contact me at  <strong>valentin.meo.1@ulaval.ca</strong> or use github at : https://github.com/valkenzz/Bigeleisen_KIE

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.



## License
[MIT](https://choosealicense.com/licenses/mit/)

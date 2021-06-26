# Bigeleisen_KIE
Library which provides tools capable of calculating the Kinetic Isotope Effect according to the Bigeleisen equation

KIE is the change of the reaction rate of a chemical reaction when one of the atoms in the reactants is replaced by one of its isotopes[1].Formally, it is the ratio of rate constants for the reactions involving the light and the heavy isotopically substituted reactants.

More particularly we use the equation figur 1 [2]. this equation neglect tunneling effect.


![image](https://user-images.githubusercontent.com/40594333/123512125-056e2b80-d686-11eb-9221-910ddcd27c06.png)

Fig1 : the KIE equation are implemented

where the subscripts l and h stand for the light and
heavy isotopes,
υl*/υh* is the ratio of the imaginary frequencies
at the transition state structure,
N is the number of normal mode frequency,
‡ denote the transition state structure,
υi is the ith normal mode frequency of the corresponding isotopolog,
kB is Boltzmann’s constant, T is temperature, and
h is Planck’s constant,C the celerity of light in the vaccum.



We used method to determine the KIE just using harmonic vibrational frequencies. The Bigeleisen equation can be extended beyond the harmonic vibrational approximation and including quantum tunneling effects in the framework of Feynman path integrals.

#### Sources 
 [1] Atkins P, de Paula J (2006). Atkins' Physical Chemistry (8th ed.). Oxford University Press. pp. 286–288, 816–818. ISBN 978-0-19-870072-2.
 
 [2] WIREs Comput Mol Sci 2016. doi: 10.1002/wcms.1268


## Installation

Use the package manager [pip](https://pypi.org/project/Bigeleisen-KIE/) to install the library.

```bash
pip install Bigeleisen-KIE
```
## Usage

```python
#We inport the library
import Bigeleisen_KIE as kie

#isH is the vibration frequencies of the molecule containing the light isotope at the initial state
#isD is the vibration frequencies of the molecule containing the heavy isotope at the initial state
#tsH is the vibration frequencies of the molecule containing the light isotope at the transition state
#tsD is the vibration frequencies of the molecule containing the heavy isotope at the transition state
#T is the temperature in Kelvin

#function to calculate the kie
kie.KIE(isH,isD,tsH,tsD,T)
```
You can also use excel file in this repository: fill the excel, then execute KieCalculationWithExcel.py in the same directory or change the path of the excel file, then execute the script to calculate the KIE.

## Repository
Bigeleisen_KIE.py is the module with all functions to calculate the KIE.

KIE_Vibration.xlsx is the excel you can use for a better "user friendly" experience.

KieCalculationWithExcel.py you can use with the excel to calculate the KIE.


## Environement/Requirement

pandas and numpy


## Contact

For any question or bug, don't hesitate to contact me at  <strong>valentin.meo.1@ulaval.ca</strong> or use github at : https://github.com/valkenzz/Bigeleisen_KIE

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.



## License
[MIT](https://choosealicense.com/licenses/mit/)

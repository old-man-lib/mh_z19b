# Library for mh_z19b
Library for work with mh-z19 CO2 senser.

## Installation
Download and install the libraries to use them in Python.

#### For Python:
`pip install -r requirements.txt`

#### For Python3:
`pip3 install -r requirements.txt`

## How to use

#### Step 1 - Enable I2C Interface
1) Open Terminal
2) Open Raspi-config with this command:
  `sudo raspi-config`
3) Select “Interfacing Options”:
  ![image](https://user-images.githubusercontent.com/51321197/148430343-d1092022-4f91-4425-8e72-4ece91fa0215.png)
4) Go to “I2C” option and activate “<Select>”.
  ![image](https://user-images.githubusercontent.com/51321197/148430305-48a2cad5-02d9-40fd-a321-f2e6b7519966.png)
5) Select and activate “<Yes>”:
  ![image](https://user-images.githubusercontent.com/51321197/148430425-99ae2b3c-7a99-44ff-ad80-410ef7b70124.png)
6) Go and activate “<Ok>”:
  ![image](https://user-images.githubusercontent.com/51321197/148430534-516fdd52-416f-4bbf-b78b-fef2c10756fc.png)
7) When prompted to reboot go and activate “<Yes>”:
  ![image](https://user-images.githubusercontent.com/51321197/148430602-9a17049e-21aa-4c17-9771-c0ea3da096d9.png)
8) The Raspberry Pi will reboot and the interface will be enabled.

#### Step 2 - Import Library
```python
import mh_z19b

print("CO2:", mh_z19b.read())
```

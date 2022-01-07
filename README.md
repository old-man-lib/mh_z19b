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

3) Select Interfacing Options:

    ![image](https://user-images.githubusercontent.com/51321197/148550156-c445291e-5be8-405b-8c52-849f7a1d1a4b.png)

4) Go to "Serial" option and activate "Select":

    ![image](https://user-images.githubusercontent.com/51321197/148550269-032a0f4b-7aaf-47dc-b104-83218ec9aa5c.png)

5) Select and activate "Yes":

    ![image](https://user-images.githubusercontent.com/51321197/148550384-955de426-cd58-411a-a3ab-c9dfce951ae8.png)

6) Go and activate "Ok":

    ![image](https://user-images.githubusercontent.com/51321197/148550430-fbdd3dff-8c55-4774-aa95-670ebee5b3fb.png)

7) When prompted to reboot go and activate "Yes":

    ![image](https://user-images.githubusercontent.com/51321197/148550514-23accebb-244f-45fd-987a-a6eec451bbf1.png)

8) The Raspberry Pi will reboot and the interface will be enabled.

#### Step 2 - Import Library and Use
```python
import mh_z19b, time

while True:
  print("CO2:", mh_z19b.read())
  time.sleep(1)
```

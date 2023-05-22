# avoid using conda with pip.
if needed install pip after all conda packages have been installed. do not use conda again after pip is used.
switch to a new env if needed to install more conda and pip packages together

# avoid adding conda to PATH. just use the conda command prompt
add it to visual studio code

# install conda
https://www.anaconda.com/download

# install vscode extensions
python

# switch user setting
ctrl + shift + p
openuser settings
default interpreter path = C:\Users\Yang\anaconda3\python.exe
conda path = C:\Users\Yang\anaconda3\_conda.exe

# activate base environment to start testing
```
conda activate base
```
when using debugger, also remember to type this in

# conda commands below:
## intall python versions
conda install python=3.9
conda update python

## create new conda environments
conda create -n env_name python=3.9

## activate env
conda activate env_name

## conda info --invs

## see install packages
conda list

## env 
conda env export > env.yaml
conda env create -f env.yaml
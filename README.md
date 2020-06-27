# Add Subtitle into Video (export exe file)

## Environment

```shell script
conda create -n your-env python=3.7

pip install opencv-python

conda install pyinstaller

# build exe file
pyinstaller -F path/to/your/program.py -p path/to/your-env/python.exe
```

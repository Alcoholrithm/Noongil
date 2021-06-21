## If you use bottom-up-attention as decoder
```
git clone https://github.com/Alcoholrithm/py-bottom-up-attention.git
cd py-bottom-up-attention
python setup.py build develop
```

## Install Oscar
```
# install apex
git clone https://github.com/NVIDIA/apex.git
cd apex
python setup.py install --cuda_ext --cpp_ext

# install oscar
cd ..
git clone --recursive git@github.com:microsoft/Oscar.git
cd Oscar/coco_caption
./get_stanford_models.sh
cd ..
python setup.py build develop

# install requirements
pip install -r requirements.txt
```

## Download Oscar Scripts
```
git clone https://github.com/Alcoholrithm/Oscar.git
```

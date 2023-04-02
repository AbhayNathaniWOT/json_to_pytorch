# JSON To Pytorch 

### This program converts JSON Object to Pytorch Model

---

### Usage
```js
usage: python json_to_pytorch.py [-h] [--show_json] [--verbose] json_filename

This Program Converts JSON data to Pytorch Model

positional arguments:
  json_filename  Provide JSON File To Load

optional arguments:
  -h, --help     show this help message and exit
  --show_json    Prints JSON
  --verbose      Increases Output Verbosity
```

# Sample Result
```js
python json_to_pytorch.py json_model_1.json 
/home/abhi/Desktop/Json_to_code/json_to_pytorch.py:57: UserWarning: Implicit dimension choice for log_softmax has been deprecated. Change the call to include dim=X as an argument.
  x = layer(x)
----------------------------------------------------------------
        Layer (type)               Output Shape         Param #
================================================================
            Conv2d-1           [-1, 32, 26, 26]             320
              ReLU-2           [-1, 32, 26, 26]               0
            Conv2d-3           [-1, 64, 24, 24]          18,496
              ReLU-4           [-1, 64, 24, 24]               0
         MaxPool2d-5           [-1, 64, 12, 12]               0
           Dropout-6           [-1, 64, 12, 12]               0
           Flatten-7                 [-1, 9216]               0
            Linear-8                  [-1, 128]       1,179,776
              ReLU-9                  [-1, 128]               0
          Dropout-10                  [-1, 128]               0
           Linear-11                   [-1, 10]           1,290
       LogSoftmax-12                   [-1, 10]               0
================================================================
Total params: 1,199,882
Trainable params: 1,199,882
Non-trainable params: 0
----------------------------------------------------------------
Input size (MB): 0.00
Forward/backward pass size (MB): 1.11
Params size (MB): 4.58
Estimated Total Size (MB): 5.69
----------------------------------------------------------------

```
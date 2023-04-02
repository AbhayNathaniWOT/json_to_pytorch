import json
import argparse 
from sys import exit
try:
    from box import Box
except ImportError as e:
    print(e)
    print("Install Box Using Command: $ pip install python-box" )
    exit(11)

try:
    from torchsummary import summary
    import torch.nn as nn
except ImportError as e:
    print(e)
    print("Problem In Importing Torch" )
    print("Try installing: $ pip3 install torch torchvision torchaudio torchsummary")
    exit(11)


registered_layers = {
    "Conv2d":nn.Conv2d,
    "Dropout":nn.Dropout,
    "Linear":nn.Linear,
    "relu":nn.ReLU,
    "Log Softmax":nn.LogSoftmax,
    "Flatten": nn.Flatten,
    "Max Pool 2D":nn.MaxPool2d
}


def get_layer(json_model_layer,verbose):
    try:
        layer = registered_layers[json_model_layer.name](**json_model_layer.params)
        if verbose:print("Success Registering",json_model_layer.name)
        return layer
    except:
        print("Invalid Json Layer",json_model_layer.name)
        exit(55)







class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.deep_nn = nn.ModuleList()
        for n,layer in enumerate(json_model.model):            
            pyt_layer = get_layer(layer,verbose)
            self.deep_nn.add_module(f"{layer.name}{n}",pyt_layer)       

    def forward(self,x):
        for layer in self.deep_nn:
            x = layer(x)
        return x



if __name__=='__main__':

    parser = argparse.ArgumentParser(
        prog="python json_to_pytorch.py",
        description="This Program Converts JSON data to Pytorch Model"
    )
    parser.add_argument("json_filename",help="Provide JSON File To Load")
    parser.add_argument("--show_json",help="Prints JSON",action="store_true")
    parser.add_argument("--verbose",help="Increases Output Verbosity",action="store_true")
    
    args = parser.parse_args()
    json_filename = args.json_filename
    
    with open(json_filename,'rb') as f:
            json_model = json.load(f)
            json_model = Box(json_model)
    verbose = args.verbose
    
    if args.show_json:print(*json_model.model,sep="\n")
    summary(Net().cuda(), input_size=[(1, 28, 28)])
    

    

    



    

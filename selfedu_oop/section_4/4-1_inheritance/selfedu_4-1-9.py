"""Большой подвиг 9. Разработать функционал по построению моделей нейронных сетей."""

class Layer:
    def __init__(self, name='Layer'):
        self.name = name
        self.next_layer = None

    def __call__(self, next_layer):
        self.next_layer = next_layer
        return next_layer


class Input(Layer):
    def __init__(self, inputs:int):
        super().__init__("Input")
        self.name = 'Input'
        self.inputs = inputs


class Dense(Layer):
    def __init__(self, inputs:int, outputs:int, activation:str):
        super().__init__("Dense")
        self.name = 'Dense'
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation

class NetworkIterator:
    def __init__(self, network):
        self.network = network

    def __iter__(self):
        layer = self.network
        while layer:
            yield layer
            layer = layer.next_layer
    

first_layer = Layer()
next_layer = first_layer(Layer())
print(next_layer)
next_layer = next_layer(Layer())

network = Input(128)
layer = network(Dense(network.inputs, 1024, 'linear'))
layer = layer(Dense(layer.inputs, 10, 'softmax'))

for x in NetworkIterator(network):
    print(x.name)

# nt = Input(12)
# layer = nt(Dense(nt.inputs, 1024, 'relu'))
# layer = layer(Dense(layer.inputs, 2048, 'relu'))
# layer = layer(Dense(layer.inputs, 10, 'softmax'))

# n = 0
# for x in NetworkIterator(nt):
#     assert isinstance(x, Layer), "итератор должен возвращать объекты слоев с базовым классом Layer"
#     n += 1
    
# assert n == 4, "итератор перебрал неверное число слоев"
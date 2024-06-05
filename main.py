# Aritmetica de prueba
import numpy as np

inputs = [1.2, 5.1, 2.1]

weights = [[3.1, 2.1, 8.7],
           [3.1, 2.1, 8.7],
           [3.1, 2.1, 8.7]]

biases = [2, 3, 2]

# Lo haremos de la forma 'manual' sin numpy para hacer la equivalencia luego a FORTRAN Moderno

layer_outputs1 = []
layer_outputs2 = []
for neuron_weights, neuron_bias in zip(weights, biases):
    neuron_output = 0
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output = neuron_output + (n_input * weight)
    neuron_output = neuron_output + neuron_bias
    layer_outputs1.append(neuron_output)

layer_outputs2 = np.dot(weights, inputs)
print(layer_outputs1)
print(layer_outputs1)

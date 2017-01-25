At the top level of the project there will be a neural
network that, for a pair of words, takes as input the 
predictions of all the modules (aka predictors) and
produces the final output. In other words, the neural
network will perform regression over the input received
from the modules.

The modules are python functions that take two arguments 
(the first and the second word) and return a float in 
the range [0, 4]. Should a module not know what score to
assign to a pair of words it must return either 2 or
None.

Another component of the project is the command line
argument parser. This component is responsible for
parsing the arguments that were provided when calling
the program from the command line.

Along that, there will be three functions. One of them
for running the predictors on a file containing pairs
of words, one for training the neural network and saving
it to disk and the last one for running the neural
network.

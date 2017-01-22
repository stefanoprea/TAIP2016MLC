Download http://nlp.stanford.edu/data/glove.6B.zip

Extract it and copy glove.6B.300d.txt to the resources folder.

export LEX_JAR=/path/to/definitions.jar

export LEX_VECTOR=/path/to/glove.6B.300d.txt

pip install -r requirements.txt


To run the predictors on some word pairs:

python nn.py predict resources/word_pairs.txt -o predictions.txt


To train the neural network:

python nn.py train predictions.txt gold_standard.txt -o neural_network.xml


To run the neural network:

1. get predictions from the modules

python nn.py predict word_pairs_from_semeval.txt -o semeval_predictions.txt

2. actually run the neural network

python nn.py run neural_network.xml semeval_predictions.txt -o semeval_answers.txt


The final answers will be found in the semeval_answers.txt file
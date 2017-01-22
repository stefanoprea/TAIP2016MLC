import argparse
import traceback

from pybrain.datasets import SupervisedDataSet
from pybrain.tools.neuralnets import NNregression
from pybrain.tools.xml.networkreader import NetworkReader

from predictors.alina import synonyms, wup_similarity
from predictors.raluca import levenshtein_distance
from predictors.razvan import definition, lexical_field
from predictors.stefan import word2vec


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    parser_predict = subparsers.add_parser('predict', help='run the predictors')
    parser_predict.add_argument('pairs', help='file containing pairs of words separated by tabs')
    parser_predict.add_argument('-o', help='output file', default='predictions')
    parser_predict.set_defaults(which='predict')

    parser_build = subparsers.add_parser('build', help='trains a NN and saves it to disk')
    parser_build.add_argument('predictions', help='outcomes predicted by modules file')
    parser_build.add_argument('gold-standard', help='gold standard file')
    parser_build.add_argument('-o', help='output file', default='nn')
    parser_build.set_defaults(which='build')

    parser_run = subparsers.add_parser('run', help='run the NN and save results to disk')
    parser_run.add_argument('nn', help='NN file')
    parser_run.add_argument('predictions', help='outcomes predicted by modules file')
    parser_run.add_argument('-o', help='output file', default='output')
    parser_run.set_defaults(which='run')

    args = parser.parse_args()
    args = vars(args)

    if args['which'] == 'predict':
        predict(pairs_file=args['pairs'], output_file=args['o'])
    elif args['which'] == 'build':
        build(
            predictions_file=args['predictions'],
            gold_standard_file=args['gold-standard'],
            output_file=args['o']
        )
    elif args['which'] == 'run':
        run(
            neural_network_file=args['nn'],
            predictions_file=args['predictions'],
            output_file=args['o']
        )


def predict(pairs_file, output_file):
    predictors = [synonyms, wup_similarity, levenshtein_distance, definition, lexical_field, word2vec]
    predictions = []

    with open(pairs_file, 'r') as fin:
        pairs = list()
        for line in fin.readlines():
            if line.strip():
                pairs.append(line.strip().split('\t'))

    for pair in pairs:
        predictions_for_pair = list()
        for predictor in predictors:
            try:
                prediction = predictor(pair[0], pair[1])
                if isinstance(prediction, float):
                    prediction = round(prediction, 2)
                else:
                    prediction = 2  # default prediction; in between 0 and 4
            except Exception, err:
                print 'predictor "{0}" failed for pair "{1}" - "{2}"'.format(
                    predictor.__name__, pair[0], pair[1]
                )
                print traceback.format_exc(err)
                prediction = 2  # default prediction; in between 0 and 4
            predictions_for_pair.append(prediction)
        print '{0} - {1}: {2}'.format(pair[0], pair[1], ' '.join([str(p) for p in predictions_for_pair]))
        predictions.append(predictions_for_pair)

    # write predictions to output file
    with open(output_file, 'w') as fout:
        for p in predictions:
            fout.write(' '.join([str(i) for i in p]) + '\n')


def build(predictions_file, gold_standard_file, output_file):
    predictions = list()
    with open(predictions_file, 'r') as fin:
        for line in fin.readlines():
            predictions.append([float(v) for v in line.split(' ')])

    assert len(predictions) > 0, 'no predictions found'

    gold_standard = list()
    with open(gold_standard_file, 'r') as fin:
        for line in fin.readlines():
            if line:
                gold_standard.append(float(line))

    assert len(predictions) == len(gold_standard), '# predictions != # gold standard'

    num_modules = len(predictions[0])

    data_set = SupervisedDataSet(num_modules, 1)
    for p, gs in zip(predictions, gold_standard):
        data_set.appendLinked(p, gs)

    nn = NNregression(data_set)
    nn.setupNN()
    nn.runTraining()
    nn.saveNetwork(output_file)


def run(neural_network_file, predictions_file, output_file):
    nn = NetworkReader.readFrom(neural_network_file)
    with open(predictions_file, 'r') as fin:
        with open(output_file, 'w') as fout:
            for line in fin.readlines():
                predictions = [float(v) for v in line.split(' ')]
                fout.write(str(round(nn.activate(predictions), 2)) + '\n')


if __name__ == '__main__':
    main()

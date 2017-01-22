import os
import subprocess


def levenshtein_distance(word1, word2):
    (stdout, _) = subprocess.Popen(
        ['java', '-jar', os.environ['LEX_JAR'], word1, word2],
        stdout=subprocess.PIPE
    ).communicate()
    return round(float(stdout.strip()), 2)


if __name__ == '__main__':
    print levenshtein_distance("cat", "dog")

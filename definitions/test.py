import subprocess
word1="tree"
word2="forest"
proc = subprocess.Popen(['java', '-jar', 'definitions.jar', word1, word2], stdout=subprocess.PIPE)
line = proc.stdout.readline()
print(line.rstrip().decode('utf-8'))

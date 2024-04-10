import optuna
import subprocess

# Define the objective function for hyperparameter optimization
def objective(trial,size):
    # Define hyperparameters to optimize
    mp = trial.suggest_float('mp', 0.01, 0.3)
    gmp = trial.suggest_float('gmp', 0.01, 0.3)
    select = trial.suggest_int('select', 1, 5)
    cp = trial.suggest_float('cp', 0.8, 1.0)
    cmd = ['java', "Genetic_New", '16','1000',str(mp),str(gmp),str(select),str(cp),str(size)]
    p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    accuracy = float(p1.stdout.read())
    return accuracy
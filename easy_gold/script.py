def run(command):
    os.system('export PYTHONPATH=${PYTHONPATH}:/kaggle/working && ' + command)

run('python setup.py develop --install-dir /kaggle/working')
run('python titanic_sample/train.py model.text --test_size 0.3')
run('python titanic_sample/predict.py model.text submission.csv')

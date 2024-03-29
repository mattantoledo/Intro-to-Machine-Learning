import pickle

import gzip



import numpy as np



def load(train_size, test_size):

    """Return a tuple containing ``(training_data, test_data)``.

    In particular, ``train_from_file`` is a list containing 50,000

    2-tuples ``(x, y)``.  ``x`` is a 784-dimensional numpy.ndarray

    containing the input image.  ``y`` is a 10-dimensional

    numpy.ndarray representing the unit vector corresponding to the

    correct digit for ``x``.



    ``test_from_file`` is a list containing 10,000

    2-tuples ``(x, y)``.  In each case, ``x`` is a 784-dimensional

    numpy.ndarry containing the input image, and ``y`` is the

    corresponding classification, i.e., the digit values (integers)

    corresponding to ``x``.



    Hence, we're using different label formats for

    the training data and the test data.  """

    f = gzip.open('mnist.pkl.gz', 'rb')

    train_from_file, validation_from_file, test_from_file = pickle.load(f, encoding='iso-8859-1')

    f.close()

    training_inputs = [np.reshape(x, (784, 1)) for x in train_from_file[0]]

    training_results = [vectorized_result(y) for y in train_from_file[1]]

    training_data = list(zip(training_inputs, training_results))

    test_inputs = [np.reshape(x, (784, 1)) for x in test_from_file[0]]

    test_data = list(zip(test_inputs, test_from_file[1]))

    np.random.seed(8)

    training_idx = np.random.choice(50000,train_size, replace=False)

    training_data = [training_data[i] for i in training_idx]

    test_idx = np.random.choice(10000,test_size, replace=False)

    test_data = [test_data[i] for i in test_idx]

    return (training_data, test_data)



def vectorized_result(j):

    """Return a 10-dimensional unit vector with a 1.0 in the jth

    position and zeroes elsewhere.  This is used to convert a digit

    (0...9) into a corresponding desired output from the neural

    network."""

    e = np.zeros((10, 1))

    e[j] = 1.0

    return e

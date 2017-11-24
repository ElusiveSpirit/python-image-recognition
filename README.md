# Python Image Recognition

Simple demo app to recognize hand written digits with 3 layers neural net in pure python

[Try demo](https://python-image-recognition.herokuapp.com/)

## Run locally

1. Install the dependencies
```bash
> pip install -r requirements.txt
```

2. Run the server
```bash
> gunicorn app:app
[2017-11-24 17:29:40 +0300] [22162] [INFO] Starting gunicorn 19.7.1
[2017-11-24 17:29:40 +0300] [22162] [INFO] Listening at: http://127.0.0.1:8000 (22162)
[2017-11-24 17:29:40 +0300] [22162] [INFO] Using worker: sync
[2017-11-24 17:29:40 +0300] [22165] [INFO] Booting worker with pid: 22165
```

3. Open http://127.0.0.1:8000 in your browser or try demo

## Teach

Open any python interpreter

1. Get training data
```python
import mnist_loader

training_data, validation_data, test_data = mnist_loader.load_data_wrapper()
training_data = list(training_data)
test_data = list(test_data)
```

2. Start teaching with your parameters
```python
from network import Network

# 784 - input layer (28x28 pic size)
# 30  - hidden layer (any value)
# 10  - output layer (from 0 to 9) 
# You should change only hidden layer
net = Network([784, 30, 10])
# Feel free to change this parameters
# 20  - epoch count
# 10  - batch size
# 3.0 - training speed
net.train(training_data, 20, 10, 3.0, test_data)
net.save_to_file('./networks/network_30_20-10-3.json')
```

## Contribute

Feel free to contribute, rewrite, improve or do it with TensorFlow

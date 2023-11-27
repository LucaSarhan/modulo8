import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.1, n_interations=100, threshold=0.5):
        self.learning_rate = learning_rate
        self.n_interations = n_interations
        self.threshold = threshold
        self.weights = np.zeros(2)
        self.bias = 0

    def activation_function(self, x):
        return 1 if x >= self.threshold else 0

    def predict(self, inputs):
        #calcula a soma ponderada das entradas
        linear_output = np.dot(inputs, self.weights) + self.bias
        #aplica a função de ativação degrau para determinar a saída
        y_pred = self.activation_function(linear_output)
        return y_pred
    
    def train(self, X, y):
        for _ in range(self.n_interations):
            for x, y_true in zip(X, y):
                y_pred = self.predict(x)
                error = y_true - y_pred
                self.weights += error * self.learning_rate * x
                self.bias += error * self.learning_rate

def main():
    # Dados para a porta AND
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    yand = np.array([0, 0, 0, 1]) 
    yor = np.array([0, 1, 1, 1])  
    ynand = np.array([1, 1, 1, 0])
    yxor = np.array([0, 1, 1, 0])

    models = {
        "AND": yand,
        "OR": yor,
        "NAND": ynand,
    }

    for model_name, model in models.items():
        
        print(f"Model: {model_name}")
        
        # Treinando o Perceptron
        perceptron = Perceptron()
        perceptron.train(X, model)

        # Testando o Perceptron
        print(f"in (0, 0), out: {perceptron.predict([0, 0])}")
        print(f"in (0, 1), out: {perceptron.predict([0, 1])}")
        print(f"in (1, 0), out: {perceptron.predict([1, 0])}")
        print(f"in (1, 1), out: {perceptron.predict([1, 1])}")
        print()

    # Treinando os Perceptrons
    perceptron1 = Perceptron()
    perceptron1.train(X, yand)
    perceptron2 = Perceptron()
    perceptron2.train(X, ynand)

    # Testando os Perceptrons
    print(f"Model: XOR")
    print(f"in (0, 0), out: {perceptron1.predict([perceptron2.predict([0, 0]), 0])}")
    print(f"in (0, 1), out: {perceptron1.predict([perceptron2.predict([0, 1]), 1])}")
    print(f"in (1, 0), out: {perceptron1.predict([perceptron2.predict([1, 0]), 1])}")
    print(f"in (1, 1), out: {perceptron1.predict([perceptron2.predict([1, 1]), 0])}")
    print()

if __name__ == "__main__":
    main()
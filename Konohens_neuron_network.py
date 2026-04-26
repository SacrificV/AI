import time
import random
import math

# --- Константы и настройки сети ---
numInpNeurons = 2  # Количество нейронов входного слоя
numHidNeurons1 = 3  # Количество нейронов первого скрытого слоя
numHidNeurons2 = 2  # Количество нейронов второго скрытого слоя
numOutNeurons = 1  # Количество нейронов выходного слоя
numVectors = 8  # Количество обучающих векторов

# Порог обучения сети в процентах
learningLimit = 85

# Норма обучения (Learning Rate)
rateTraining = 0.1

# Момент (Momentum)
y = 0.1

# Количество эпох
numberEpochs = 950000

# --- Данные для обучения ---
dataSensor = [
    [0.11, 0.32],
    [0.68, 0.89],
    [0.03, 0.44],
    [0.69, 0.70],
    [0.32, 0.05],
    [0.89, 0.50],
    [0.43, 0.32],
    [0.60, 0.55]
]

expectedOutput = [0.2, 0.7, 0.2, 0.7, 0.2, 0.7, 0.2, 0.7]

# --- Инициализация весов ---
# inputWeights1: [numHidNeurons1][numInpNeurons] -> [3][2] 
inputWeights1 = [
    [-1.00, 1.00],
    [2.50, 0.40],
    [1.00, -1.50]
]

# inputWeights2: [numHidNeurons2][numHidNeurons1] -> [2][3]
inputWeights2 = [
    [2.20, -1.40, 0.56],
    [0.34, 1.05, 3.10]
]

# outputWeights: [numOutNeurons][numHidNeurons2] -> [1][2]
outputWeights = [[0.75, -0.22]]

# --- Переменные для хранения промежуточных результатов ---
hiddenCombined1 = [0.0] * numHidNeurons1
activityNeuron1 = [0.0] * numHidNeurons1

hiddenCombined2 = [0.0] * numHidNeurons2
activityNeuron2 = [0.0] * numHidNeurons2

outputCombined = 0.0
activityOutputNeuron = 0.0
errorOutputNeuron = 0.0

# Матрицы для изменения весов (Momentum buffers)
# weightChange2: [numOutNeurons][numHidNeurons2] -> [1][2]
weightChange2 = [[0.0 for _ in range(numHidNeurons2)] for _ in range(numOutNeurons)]

# weightChange1: [numHidNeurons2][numHidNeurons1] -> [2][3] (Строка - нейрон слоя 2, Столбец - нейрон слоя 1)
weightChange1 = [[0.0 for _ in range(numHidNeurons1)] for _ in range(numHidNeurons2)]

# weightChangeInput: [numHidNeurons1][numInpNeurons] -> [3][2]
weightChangeInput = [[0.0 for _ in range(numInpNeurons)] for _ in range(numHidNeurons1)]

# Ошибки скрытых слоев
errorHiddenNeuron1 = [0.0] * numHidNeurons1
errorHiddenNeuron2 = [0.0] * numHidNeurons2

currentOutput = [0.0] * numVectors
sumErrors = 0.0
arithmeticMeanErrors = 0.0


# Функция активации (Сигмоида)
def activationFunction(combinedInput):
    # 1 / (1 + exp(-x))
    return 1.0 / (1.0 + math.exp(-combinedInput))


def outputTrainedWeights():
    print("\n" + "=" * 60)
    print("inputWeights1 ( Обученные веса: Вход -> Скрытый 1 )")
    for i in range(numHidNeurons1):
        row = [f"{w:.2f}" for w in inputWeights1[i]]
        print(f"  {row}")

    print("\ninputWeights2 ( Обученные веса: Скрытый 1 -> Скрытый 2 )")
    for i in range(numHidNeurons2):
        row = [f"{w:.2f}" for w in inputWeights2[i]]
        print(f"  {row}")

    print("\noutputWeights ( Обученные веса: Скрытый 2 -> Выход )")
    row = [f"{w:.2f}" for w in outputWeights[0]]
    print(f"  {row}")

    print("\ncurrentOutput ( Текущие выходы сети )")
    formatted_output = []
    for i in range(numVectors):
        formatted_output.append(f"{currentOutput[i]:.4f}")
    print(f"  {', '.join(formatted_output)}")


def dataPortMonitorOutput():
    print("\n" + "=" * 60)
    print("dataSensor ( Входные данные для обучения )")
    for i in range(numVectors):
        row = [f"{d:.2f}" for d in dataSensor[i]]
        print(f"  {row}")

    print("\nexpectedOutput ( Ожидаемые выходы )")
    print(f"  {[round(w, 2) for w in expectedOutput]}")

    print("\ninputWeights1 ( Начальные веса: Вход -> Скрытый 1 )")
    for i in range(numHidNeurons1):
        row = [f"{w:.2f}" for w in inputWeights1[i]]
        print(f"  {row}")

    print("\ninputWeights2 ( Начальные веса: Скрытый 1 -> Скрытый 2 )")
    for i in range(numHidNeurons2):
        row = [f"{w:.2f}" for w in inputWeights2[i]]
        print(f"  {row}")

    print("\noutputWeights ( Начальные веса: Скрытый 2 -> Выход )")
    row = [f"{w:.2f}" for w in outputWeights[0]]
    print(f"  {row}")

    print("\nСтарт работы сети")


def trainKohonenNetwork():
    global sumErrors, arithmeticMeanErrors

    # Сброс сумм ошибок для новой эпохи
    sumErrors = 0.0

    for vectorIdx in range(numVectors):
        # --- Прямое распространение (Forward Pass) ---

        # Слой 1
        for i in range(numHidNeurons1):
            hiddenCombined1[i] = 0.0
            for j in range(numInpNeurons):
                hiddenCombined1[i] += dataSensor[vectorIdx][j] * inputWeights1[i][j]
            activityNeuron1[i] = activationFunction(hiddenCombined1[i])

        # Слой 2
        for i in range(numHidNeurons2):
            hiddenCombined2[i] = 0.0
            for j in range(numHidNeurons1):
                hiddenCombined2[i] += activityNeuron1[j] * inputWeights2[i][j]
            activityNeuron2[i] = activationFunction(hiddenCombined2[i])

        # Выходной слой
        outputCombined = 0.0
        for i in range(numHidNeurons2):
            outputCombined += activityNeuron2[i] * outputWeights[0][i]
        activityOutputNeuron = activationFunction(outputCombined)

        # --- Обратное распространение (Backward Pass) ---

        # Ошибка выходного нейрона
        errorOutputNeuron = expectedOutput[vectorIdx] - activityOutputNeuron
        sumErrors += abs(errorOutputNeuron)

        # Слой 2 -> Выход
        for i in range(numHidNeurons2):
            # Ошибка скрытого нейрона 
            errorHiddenNeuron2[i] = outputWeights[0][i] * errorOutputNeuron * activityNeuron2[i] * (
                        1 - activityNeuron2[i])

            # Обновление весов со моментом
            weightChange2[0][i] = rateTraining * errorOutputNeuron * activityNeuron2[i] + y * weightChange2[0][i]
            outputWeights[0][i] += weightChange2[0][i]

        # Слой 1 -> Слой 2 (ИСПРАВЛЕННАЯ ЧАСТЬ)
        for i in range(numHidNeurons1):  # i - индекс нейрона слоя 1 (0..2)
            errorHiddenNeuron1[i] = 0.0

            # Вычисляем ошибку для нейрона i слоя 1, суммируя ошибки от всех нейронов слоя 2
            for j in range(numHidNeurons2):  # j - индекс нейрона слоя 2 (0..1)
                # inputWeights2[j][i] соответствует весу от нейрона j (слой 2) к нейрону i (слой 1)
                errorHiddenNeuron1[i] += inputWeights2[j][i] * errorHiddenNeuron2[j]

            # Добавляем производную сигмоиды для скрытого слоя
            derivative = activityNeuron1[i] * (1 - activityNeuron1[i])
            errorHiddenNeuron1[i] *= derivative

            # Обновление весов inputWeights2
            # inputWeights2 имеет размер [numHidNeurons2][numHidNeurons1].
            # Нам нужно обновить веса, идущие ОТ нейрона i (слой 1) ко всем нейронам j (слой 2).
            # В матрице inputWeights2 это элементы [j][i].

            for j in range(numHidNeurons2):
                # Формула: delta = lr * error_hidden_layer_1 * activation_input
                # Здесь errorHiddenNeuron1[i] - ошибка нейрона i слоя 1.
                # activityNeuron1[i] - активность этого же нейрона (вход для следующего слоя).

                delta = rateTraining * errorHiddenNeuron1[i] * activityNeuron1[i] + y * weightChange1[j][i]
                weightChange1[j][i] = delta
                inputWeights2[j][i] += weightChange1[j][i]

        # Входной слой -> Слой 1
        for i in range(numInpNeurons):
            for j in range(numHidNeurons1):
                derivative = activityNeuron1[j] * (1 - activityNeuron1[j])

                weightChangeInput[j][i] = rateTraining * errorHiddenNeuron1[j] * dataSensor[vectorIdx][i] + y * \
                                          weightChangeInput[j][i]
                inputWeights1[j][i] += weightChangeInput[j][i]

    # Расчет средней ошибки эпохи
    arithmeticMeanErrors = sumErrors / numVectors


def main():
    global counterEpoch, networkProgress

    dataPortMonitorOutput()

    while True:
        trainKohonenNetwork()

        # --- Финальный проход для сбора статистики---
        for vectorIdx in range(numVectors):
            h1 = [activationFunction(sum(dataSensor[vectorIdx][k] * inputWeights1[i][k] for k in range(numInpNeurons)))
                  for i in range(numHidNeurons1)]
            h2 = [activationFunction(sum(h1[j] * inputWeights2[i][j] for j in range(numHidNeurons1)))
                  for i in range(numHidNeurons2)]
            out_val = activationFunction(sum(h2[i] * outputWeights[0][i] for i in range(numHidNeurons2)))
            currentOutput[vectorIdx] = out_val

        # Расчет времени обучения сети (в секундах)
        studyingTime = time.time()

        # Расчет прогресса сети
        lastVectorIdx = numVectors - 1
        h1_last = [
            activationFunction(sum(dataSensor[lastVectorIdx][k] * inputWeights1[i][k] for k in range(numInpNeurons)))
            for i in range(numHidNeurons1)]
        h2_last = [activationFunction(sum(h1_last[j] * inputWeights2[i][j] for j in range(numHidNeurons1)))
                   for i in range(numHidNeurons2)]
        out_val_last = activationFunction(sum(h2_last[i] * outputWeights[0][i] for i in range(numHidNeurons2)))

        errorOutputNeuron = expectedOutput[lastVectorIdx] - out_val_last
        networkProgress = abs(100 - (100 * abs(errorOutputNeuron)))

        # Вывод текущей информации
        print(f"AMErrors: {arithmeticMeanErrors:.4f}")
        print(f"minProgress: {networkProgress:.2f} %")

        print(f"Time: {studyingTime:.2f} c")

        # Завершение работы сети
        if networkProgress >= learningLimit:
            outputTrainedWeights()
            break

        # time.sleep(0.001)

    return


if __name__ == "__main__":
    main()

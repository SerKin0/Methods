def print_matrix(matrix: list, text: str = "Matrix: "):
    print(text)
    for y in matrix:
        for x in y:
            print("%.2f" % x, end=" ")
        print()


# _______________________________Input matrix_________________________________________
size_matrix = 3  # Пример размера матрицы
matrix = [
    [2, 4, 1, 36],
    [5, 2, 1, 47],
    [2, 3, 4, 37]
]
print_matrix(matrix)


# ________________________________Method Gauss______________________________________________
def swap_string(matrix: list, first_index: int, second_index: int) -> None:
    temp = matrix[first_index]
    matrix[first_index] = matrix[second_index]
    matrix[second_index] = temp


def swap_max_string(matrix: list, start_line: int) -> None:
    temp = [matrix[i][start_line] for i in range(start_line, len(matrix))]
    index_max = temp.index(max(temp)) + start_line
    swap_string(matrix, start_line, index_max)


def gauss(matrix: list, size_matrix: int):
    for i in range(size_matrix):
        swap_max_string(matrix, i)

        if matrix[i][i] == 0:  # Проверяем на ноль на диагонали, чтобы избежать деления на ноль
            print("Система не имеет однозначного решения или имеет бесконечное количество решений")
            return None

        # Деление элементов строки на первый ненулевой элемент строки
        matrix[i] = [element / matrix[i][i] for element in matrix[i]]

        for j in range(size_matrix):
            if i != j:
                # Вычитаем i-ю строку из последующих строк
                temp = []
                for k in range(size_matrix + 1):
                    temp.append(matrix[j][k] - matrix[i][k] * matrix[j][i])

                matrix[j] = temp

    return [row[-1] for row in matrix]  # Возвращаем решения


print(gauss(matrix, size_matrix))

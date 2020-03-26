import numpy as np

# Hàm tạo ma trận
def make_matrix(n):
    # n là số dòng của ma trận, ma trận vuông nên 2 thứ bằng nhau
    # sử dụng numpy arrays
    return np.zeros((n, n))

# Hàm nhập
def set_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = int(input('Enther element at row %d, col %d\n>>> ' %(i, j)))

# Ghi ma trận vào file
def write_file(matrix):
    f = open('Input.txt', 'w')
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            f.write(str(matrix[i][j]) + ',')
        f.write('\n')
    f.close()

def read_file(n):
    f = open('Input.txt', 'r')
    matrix = []
    for i in range(n):
        line = f.readline()
        line_len = len(line)
        line = line[0:line_len - 2]
        arr_str = line.split(',')
        arow = []
        for str in arr_str:
            arow.append(float(str))
        matrix.append(arow)
    f.close()
    return np.array(matrix)

# Hàm main
def main():
    n = int(input('Input n = '))
    matrix = make_matrix(n) # Tạo ma trận 0 bằng numpy
    set_matrix(matrix) # Nhập giá trị cho ma trận
    print(matrix)

    write_file(matrix) # Ghi ma trận vào file

main()
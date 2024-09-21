import numpy as np

def read_vectors_and_dot_product(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # if len(lines) % 3 != 0:
    #     raise ValueError("文件行数不是3的倍数，每组三行数据不完整。")

    for i in range(0, len(lines), 3):
        # 读取每组三行
        vector1_str = lines[i].strip().split()
        vector1 = np.array([1 if x == '1' else -1 if x == '3' else 0 for x in vector1_str])
        
        vector2 = np.fromstring(lines[i + 1].strip(), sep=' ')
        expected_dot_product = float(lines[i + 2].strip())

        # 计算点积
        calculated_dot_product = np.dot(vector1, vector2)

        # 验证结果
        if np.isclose(calculated_dot_product, expected_dot_product):
            print(f"第 {i//3 + 1} 组数据验证通过。")
        else:
            print(f"第 {i//3 + 1} 组数据验证失败。")
            print(f"向量1: {vector1}")
            print(f"向量2: {vector2}")
            print(f"预期点积: {expected_dot_product}")
            print(f"计算点积: {calculated_dot_product}")

if __name__ == "__main__":
    file_path = "/home/cipherxzc/Projects/tensor"
    read_vectors_and_dot_product(file_path)

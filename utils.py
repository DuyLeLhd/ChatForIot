import ast
import os


def load_n_grams(file_path):

    with open(file_path, encoding="utf8") as fr:
        words = fr.read()
        words = ast.literal_eval(words)
    return words

def clean_html(html):
    from bs4 import BeautifulSoup   #Thư viện dùng để lấy dữ liệu ra khỏi file html và xml

    soup = BeautifulSoup(html)
    text = soup.get_text()
    return text


def clean_html_file(input_path, output_path):

    if os.path.exists(output_path):     #Kiểm tra xem file có tồn tại không
        raise Exception("Output path existed")
    with open(input_path, 'r') as fr:
        html = fr.read()
        text = clean_html(html)

    lines = text.split('\n')    #Chia chuỗi trả về các chuỗi con

    with open(output_path, 'w') as fw:
        for line in lines:
            if len(line.strip()) > 0:   #line.strip(a) trả về 1 chuỗi string đã loại đi ký tự a
                fw.write(line + "\n")


def clean_files_from_dir(input_dir, output_dir):
    """
    Clean html tags for files in a directory
    :param input_dir: path to directory
    :param output_dir: path to output director
    :return: None
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir) #Tạo thư mục
    input_files = os.listdir(input_dir)     #trả về một danh sách chứa tên của các mục trong thư mục được cung cấp bởi đường dẫn. Danh sách theo thứ tự tùy ý. Nó không bao gồm các mục đặc biệt '.' và '..' ngay cả khi chúng có trong thư mục.
    for input_file in input_files:
        input_file_path = os.path.join(input_dir, input_file)
        if input_file.startswith('.') or os.path.isdir(input_file_path):
            continue
        output_file_path = os.path.join(output_dir, input_file)
        clean_html_file(input_file_path, output_file_path)

"""Tests"""

def test_clean_file():
    data_path = '../data/tokenized/samples/html/html_data.txt'
    output_path = '../data/tokenized/samples/training/data.txt'
    clean_html_file(data_path, output_path)


def test_clean_files_in_dir():
    input_dir = '../data/tokenized/real/html'
    output_dir = '../data/tokenized/real/training'
    clean_files_from_dir(input_dir, output_dir)


if __name__ == '__main__':
    # test_clean_file()
    test_clean_files_in_dir()

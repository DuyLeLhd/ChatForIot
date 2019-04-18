from base_tokenizer import BaseTokenizer
from utils import load_n_grams


class LongMatchingTokenizer(BaseTokenizer):
    def __init__(self, bi_grams_path='bi_grams.txt', tri_grams_path='tri_grams.txt'):
        # lib_grams_path = 'VNTQcorpus-big.txt'):

        self.bi_grams = load_n_grams(bi_grams_path)
        self.tri_grams = load_n_grams(tri_grams_path)
        # self.lib_grams = load_n_grams(lib_grams_path)
    def tokenize(self, text):

        syllables = LongMatchingTokenizer.syllablize(text)  #Tách câu thành 1 mảng các từ riêng biệt
        syl_len = len(syllables)    #Chiều dài mảng
        curr_id = 0
        word_list = []
        done = False
        #Trong khi từ hiện tại nhỏ hơn chiều dài câu
        while (curr_id < syl_len) and (not done):
            curr_word = syllables[curr_id] 
            if curr_id >= (syl_len - 1):
                word_list.append(curr_word) #Thêm curr_word vào cuối danh sách
                done = True
            else:
                next_word = syllables[curr_id + 1]
                #Nối chuỗi join
                pair_word = ' '.join([curr_word.lower(), next_word.lower()])   
                if curr_id >= (syl_len - 2):
                    #Nếu pair_word có trong bi_gram thì từ đó có nghĩa
                    if pair_word in self.bi_grams:
                        word_list.append(' '.join([curr_word, next_word])) 
                        curr_id += 2
                    else:
                        word_list.append(curr_word)
                        curr_id += 1
                else:
                    next_next_word = syllables[curr_id + 2]
                    triple_word = ' '.join([pair_word, next_next_word.lower()])
                    if triple_word in self.tri_grams:
                        word_list.append(' '.join([curr_word, next_word, next_next_word]))
                        curr_id += 3
                    elif pair_word in self.bi_grams:
                        word_list.append(' '.join([curr_word, next_word]))
                        curr_id += 2
                    else:
                        word_list.append(curr_word)
                        curr_id += 1
                
        return word_list



def test():
    s = input()
    lm_tokenizer = LongMatchingTokenizer()
    tokens = lm_tokenizer.tokenize(s)
    print(tokens)
    print(tokens[1])
if __name__ == '__main__':
    test()

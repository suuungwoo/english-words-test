import numpy as np
import re
import random

source = "english_words_01.txt"
n_tests = 50
n_questions = 50


def create_words_dict(source):
    english_words = []
    meanings = []
    with open(source) as f:
        for i, row in enumerate(f):
            row = re.sub("\n", "", row)
            if i % 3 == 0:
                english_words.append(row)
            elif i % 3 == 1:
                meanings.append(row)

    words_dict = dict(zip(english_words, meanings))

    return english_words, meanings, words_dict


if __name__ == "__main__":
    english_words, meanings, words_dict = create_words_dict(source)

    for test_num in range(n_tests):
        with open("dest/english_words_test_{:02d}.txt".format(test_num + 1),
                  "w") as f:
            f.write("出席番号：\n"
                    "名前：\n\n"
                    "第{}回英単語テスト\n\n".format(test_num + 1))

            random_index = np.random.randint(low=0, high=50, size=50)

            for question_num in range(n_questions):
                question_word = english_words[random_index[question_num]]
                correct_answer = words_dict[question_word]

                meanings_copy = meanings.copy()
                meanings_copy.remove(correct_answer)
                wrong_answers = random.sample(meanings_copy, 3)

                answer_options = [correct_answer] + wrong_answers

                random.shuffle(answer_options)

                f.write("問{}. {}\n\n".format(question_num + 1, question_word))
                for i, answer_option in enumerate(answer_options):
                    f.write("{}. {}\n".format(i + 1, answer_option))
                f.write("\n\n")

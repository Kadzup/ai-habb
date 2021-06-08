#%%
DATA_FILENAME = 'input.txt'
MATRIX_SIZE = 5

K = (
    -1,  1, -1, -1,  1,
    -1,  1, -1,  1, -1,
    -1,  1,  1, -1, -1,
    -1,  1, -1,  1, -1,
    -1,  1, -1, -1,  1
)

S = (
    -1,  1,  1,  1, -1,
    -1,  1, -1, -1, -1,
    -1,  1,  1,  1, -1,
    -1, -1, -1,  1, -1,
    -1,  1,  1,  1, -1
)


def train(l1, l2):
    uw, ub = [], []
    for x in l1:
        uw.append(x * -1)
        ub.append(-1)

    n_uw, n_ub = [], []
    for i in range(len(l2)):
        n_uw.append(uw[i] + l2[i])
        n_ub.append(ub[i] + 1)

    return n_uw, n_ub


def recognize(n_uw, n_ub, letter):
    res_value = 0
    for i in range(len(letter)):
        res_value += n_uw[i] * letter[i] + n_ub[i]
    return res_value


def parse_letter(letter):
    result = []
    for line in letter.split('\n'):
        result += [int(x) for x in line.split(', ')]
    return result


def get_letters(filename):
    with open(filename) as file:
        result = file.read()
        letters = result.split('\n\n')
        return [parse_letter(x) for x in letters]


def print_letter(letter):
    index = 0
    for x in letter:
        index += 1
        print('•' if x == 1 else ' ', end='\n' if index %
              MATRIX_SIZE == 0 else ' ')


if __name__ == '__main__':
    print('Letter K: ')
    print_letter(K)

    print('\nLetter S: ')
    print_letter(S)

    print('\nInput test data')

    n_uw, n_ub = train(K, S)
    for letter in get_letters(DATA_FILENAME):
        print('[BEGIN]\n')
        print_letter(letter)
        print('\n')

        result_value = recognize(n_uw, n_ub, letter)
        if result_value < 0:
            print('Letter is K')
        elif result_value > 0:
            print('Letter is S')
        else:
            print('Can\'t recognize letter')

        print('[END]\n')

# %%

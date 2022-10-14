def log_expr(a):
    with open('fileSem7.txt', 'w', encoding = 'utf-8') as f:
        f.write(f'Уравнение: {a} = 0 \n')

def log_ans(b):
    with open('fileSem7.txt', 'a', encoding = 'utf-8') as g:
        g.write(f'Корни уравнения: {b} \n')

import model
import logger

# получение уравнения от пользователя
def get_expr():
    return input()

# вывод информации
def show_res(a):
    print(a)

expression = get_expr() # вызов функции
logger.log_expr(expression)
answer = model.evaluate_expr(expression) # получение решения
logger.log_ans(answer)
show_res(answer) # вывод ответа



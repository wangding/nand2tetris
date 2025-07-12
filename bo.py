import itertools
import re

def generate_truth_table(logic_expr):
    # 提取变量名（只匹配小写或大写字母组成的变量）
    variables = sorted(set(re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', logic_expr)))
    variables = [x for x in variables if len(x)==1]
    print(variables)
    
    # 生成所有可能的变量组合（0 或 1）
    combinations = list(itertools.product([0, 1], repeat=len(variables)))
    
    # 打印真值表
    for combo in combinations:
        # 将变量与当前组合绑定
        env = dict(zip(variables, combo))
        
        # 计算表达式值（使用 eval，在安全环境下可用）
        try:
            result = int(eval(logic_expr, {}, env))
        except Exception as e:
            print("表达式错误:", e)
            return
        
        # 打印输入和结果
        print(' '.join(map(str, combo + (result,))))

# 测试
logic_input = input('请输入逻辑表达式：')
generate_truth_table(logic_input)

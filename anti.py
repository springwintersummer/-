code=[]
#读取代码文件
def read_txt(file,code):
    with open(file) as f:
        line=f.readline()
        code.append(line)
        while line:
            line=f.readline()
            code.append(line)
    for i in range (0,len(code)):
        j=code[i]
        j=j.replace(" ","")
        j = j.replace("\n", "")
        code[i]=j
    while '' in code:
        code.remove('')
    return code

#存储常见的安全库函数
unsafe_functions=[]
#用于存储比较指令操作数中的立即数值
constantlist=[]
#存储存在有对不安全库函数调用指令的函数首地址
functionlist=[]

#反汇编指定地址处的二进制指令，得到相应的汇编代码，并在汇编指令中查找指定的字符串
def disasm_match():
    return 0

#获取指定地址处的指令中所引用的常量数值
def get_constant_ref():
    return 0

#判定指定地址处的指令处的指令中的助记符和操作数与给定的相应参数是否匹配
def instruction_match():
    return 0

#在PIDA分析文件中查找给定地址所在函数块，并将functionlist中不存在的函数首地址添进去
def find_func():
    return 0

#IDA的IDC接口函数，通过函数名称查找所在地址
def LocByName():
    return 0


#所有可能接受外部输入的函数列表，包含函数所在的模块名称和函数名称
recv_functions=[]

#返回给定的调试上下文中的函数（所在模块名，函数名）的对应地址
def func_resolve():
    return 0

#在指定的代码地址设置中断点，并可指定处理断点异常的回调函数
def bp_set():
    return 0

#在指定的内存位置设置内存中断点，通过修改内存地址所在页的访问权限来实现
def bp_set_mem():
    return 0

def find_function():
    return 0

#读取进程中指定内存地址处的给定长度的数据内容
def read_process_memory():
    return 0


#存放针对缓冲区溢出类漏洞的测试用例列表
overflow=[]
#存放针对格式化字符串类漏洞的测试用例列表
format_string=[]
#存放针对整数溢出类漏洞的测试用例列表
int_overflow=[]
#存放针对目录遍历类漏洞的测试用例列表
dir_traverse=[]
#存放针对命令注入类漏洞的测试用例列表
command_inject=[]
#用于存储比较指令操作数中的立即数值
constantlist=[]



#获取所跟踪进程的内存和线程上下文的快照，调用前所有线程必须被挂起
def process_snapshot():
    return 0
#将所跟踪进程的内存和线程上下文恢复为之前保存的快照内容，同样调用前有线程必须被挂起
def process_restore():
    return 0
#将数据写入到指定的内存空间中
def write_process_memory():
    return 0


if __name__ == "__main__":
    read_txt("code.txt",code)
    print(code)
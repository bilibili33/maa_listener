import sys
import time
import psutil


def logger(s):
    return "Log: " + time.ctime() + " >> " + s


def do_file(t="r", s=""):
    if t != "r" and t != "w":
        return "wrong arg"
    try:
        with open("stat.log") as f:
            data = f.read()
        # print(data)
    except FileNotFoundError:
        if t == "r":
            return ""
        elif t == "w":
            data = ""
    if t == "w":
        if s == data:
            return "File: no change"
        else:
            with open("stat.log", "w") as f:
                f.write(s)
            return "File: write ok"


def read_args():
    arg_list = []
    def_info = "参数错误，参数1为进程名（需要写exe后缀，默认MAA.exe），参数2为等待时间（默认300s，最长600s，不用写s）"
    if len(sys.argv) == 1:
        pass
    elif len(sys.argv) > 3 or len(sys.argv) == 2:
        return def_info
    else:
        try:
            arg1 = sys.argv[1]
            int(arg1)
            # 匹配通过就return报错
            return def_info
        except ValueError:
            # 正确匹配出口
            arg_list.append(sys.argv[1])
        try:
            arg2 = sys.argv[2]
            if int(arg2) < 5 or int(arg2) > 600:
                return def_info
            # 正确匹配出口
            arg_list.append(arg2)
        except ValueError:
            return def_info
        return arg_list


def foo(p_name="MAA.exe", sleep_time=300):
    p_list = []
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() == p_name:
            p_list.append(str(p.pid))
        else:
            pass
    if len(p_list) == 0:
        print(logger("0个" + p_name + "进程"))
        print(logger(do_file("w", "no")))
    else:
        info = str(len(p_list)) + "个" + p_name + "进程:" + ",".join(p_list)
        print(logger(info))
        print(logger(do_file("w", "yes")))
    time.sleep(sleep_time)


if __name__ == '__main__':
    get_args = read_args()
    if type(get_args) == list:
        print("自定义参数：进程：" + get_args[0] + " 等待时间：" + get_args[1])
        while True:
            try:
                foo(get_args[0], int(get_args[1]))
            except:
                pass
    elif type(get_args) == str:
        print(get_args)
    else:
        print("默认参数：进程：MAA.exe 等待时间：300")
        while True:
            try:
                foo()
            except:
                pass

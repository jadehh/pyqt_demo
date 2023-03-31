#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File     : packing_app.py.py
# @Author   : jade
# @Date     : 2023/3/31 14:14
# @Email    : jadehh@1ive.com
# @Software : Samples
# @Desc     :
from jade import *
if __name__ == '__main__':
    import argparse
    lib_path = ""
    if getOperationSystem() == "Windows":
        lib_path = "pyqt_demo_lib32"
    elif getOperationSystem() == "Darwin":
        lib_path = ""
    else:
        lib_path = "pyqt_demo_lib64"
    parser = argparse.ArgumentParser()
    if getOperationSystem() == "Windows":
        parser.add_argument('--extra_sys_list', type=str,
                            default="")  ## 需要额外打包的路径
        parser.add_argument('--scripts_path', type=str,
                            default="")  ## 打包成一个完成的包
        parser.add_argument('--full', type=str,
                            default="False")  ## 打包成一个完成的包
        parser.add_argument('--extra_path_list', type=list,
                            default=[("lib/Windows/", "./")])
    else:
        parser.add_argument('--extra_sys_str', type=str,
                            default=[])  ## sys.path.append需要额外打包的路径
        parser.add_argument('--remove_import_list', type=list,
                            default=[])
        if getOperationSystem() == "Linux":
            parser.add_argument('--full', type=str,
                                default="True")  ## 打包成一个完成的包
        else:
            parser.add_argument('--full', type=str,
                                default="False")  ## 打包成一个完成的包
        parser.add_argument('--extra_path_list', type=list,
                            default=[])
    parser.add_argument('--lib_path', type=str, default=lib_path)  ## 是否lib包分开打包
    if getOperationSystem() == "Darwin":
        parser.add_argument("--head_str", type=str, default="")
    else:
        parser.add_argument("--head_str", type=str, default="from jade import *\n"
                                                        "update_lib('/tmp/{}')\n".format(lib_path))
    parser.add_argument('--use_jade_log', type=str,
                        default="True")  ##是否使用JadeLog

    parser.add_argument('--console', type=str,
                        default="False")  ## 是否显示命令行窗口,只针对与Windows有效
    parser.add_argument("--app_version", type=str, default=get_app_version())  ## 版本号
    parser.add_argument('--app_name', type=str,
                        default="PyQtDemo")  ##需要打包的文件名称
    parser.add_argument('--name', type=str,
                        default="pyqt_demo")  ##需要打包的文件名称
    parser.add_argument('--appimage', type=str,
                        default="True")  ## 是否打包成AppImage
    parser.add_argument('--is_auto_packing',type=str,default="False") ##是否自动打包
    parser.add_argument('--is_qt', type=str, default="False")  ## qt 会将controller view src 都进行编译
    parser.add_argument('--specify_files', type=str, default="")  ## 指定编译的文件
    args = parser.parse_args()
    writeSpec(args)
    # build(args)
    # packAPP(args)


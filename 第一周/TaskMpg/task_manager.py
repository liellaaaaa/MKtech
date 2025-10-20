#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
任务清单小助手 - Python入门项目
主程序文件
"""

import os
import time
from task_operations import *
from data_handler import *


def display_menu():
    """显示菜单选项"""
    print("\n=== 任务清单小助手 ===")
    print("1. 添加任务")
    print("2. 查看任务")
    print("3. 删除任务")
    print("4. 完成/取消完成任务")
    print("5. 搜索任务")
    print("6. 退出")
    print("=====================")


def main():
    """主函数"""
    # 加载保存的任务
    tasks = load_tasks()
    print(f"已加载 {len(tasks)} 个任务")
    
    while True:
        display_menu()
        
        try:
            choice = input("请输入您的选择 (1-6): ")
            
            if choice == '1':
                # 添加任务
                task_content = input("请输入任务内容: ")
                priority_input = input("请输入优先级 (高/中/低，默认为中): ").strip()
                # 如果用户直接按回车，使用默认值
                if not priority_input:
                    priority = "中"
                # 检查输入是否为有效优先级
                elif priority_input in ["高", "中", "低"]:
                    priority = priority_input
                else:
                    print("❌ 无效的优先级，请输入'高'、'中'或'低'")
                    continue    
                add_task(tasks, task_content, priority)
                save_tasks(tasks)  # 自动保存
                print("✅ 任务添加成功！")
                
            elif choice == '2':
                # 查看任务
                display_tasks(tasks)
                
            elif choice == '3':
                # 删除任务
                display_tasks(tasks)
                if tasks:
                    task_id = int(input("请输入要删除的任务编号: "))
                    if delete_task(tasks, task_id):
                        save_tasks(tasks)  # 自动保存
                        print("✅ 任务删除成功！")
                    else:
                        print("❌ 任务编号不存在！")
                
            elif choice == '4':
                # 完成/取消完成任务
                display_tasks(tasks)
                if tasks:
                    task_id = int(input("请输入要标记的任务编号: "))
                    if toggle_task_status(tasks, task_id):
                        save_tasks(tasks)  # 自动保存
                        print("✅ 任务状态已更新！")
                    else:
                        print("❌ 任务编号不存在！")
                
            elif choice == '5':
                # 搜索任务
                keyword = input("请输入搜索关键词: ")
                search_tasks(tasks, keyword)
                
            elif choice == '6':
                # 退出程序
                save_tasks(tasks)
                print("已保存，谢谢使用！")
                break
                
            else:
                print("❌ 请输入有效的选项！")
                
        except ValueError:
            print("❌ 请输入有效的数字！")
        except Exception as e:
            print(f"❌ 发生错误: {e}")
        
        # 等待用户确认，增强交互体验
        input("\n按回车键继续...")


if __name__ == "__main__":
    print("欢迎使用任务清单小助手！")
    main()
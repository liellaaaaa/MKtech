#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
数据处理模块
负责任务数据的保存和加载
"""

import json
import os

# 任务文件路径
TASKS_FILE = "tasks.txt"

def load_tasks():
    """
    从文件加载任务列表
    
    Returns:
        list: 任务列表
    """
    try:
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r', encoding='utf-8') as file:
                # 尝试读取并解析JSON数据
                try:
                    tasks = json.load(file)
                    # 确保返回的是列表类型
                    if isinstance(tasks, list):
                        return tasks
                    else:
                        return []
                except json.JSONDecodeError:
                    # 如果文件格式错误，返回空列表
                    print(f"⚠️  {TASKS_FILE} 文件格式错误，将创建新文件")
                    return []
        else:
            # 文件不存在，返回空列表
            return []
    except Exception as e:
        print(f"⚠️  加载任务时出错: {e}")
        return []

def save_tasks(tasks):
    """
    保存任务列表到文件
    
    Args:
        tasks (list): 任务列表
    """
    try:
        with open(TASKS_FILE, 'w', encoding='utf-8') as file:
            # 使用json.dump保存任务数据，确保中文正常显示
            json.dump(tasks, file, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"❌ 保存任务时出错: {e}")
        return False
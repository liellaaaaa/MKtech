#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
任务操作模块
包含任务的增删改查等核心功能
"""
import time


def add_task(tasks, content, priority="中"):
    """
    添加新任务
    
    Args:
        tasks (list): 任务列表
        content (str): 任务内容
        priority (str): 任务优先级（高/中/低）
    """
    # 创建任务字典，包含内容、状态、优先级和添加时间
    task = {
        "content": content,
        "status": "未完成",  # 初始状态为未完成
        "priority": priority,
        "created_time": time.strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(task)


def delete_task(tasks, task_id):
    """
    删除指定任务
    
    Args:
        tasks (list): 任务列表
        task_id (int): 任务编号（从1开始）
    
    Returns:
        bool: 删除是否成功
    """
    # 检查任务编号是否有效
    if 1 <= task_id <= len(tasks):
        del tasks[task_id - 1]  # 索引从0开始，所以减1
        return True
    return False

def display_tasks(tasks):
    """
    显示所有任务
    
    Args:
        tasks (list): 任务列表
    """
    if not tasks:
        print("\n📝 暂无任务")
        return
    
    print("\n📝 任务列表:")
    print("-" * 80)
    print(f"{'编号':<5}{'状态':<8}{'优先级':<8}{'创建时间':<20}{'内容':<30}")
    print("-" * 80)
    
    for i, task in enumerate(tasks, 1):
        # 为已完成任务添加标记
        status_display = "✅ 已完成" if task["status"] == "已完成" else "⬜ 未完成"
        
        # 优先级颜色标记
        priority_display = task["priority"]
        if priority_display == "高":
            priority_display = "🔴 高"
        elif priority_display == "中":
            priority_display = "🟡 中"
        else:
            priority_display = "🟢 低"
        
        # 输出任务信息
        print(f"{i:<5}{status_display:<8}{priority_display:<8}{task['created_time']:<20}{task['content']:<30}")
    print("-" * 80)

def toggle_task_status(tasks, task_id):
    """
    切换任务状态（未完成/已完成）
    
    Args:
        tasks (list): 任务列表
        task_id (int): 任务编号（从1开始）
    
    Returns:
        bool: 状态切换是否成功
    """
    if 1 <= task_id <= len(tasks):
        task = tasks[task_id - 1]
        # 切换状态
        task["status"] = "已完成" if task["status"] == "未完成" else "未完成"
        return True
    return False

def search_tasks(tasks, keyword):
    """
    搜索任务
    
    Args:
        tasks (list): 任务列表
        keyword (str): 搜索关键词
    """
    if not keyword:
        display_tasks(tasks)
        return
    
    # 搜索包含关键词的任务
    results = []
    for i, task in enumerate(tasks, 1):
        if keyword.lower() in task["content"].lower() or \
           keyword.lower() in task["priority"].lower() or \
           keyword.lower() in task["status"].lower():
            results.append((i, task))
    
    if not results:
        print(f"\n🔍 未找到包含 '{keyword}' 的任务")
        return
    
    print(f"\n🔍 搜索结果（包含 '{keyword}'）:")
    print("-" * 80)
    print(f"{'编号':<5}{'状态':<8}{'优先级':<8}{'创建时间':<20}{'内容':<30}")
    print("-" * 80)
    
    for i, task in results:
        status_display = "✅ 已完成" if task["status"] == "已完成" else "⬜ 未完成"
        
        priority_display = task["priority"]
        if priority_display == "高":
            priority_display = "🔴 高"
        elif priority_display == "中":
            priority_display = "🟡 中"
        else:
            priority_display = "🟢 低"
        
        print(f"{i:<5}{status_display:<8}{priority_display:<8}{task['created_time']:<20}{task['content']:<30}")
    print("-" * 80)
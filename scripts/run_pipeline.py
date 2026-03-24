import os
import sys

# 将项目根目录加入环境变量，确保模块可导入
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core_engine.cross_referencer import ClawComparator
from onchain_execution.tx_builder import TerminalExecutionEngine

def generate_mock_data():
    """生成用于测试的本地离线表单数据"""
    data_dir = "data_vault/raw_inputs"
    os.makedirs(data_dir, exist_ok=True)
    file_path = os.path.join(data_dir, "batch_tasks_001.csv")
    
    with open(file_path, "w") as f:
        f.write("target_address,amount\n")
        f.write("0x1234567890abcdef1234567890abcdef12345678,50\n")
        f.write("0xbad0000000000000000000000000000000000000,100\n") # 将被拦截的地址
        f.write("0xabcdef1234567890abcdef1234567890abcdef12,20\n")
        f.write("0x9999999999999999999999999999999999999999,-5\n")  # 将被拦截的金额
    return file_path

if __name__ == "__main__":
    print(">>> 启动 Nexus-Recon 自动化管线 <<<\n")
    
    # 1. 准备本地数据
    csv_file = generate_mock_data()
    
    # 2. 初始化核心引擎
    comparator = ClawComparator()
    execution_engine = TerminalExecutionEngine()
    
    # 3. 执行交叉比对与自动过滤
    ready_queue, anomalies = comparator.process_batch(csv_file)
    
    # 4. 打印异常拦截日志
    if anomalies:
        print("\n[Audit] 发现异常数据，已自动拦截:")
        for log in anomalies:
            print(f"  - 拦截地址: {log['address'][:8]}... | 原因: {log['reason']}")
            
    # 5. 硬核执行放行数据
    execution_engine.execute_batch(ready_queue)

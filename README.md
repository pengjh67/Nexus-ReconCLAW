# Nexus-Recon (枢纽核对者)
**基于 OKX Onchain OS 的链下链上自动化对账与硬核执行网关**

## 1. 项目简介
针对 Web3 机构在批量资金交互（如财库分发、结算）时面临的“链下复杂表单与链上实时状态核对困难”的痛点，Nexus-Recon 提供了一套主权级的 Agent 自动化解决方案。
本系统运行于本地 Windows 节点，通过提取本地 Excel/CSV 业务数据，利用 OpenClaw 模型调用 Onchain OS 接口进行自动化交叉核对与风险仲裁，最终输出并执行硬核链上指令，拒绝纯文本补全的“伪执行”。

## 2. 核心架构
* **Local Vault (本地安全数据引擎):** 基于 Pandas 处理本地多维财务表单，执行数据清洗。
* **Claw-Comparator (AI 交叉仲裁器):** 读取清洗数据，比对链上实时状态（余额、合约安全评分），由 AI 裁决是否放行。
* **Terminal Execution Engine:** 过滤掉异常数据后，对 Ready_To_Execute 队列自动构建交易 Payload 并在 Onchain OS 上执行。

## 3. 快速复现 (Quick Start)
环境要求：Windows 10/11, Python 3.10+

```bash
# 1. 克隆仓库
git clone [https://github.com/hkai614119-star/nexus-recon.git](https://github.com/hkai614119-star/nexus-recon.git)
cd nexus-recon

# 2. 安装依赖
pip install -r requirements.txt

# 3. 运行主干测试管线
python scripts/run_pipeline.py

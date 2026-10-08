# -*- coding: utf-8 -*-
# FASTA程序功能与BLAST工具分类（ch03 p53）
# 来源：陈铭《生物信息学》第三版 自学示例
# 依赖安装：
#   Python 3.8+；无需额外依赖（仅标准库）。可选：pip install biopython 用于真实序列搜索。

# FASTA 家族程序功能对照表
FASTA_PROGRAMS = {
    "FASTA":    "DNA vs DNA 或 protein vs protein 库搜索",
    "FASTX/Y":  "DNA 正向翻译成 3 种蛋白后搜索蛋白库",
    "FASTF":    "混合无序多肽片段搜索蛋白库",
    "FASTS":    "有序多肽片段搜索蛋白库",
    "TFASTX/Y": "DNA 库每条序列翻译成 6 种蛋白后与查询蛋白比较",
}

def show_programs():
    # 打印程序功能对照表
    print(f"{'程序':<10}{'功能'}")
    print("-" * 60)
    for name, desc in FASTA_PROGRAMS.items():
        print(f"{name:<10}{desc}")

def typical_commands():
    # 典型命令行调用示例
    cmds = [
        "fasta query.fa db.fa",
        "fastx query_dna.fa protein_db.fa",
        "tfastx query_protein.fa dna_db.fa",
    ]
    print("\n典型命令行调用：")
    for c in cmds:
        print("  " + c)

if __name__ == "__main__":
    show_programs()
    typical_commands()
    print("\n说明：随数据量增长，FASTA 速度不足，逐渐被 BLAST 取代。")


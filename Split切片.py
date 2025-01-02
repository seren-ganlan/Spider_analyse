import pandas as pd
import openpyxl
# 读取 Excel 文件
file_path = r'C:\Users\Administrator\PycharmProjects\pythonProject\Item\Blog\Website_Information.xlsx'
df = pd.read_excel(file_path)

# 假设包含 URL 的列名为 'url'
def extract_domain(URL):
    try:
        # 切分 URL 获取域名
        parts = URL.split("//")
        if len(parts) > 1:
            domain = parts[1].split("/")[0]
            return domain
        return None
    except Exception as e:
        return None

# 创建新的一列存储域名
df['Domain'] = df['URL'].apply(extract_domain)

# 去重：根据域名列保留第一个出现的行
df_unique = df.drop_duplicates(subset='Domain', keep='first')


# 保存结果到新的 Excel 文件
output_file_path = 'Domain.xlsx'  # 替换为输出文件路径
df_unique.to_excel(output_file_path, index=False)

print(f"处理完成，结果已保存到 {output_file_path}")

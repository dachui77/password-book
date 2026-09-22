#!/usr/bin/env python3
"""
密码本项目日报发送脚本
用法: python3 send_report.py [项目路径]
"""

import smtplib
import sys
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# 收件人列表
RECIPIENTS = [
    'dacuiw448@gmail.com',
    'liushu@163.com'
]

def send_email(subject, body, project_path='.'):
    """发送邮件报告"""
    
    # 获取发件人信息（需要从环境变量或配置获取）
    # Gmail SMTP
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    
    # 检查是否有邮箱配置
    sender_email = os.getenv('EMAIL_SENDER')
    sender_password = os.getenv('EMAIL_PASSWORD')
    
    if not sender_email or not sender_password:
        print("错误: 请设置环境变量 EMAIL_SENDER 和 EMAIL_PASSWORD")
        print("示例:")
        print("  export EMAIL_SENDER='your_email@gmail.com'")
        print("  export EMAIL_PASSWORD='your_app_password'")
        return False
    
    # 创建邮件
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(RECIPIENTS)
    msg['Subject'] = f'[密码本日报] {subject} - {datetime.now().strftime("%Y-%m-%d")}'
    
    # 邮件正文
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    report_body = f"""密码本项目工作日报

发送时间: {timestamp}

{body}

---
此邮件由 Password Book 项目自动生成
"""
    msg.attach(MIMEText(report_body, 'plain', 'utf-8'))
    
    # 附加项目摘要文件（如果存在）
    summary_file = os.path.join(project_path, 'WORK_LOG.md')
    if os.path.exists(summary_file):
        with open(summary_file, 'r', encoding='utf-8') as f:
            attachment = MIMEText(f.read(), 'plain', 'utf-8')
            attachment.add_header('Content-Disposition', 'attachment', filename='WORK_LOG.md')
            msg.attach(attachment)
    
    # 发送邮件
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, RECIPIENTS, msg.as_string())
        server.quit()
        print(f"✓ 邮件已发送至: {', '.join(RECIPIENTS)}")
        return True
    except Exception as e:
        print(f"✗ 邮件发送失败: {e}")
        return False

if __name__ == '__main__':
    project_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    subject = sys.argv[2] if len(sys.argv) > 2 else '项目开发日志'
    
    # 读取工作日志作为内容
    work_log = os.path.join(project_path, 'WORK_LOG.md')
    if os.path.exists(work_log):
        with open(work_log, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = '今日无工作记录'
    
    send_email(subject, content, project_path)

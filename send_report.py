#!/usr/bin/env python3
"""密码本项目日报发送脚本"""
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

RECIPIENTS = ['dacuiw448@gmail.com', 'liushu@163.com']

def load_config():
    """从 .env 文件加载配置"""
    config = {}
    env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    if os.path.exists(env_file):
        with open(env_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    if '=' in line:
                        key, val = line.split('=', 1)
                        config[key.strip()] = val.strip()
    # 也支持环境变量
    config.setdefault('EMAIL_SENDER', os.getenv('EMAIL_SENDER', ''))
    config.setdefault('EMAIL_PASSWORD', os.getenv('EMAIL_PASSWORD', ''))
    return config

def send_email(subject, body, project_path='.'):
    config = load_config()
    sender = config.get('EMAIL_SENDER')
    password = config.get('EMAIL_PASSWORD')
    
    if not sender or not password:
        print("错误: 请检查 .env 文件中的 EMAIL_SENDER 和 EMAIL_PASSWORD")
        return False
    
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ', '.join(RECIPIENTS)
    msg['Subject'] = f'[Password Book日报] {subject} - {datetime.now().strftime("%Y-%m-%d")}'
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    report_body = f"""密码本项目工作日报

发送时间: {timestamp}

{body}

---
此邮件由 Password Book 项目自动生成
"""
    msg.attach(MIMEText(report_body, 'plain', 'utf-8'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, RECIPIENTS, msg.as_string())
        server.quit()
        print(f"✓ 邮件已发送至: {', '.join(RECIPIENTS)}")
        return True
    except Exception as e:
        print(f"✗ 邮件发送失败: {e}")
        return False

if __name__ == '__main__':
    project_path = sys.argv[1] if len(sys.argv) > 1 else '.'
    subject = sys.argv[2] if len(sys.argv) > 2 else '工作日报'
    
    work_log = os.path.join(project_path, 'WORK_LOG.md')
    if os.path.exists(work_log):
        with open(work_log, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = '今日无工作记录'
    
    send_email(subject, content, project_path)

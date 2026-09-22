#!/bin/bash
# 自动生成日报并发送邮件
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$PROJECT_DIR/WORK_LOG.md"
DATE=$(date '+%Y-%m-%d')
TIME=$(date '+%H:%M:%S')

# 更新工作日志
cat >> "$LOG_FILE" << HEADER

---
## 今日工作记录 ($DATE)

**工作时间**: $TIME
**完成事项**:
- 续接上日工作，推进项目进度

**下一步计划**:
- 根据项目待办事项继续开发

---
*自动记录时间: $DATE $TIME*
HEADER

# 检查环境变量
if [ -f "$HOME/.password_book_env" ]; then
    source "$HOME/.password_book_env"
    
    if [ -n "$EMAIL_SENDER" ] && [ -n "$EMAIL_PASSWORD" ]; then
        python3 "$PROJECT_DIR/send_report.py" "$PROJECT_DIR" "工作日报 $DATE"
    else
        echo "警告: 邮箱配置不完整，请运行 setup_email.sh"
    fi
else
    echo "警告: 未找到邮箱配置，请运行 ./setup_email.sh"
fi

echo "日报已生成: $LOG_FILE"

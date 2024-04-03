#coding=utf-8
import sys
sys.path.append('/Users/ph/Library/Python/3.6/lib/python/site-packages')
sys.path.append('Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages')
import xlrd
import logging,os
import yagmail

class Helper(object):

    def read_excles(self,rowx):
        book=xlrd.open_workbook('../data/info.xlsx','r')
        table=book.sheet_by_index(0)
        return table.row_values(rowx)

    def read_loginname(self,rowx):
        return str(self.read_excles(rowx)[0])

    def read_password(self,rowx):
        return str(self.read_excles(rowx)[1])

    def read_text(self,rowx):
        return str(self.read_excles(rowx)[1])

    def dirname(self,filename,filepath='data'):
        return os.path.join(os.path.dirname(__file__),filepath,filename) #os.path.dirname(__file__))会报格式错误

    def log(self,log_content):
        logFile=logging.FileHandler('../log/log.txt','a',encoding='utf-8')
        fmt=logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
        logFile.setFormatter(fmt)
        logger1=logging.Logger('logTest',level=logging.DEBUG)
        logger1.addHandler(logFile)
        logger1.info(log_content)
        logFile.close()

    def send_mail(self,filename):
        mail = yagmail.SMTP(user='1622480955@qq.com', password='bzqrasymomjkdejg', host='smtp.qq.com')
        contents = ['测试结果']
        # 接收者，主题名称、发送内容、附件（没有不写）
        mail.send(['1622480955@qq.com', 'peng.hui@cesgroup.com.cn'], '邮件名称', contents, [filename])


# logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
# logger=logging.getLogger(__name__)
# logger.info('开始输出logging日志')
# logger.debug('显示debug级别的日志信息')
# logger.warning("显示wanrning级别的日志")
# logger.info('结束输出logging日志')
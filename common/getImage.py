#coding=utf-8
import os,time



def SaveImage(driver,errorImage):
    # Rawpath=os.path.join(os.path.dirname(__file__)),'Image')
    Rawpath='../picture'
    newPicture=Rawpath+'/'+time.strftime('%Y_%m_%d_%H:%M:%S')+" "+errorImage
    driver.get_screenshot_as_file(newPicture) #截图保存在指定的路径




# Hello World project 
# python3
#ماژول پایتون برای ردیابی و تشخیص
# FIRST ֲ®  اشیاء بینایی کامپیوتری عمدتاً برای برنامه مسابقه رباتیک
#python -m pip install ovl[cv]
#For the full installation of all features use: python -m pip install ovl[full]
#For the frc related features use the frc option: python -m pip install ovl[frc]
print ()

import ovl

target_filters = [ovl.percent_area_filter(min_area=0.005),
                  ovl.circle_filter(min_area_ratio=0.7),
                  ovl.area_sort()]

threshold = ovl.Color([20, 100, 100], [55, 255, 255])

yellow_circle = ovl.Vision(threshold=threshold,
                           target_filters=target_filters,
                           camera=0,  # open the first connected camera
                           image_filters=[ovl.gaussian_blur()])

while True:
    image = yellow_circle.get_image()
    targets, filtered_image = yellow_circle.detect(image)
    directions = yellow_circle.get_directions(targets, filtered_image)

    print(directions)  # prints out the (x, y) coordinates of the largest target

# مبنع پروزه https://pypi.org/project/ovl/
#Ovl از خطوط لوله بینایی کامپیوتری پیچیده و در عین حال مدولار پشتیبانی می کند
#که ایجاد و تغییر آن آسان است.
#ایجاد و راه اندازی آسان برای مبتدیان و انعطاف پذیر برای حرفه ای ها
#این کتابخانه از نحو ساده و در عین حال بسیار قابل تنظیم برای ایجاد خط لوله چشم
#چشم اندازبااستفاده از شی (vision)استفاده میکند
#خط لوله ای که دایره زرد راتشخیص میدهد

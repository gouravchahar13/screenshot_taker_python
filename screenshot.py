import pyscreenshot as img_sc
import schedule
import time,random as rd

def takescreen():
    print("taking screenshot")
    image_name=f"screenshot-{rd.randint(1,100)}"
    screenshot=img_sc.grab()
    filepath=f"{image_name}.png"
    screenshot.save(filepath)
    print("screenshot taken")
    return filepath

def main():
    schedule.every(10).seconds.do(takescreen)
    while True:
        schedule.run_pending()
        time.sleep(10)

#clear
if __name__=="__main__":
    main()
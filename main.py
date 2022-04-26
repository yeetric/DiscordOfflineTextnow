import pytextnow #textnow module
import pyautogui #computer commands
import time

# open https://electron.textnow.com/messaging
# open your discord link
# start on discord

def moveAndClick(x,y):
    pyautogui.moveTo(x,y)
    pyautogui.click()

def switch_tabs():
    with pyautogui.hold("ctrl"):
        pyautogui.press(['tab'])

def screenshot():
    with pyautogui.hold("win"):
        pyautogui.press(['prtscr'])

def paste():
    pyautogui.hotkey('ctrl', 'v')


client = pytextnow.Client("yeetricstorage",
                          sid_cookie="s%3ACPyraqk8YbdKDhLNjMThwSwPSVtpdEsb.TGedwHmjcZ82uFARzF5fiXhJ6ohDMWWOVw0Uq27JXgI",
                          csrf_cookie="s%3AIUtsySojIO94oiFnIho3Ee0n.OJJ%2F5y4fnrF3vxvVVh9y8Toz57NGPbcMd7iKNTXgIaw")

while True:
    try:
        new_messages = client.get_unread_messages()

        for message in new_messages:
            message.mark_as_read()
            print(message.number)
            print(message.content)
            x = message.content

            if "discord-" in message.content:
                print("discord detected")
                x = x.replace("discord-", "")
                moveAndClick(650, 1000)
                pyautogui.typewrite(x) # type the message
                pyautogui.press('enter') # press enter
                client.send_sms("5102880541", "Message sent")

            if "update-" in message.content:
                print("update detected")
                screenshot()
                switch_tabs()
                moveAndClick(650, 1000)
                paste()
                time.sleep(1)
                moveAndClick(968,727) #clicks send
                time.sleep(1)
                switch_tabs()
                moveAndClick(650, 1000)
    except:
        print("idk smth went wrong")

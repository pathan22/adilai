import pywhatkit

def send_message():

    number = input("918639943613: ")

    message = input("send msg: ")

    hour = int(input("hour"))
    minute = int(input(" minute"))

    pywhatkit.sendwhatmsg(
        number,
        message,
        hour,
        minute
    )

    print("Message scheduled 😄")
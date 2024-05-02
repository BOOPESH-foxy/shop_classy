# import smtplib
# from email.message import EmailMessage
# import data
# import socket 


# def mail_gen():

#         Message = EmailMessage()

#         Message["subject"] = "Your cart !"
#         Message["From"] = data.from_mail
#         Message["To"] = input("Enter valid mail address for cart bill : ")
#         # Message["To"] = data.to_mail
#         Message.set_content("Cart id:%s\nPurcahsed item code:%s \nQuantity:%s \nBill:%s"%(table_data[0][0],table_data[0][1], table_data[0][2],table_data[0][3]
#                                                                                        ))

#         # to establish secure connection
#         server = smtplib.SMTP_SSL("smtp.gmail.com",465)
#         server.login(data.from_mail,data.app_password)

#         server.send_message(Message)
#         print("Mail sent and server has been closed !")
#         server.quit()
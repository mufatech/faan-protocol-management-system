# import yagmail


# event_name = "Dawah Youth Camp 2025"
# event_date = "24th - 28th December 2025"
# location = "Towab Private Schools, Ijegun'25"
# # whatsapplink = "Follow this link to join Delegates group: https://chat.whatsapp.com/DBdjiShxtdN9u71hNP6lB5"
# subject = "Registration Confirmation"


# port = 465

# # sender = "fabosedesidiqat@gmail.com"
#sender = "nasfatlagosyouthzone2@gmail.com"



# def send_confirmation_email(name, email, number, branch, category):
#     msg = """\
#     Hello {0},
#     As-salam Alaykun Waramotuh laha wabarakatuh
#     Welcome To Nasfat Youth Wing Lagos zone 2 {1}

#     Event Details:
#     - Date: {2}
#     - Location: {3}
#     - Number: {4}
#     - Branch: {5}
#     - Category: {6}


#     We hope you will learn, unlearn and relearn.

#     Regards
#     The Committee

    
#     """.format(name, event_name, event_date, location, number, branch, category)  #whatsapplink
#     try:
#         yag = yagmail.SMTP(sender, password)
#         yag.send(email, subject, msg)
#         print("mail successfully sent")
        
#     except:
#         print("email not sending")
# #send_confirmation_email("Bose", "fabosedesidiqat@gmail.com")

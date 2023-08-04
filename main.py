import tkinter

window=tkinter.Tk()

window.title("You Dahee")
window.geometry("1024x768+100+100")
window.resizable(False, False)

# os체크 함수
def check():
    os_type_label.config(text= "os type = " + os_type_radio.get() + "\n")
    global os_type
    os_type = os_type_radio.get()

# 버튼 함수
def showResult():
    appName=appNameText.get()
    appSite=appSiteText.get()
    siteDomain=siteDomainText.get()
    appId=appIdText.get()
    appVersion=appVersionText.get()
    onesignalPushId=onesignalPushIdText.get()
    if(os_type == "android"):
        appVersionCode=appVersionCodeText.get()
        androidKeystorePath=androidKeystorePathText.get()
        androidKeystorePassword=androidKeystorePasswordText.get()
        androidAlias=androidAliasText.get()
        androidAliasPassword=androidAliasPasswordText.get()
    result.config(text=os_type+appName+appSite+siteDomain+appId+appVersion+onesignalPushId+appVersionCode+androidKeystorePath+androidKeystorePassword+androidAlias+androidAliasPassword)


os_type_radio=tkinter.StringVar()

radio1=tkinter.Radiobutton(window, text="Android", value="android", variable=os_type_radio, command=check)
radio1.pack()

radio2=tkinter.Radiobutton(window, text="iOS", value="ios", variable=os_type_radio, command=check)
radio2.pack()

os_type_label=tkinter.Label(window, text="None", height=5)
os_type_label.pack()

# appName 입력창
appNameLabel=tkinter.Label(window, text="\nappName")
appNameLabel.pack()
appNameText=tkinter.Entry(window)
appNameText.bind("<Return>")
appNameText.pack()

# appSite 입력창
appSiteLabel=tkinter.Label(window, text="\nappSite")
appSiteLabel.pack()
appSiteText=tkinter.Entry(window)
appSiteText.bind("<Return>")
appSiteText.pack()

# siteDomain 입력창
siteDomainLabel=tkinter.Label(window, text="\nsiteDomain")
siteDomainLabel.pack()
siteDomainText=tkinter.Entry(window)
siteDomainText.bind("<Return>")
siteDomainText.pack()

# appId 입력창
appIdLabel=tkinter.Label(window, text="\nappId")
appIdLabel.pack()
appIdText=tkinter.Entry(window)
appIdText.bind("<Return>")
appIdText.pack()

# appVersion 입력창
appVersionLabel=tkinter.Label(window, text="\nappVersion")
appVersionLabel.pack()
appVersionText=tkinter.Entry(window)
appVersionText.bind("<Return>")
appVersionText.pack()

# onesignalPushId 입력창
onesignalPushIdLabel=tkinter.Label(window, text="\nonesignalPushId")
onesignalPushIdLabel.pack()
onesignalPushIdText=tkinter.Entry(window)
onesignalPushIdText.bind("<Return>")
onesignalPushIdText.pack()


androidOnlyLabel=tkinter.Label(window, text="\n\n여기부터는 안드로이드 빌드할 때만 입력해주시기 바랍니다.")
androidOnlyLabel.pack()


# appVersionCode 입력창
appVersionCodeLabel=tkinter.Label(window, text="\nappVersionCode")
appVersionCodeLabel.pack()
appVersionCodeText=tkinter.Entry(window)
appVersionCodeText.bind("<Return>")
appVersionCodeText.pack()

# androidKeystorePath 입력창
androidKeystorePathLabel=tkinter.Label(window, text="\nandroidKeystorePath")
androidKeystorePathLabel.pack()
androidKeystorePathText=tkinter.Entry(window)
androidKeystorePathText.bind("<Return>")
androidKeystorePathText.pack()

# androidKeystorePassword 입력창
androidKeystorePasswordLabel=tkinter.Label(window, text="\nandroidKeystorePassword")
androidKeystorePasswordLabel.pack()
androidKeystorePasswordText=tkinter.Entry(window)
androidKeystorePasswordText.bind("<Return>")
androidKeystorePasswordText.pack()

# androidAlias 입력창
androidAliasLabel=tkinter.Label(window, text="\nandroidAlias")
androidAliasLabel.pack()
androidAliasText=tkinter.Entry(window)
androidAliasText.bind("<Return>")
androidAliasText.pack()

# androidAliasPassword 입력창
androidAliasPasswordLabel=tkinter.Label(window, text="\nandroidAliasPassword")
androidAliasPasswordLabel.pack()
androidAliasPasswordText=tkinter.Entry(window)
androidAliasPasswordText.bind("<Return>")
androidAliasPasswordText.pack()


result=tkinter.Label(window)
result.pack()

button = tkinter.Button(window, text="앱 정보 변경", overrelief="solid", width=15, command=showResult, repeatdelay=1000, repeatinterval=100)
button.pack()



window.mainloop()
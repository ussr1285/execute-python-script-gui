import tkinter
import test

window=tkinter.Tk()

window.title("Make cordova app")
window.geometry("1024x768+100+100")
window.resizable(True, True)

# os체크 함수
def check():
    os_type_label.config(text= "os type = " + os_type_radio.get() + "")
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

    androidInfoArr = []
    if(os_type == "android"):
        appVersionCode=appVersionCodeText.get()
        androidKeystorePath=androidKeystorePathText.get()
        androidKeystorePassword=androidKeystorePasswordText.get()
        androidAlias=androidAliasText.get()
        androidAliasPassword=androidAliasPasswordText.get()
        androidInfoArr = [appVersionCode, androidKeystorePath, androidKeystorePassword, androidAlias, androidAliasPassword]
    test.funca(os_type, appName, appSite, siteDomain, appId, appVersion, onesignalPushId, androidInfoArr) # 여기서 인자 담아서 다른 소스코드 함수 실행.
    result.config(text=os_type+appName+appSite+siteDomain+appId+appVersion+onesignalPushId+str(androidInfoArr))


os_type_radio=tkinter.StringVar()

radio1=tkinter.Radiobutton(window, text="Android", value="android", variable=os_type_radio, command=check)
radio1.pack()

radio2=tkinter.Radiobutton(window, text="iOS", value="ios", variable=os_type_radio, command=check)
radio2.pack()

os_type_label=tkinter.Label(window, text="None", height=5)
os_type_label.pack()

# appName 입력창
appNameLabel=tkinter.Label(window, text="app Name")
appNameLabel.pack()
appNameText=tkinter.Entry(window)
appNameText.bind("<Return>")
appNameText.pack()

# appSite 입력창
appSiteLabel=tkinter.Label(window, text="appSite")
appSiteLabel.pack()
appSiteText=tkinter.Entry(window)
appSiteText.bind("<Return>")
appSiteText.pack()

# siteDomain 입력창
siteDomainLabel=tkinter.Label(window, text="siteDomain")
siteDomainLabel.pack()
siteDomainText=tkinter.Entry(window)
siteDomainText.bind("<Return>")
siteDomainText.pack()

# appId 입력창
appIdLabel=tkinter.Label(window, text="appId")
appIdLabel.pack()
appIdText=tkinter.Entry(window)
appIdText.bind("<Return>")
appIdText.pack()

# appVersion 입력창
appVersionLabel=tkinter.Label(window, text="appVersion")
appVersionLabel.pack()
appVersionText=tkinter.Entry(window)
appVersionText.bind("<Return>")
appVersionText.pack()

# onesignalPushId 입력창
onesignalPushIdLabel=tkinter.Label(window, text="onesignalPushId")
onesignalPushIdLabel.pack()
onesignalPushIdText=tkinter.Entry(window)
onesignalPushIdText.bind("<Return>")
onesignalPushIdText.pack()

androidOnlyLabel=tkinter.Label(window, text="\n\n여기부터는 안드로이드 빌드할 때만 입력해주시기 바랍니다.\n")
androidOnlyLabel.pack()

# appVersionCode 입력창
appVersionCodeLabel=tkinter.Label(window, text="appVersionCode")
appVersionCodeLabel.pack()
appVersionCodeText=tkinter.Entry(window)
appVersionCodeText.bind("<Return>")
appVersionCodeText.pack()

# androidKeystorePath 입력창
androidKeystorePathLabel=tkinter.Label(window, text="androidKeystorePath")
androidKeystorePathLabel.pack()
androidKeystorePathText=tkinter.Entry(window)
androidKeystorePathText.bind("<Return>")
androidKeystorePathText.pack()

# androidKeystorePassword 입력창
androidKeystorePasswordLabel=tkinter.Label(window, text="androidKeystorePassword")
androidKeystorePasswordLabel.pack()
androidKeystorePasswordText=tkinter.Entry(window)
androidKeystorePasswordText.bind("<Return>")
androidKeystorePasswordText.pack()

# androidAlias 입력창
androidAliasLabel=tkinter.Label(window, text="androidAlias")
androidAliasLabel.pack()
androidAliasText=tkinter.Entry(window)
androidAliasText.bind("<Return>")
androidAliasText.pack()

# androidAliasPassword 입력창
androidAliasPasswordLabel=tkinter.Label(window, text="androidAliasPassword")
androidAliasPasswordLabel.pack()
androidAliasPasswordText=tkinter.Entry(window)
androidAliasPasswordText.bind("<Return>")
androidAliasPasswordText.pack()


result=tkinter.Label(window)
result.pack()

button = tkinter.Button(window, text="앱 정보 변경", overrelief="solid", width=15, command=showResult, repeatdelay=1000, repeatinterval=100)
button.pack()



window.mainloop()
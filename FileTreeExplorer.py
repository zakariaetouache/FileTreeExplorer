import os

esp = 0
chemin = "C:/"


def detChemin():
    global esp
    global chemin
    lstChemin.append(lstC[0]+"/")
    while not os.path.exists("".join(lstChemin)):
        del lstChemin[len(lstChemin)-2]
        esp -= 1
    chemin = "".join(lstChemin)
    del lstC[0]


with open("imageOrd.txt", "w") as f:
    lstC = os.listdir("C:/")
    tmpList = lstC
    lstChemin = ["C:/"]
    k = True
    f.writelines(lstChemin[-1])
    while (len(lstC) != 0):
        p = False
        if k:
            lstC = []
            k = False
        esp += 1
        i = 0
        l = len(tmpList)
        if (l == 1 and not os.path.isfile(chemin+tmpList[0])):
            p = True
        while (i < l):
            fich = tmpList[i]
            if os.path.isfile(chemin+fich):
                f.writelines(["\n"])
                f.writelines(["    "*esp, fich])
                tmpList.remove(fich)
                i -= 1
                l -= 1
            i += 1
        lstC = tmpList+lstC
        print("lstC === ", lstC)
        # if lstC[0] == "Config.Msi" or lstC[0] == "$Recycle.Bin" or lstC[0] == "Documents and Settings" or lstC[0] == "IntelOptaneData" or lstC[0] == "MSOCache" or lstC[0] == "PerfLogs" or lstC[0] == "Fichiers communs" or lstC[0] == "Accessoires" or lstC[0] == "WindowsApps":
        #     if lstC[0] == "Config.Msi":
        #         f.writelines(["\n", "    ", "Config.Msi"])
        #     if lstC[0] == "$Recycle.Bin":
        #         f.writelines(["\n", "    ", "$Recycle.Bin"])
        #     if lstC[0] == "Documents and Settings":
        #         f.writelines(["\n", "    ", "Documents and Settings"])
        #     if lstC[0] == "IntelOptaneData":
        #         f.writelines(["\n", "    "*2, "Documents and Settings"])
        #     if lstC[0] == "MSOCache":
        #         f.writelines(["\n", "    ", "MSOCache"])
        #     if lstC[0] == "PerfLogs":
        #         f.writelines(["\n", "    ", "PerfLogs"])
        #     if lstC[0] == "Fichiers communs":
        #         f.writelines(["\n", "    "*2, "Fichiers communs"])
        #     if lstC[0] == "Accessoires":
        #         f.writelines(["\n", "    "*3, "Accessoires"])
        #     if lstC[0] == "WindowsApps":
        #         f.writelines(["\n", "    "*2, "WindowsApps"])
        #     del lstC[0]
        if lstC[0] == "$Recycle.Bin":
            f.writelines(["\n", "    ", "$Recycle.Bin"])
            del lstC[0]
        detChemin()

        while (True):
            try:
                tmpList = os.listdir(chemin)
                break
            except:
                detChemin()
                esp += 1

        # print("chemin == ", chemin)

        if p:
            f.write(lstChemin[-1])
        else:
            f.writelines(["\n", "    "*esp, lstChemin[-1]])

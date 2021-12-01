from tkinter import *

def createNewGoalWin():
     if isGoalEnough():
          goalEnoughLabel.configure(text = "紐⑺몴瑜� �뜑 �씠�긽 異붽���븷 �닔 �뾾�뒿�땲�떎. 紐⑺몴�뒗 8媛쒓퉴吏� 異붽�� 媛��뒫�빀�땲�떎.")
     else:     
          global newGoalWin
          newGoalWin = Toplevel(root)
          newGoalWin.title("紐⑺몴 異붽���븯湲�")
          newGoalWin.geometry("480x360")
          newGoalWin.configure(bg = 'white')
          label=Label(newGoalWin,fg = _from_rgb(bigTLColor), text="異붽���븷 紐⑺몴瑜� �엯�젰�빐 二쇱꽭�슂.",font = ("留묒�� 怨좊뵓",20,"bold"),bg = 'white')
          label.place(x=60,y=50)
          global textbox
          textbox = Entry(newGoalWin, width=40, textvariable=str, highlightthickness=2)
          textbox.place(x=80,y=130)
          button = Button(newGoalWin, overrelief="solid", width=4,text="異붽��",command = createNewGoal,bg = _from_rgb(bigTLColor),fg = 'white')
          button.place(x=400,y=125)

def createNewGoal():
     file = open("goalsList.txt",'r')
     stateFile = open("goalState.txt", 'r')
     goalName = file.readlines()
     goalState = stateFile.readlines()
     goalEnough = True
     for name in goalName:
          if "紐⑺몴媛� �뾾�뒿�땲�떎.\n" == name:
               goalEnough = False
               goalName[goalName.index(name)] = textbox.get()+"\n"
               print(goalName)
               break
     for state in goalState:
          if "紐⑺몴媛� �뾾�뒿�땲�떎.\n" == state:
               goalState[goalState.index(state)] = "x\n"
               print(goalState)
               break
     file.close()
     stateFile.close()
     file = open("goalsList.txt",'w')
     stateFile = open("goalState.txt", 'w')
     print(goalName)
     file.writelines(goalName)
     stateFile.writelines(goalState)
     file.close()
     stateFile.close()
     changeCheckbuttonText()
     change_img()
     newGoalWin.destroy()

def changeCheckbuttonText():
     checkBList = [checkB1,checkB2,checkB3,checkB4,checkB5,checkB6,checkB7,checkB8]
     varList = [v1,v2,v3,v4,v5,v6,v7,v8]
     hideCheckbutton(checkBList)
     fileForOpen = open("goalsList.txt", 'r')
     goalName = fileForOpen.readlines()
     print("�깉濡쒓퀬移� �뿴��� goalName")
     print(goalName)
     fileForOpen.close()
     for name in goalName:
          if "紐⑺몴媛� �뾾�뒿�땲�떎.\n" == name:
               del checkBList[goalName.index(name):]
               break
          varList[goalName.index(name)].set(name)
          print(name)
     print(checkBList)
     packCheckbutton(checkBList)
     
def hideCheckbutton(checkBLi):
     for checkB in checkBLi:
          checkB.place_forget()
def isGoalEnough():
     file = open("goalsList.txt",'r')
     goalName = file.readlines()
     goalEnough = True
     for name in goalName:
          if "紐⑺몴媛� �뾾�뒿�땲�떎." in name:
               goalEnough = False
               break
     return goalEnough
def packCheckbutton(checkBLi):
     initX = 600
     initY = 100
     interval = 40
     try:
          checkBLi[0].place(x=initX,y=initY)
     except:
          pass
     try:
          checkBLi[1].place(x=initX,y=initY+interval)
     except:
          pass
     try:
          checkBLi[2].place(x=initX,y=initY+interval*2)
     except:
          pass
     try:
          checkBLi[3].place(x=initX,y=initY+interval*3)
     except:
          pass
     try:
          checkBLi[4].place(x=initX,y=initY+interval*4)
     except:
          pass
     try:
          checkBLi[5].place(x=initX,y=initY+interval*5)
     except:
          pass
     try:
          checkBLi[6].place(x=initX,y=initY+interval*6)
     except:
          pass
     try:
          checkBLi[7].place(x=initX,y=initY+interval*7)
     except:
          pass
     
def check_goal_state():
     fileForOpen = open("goalState.txt", 'r')
     goalState = fileForOpen.readlines()
     global first_no_goal
     global first_num_goal
     global first_sc_goal
     first_no_goal = 0
     first_num_goal = 0
     first_sc_goal = 0
     for state in goalState:
        if state == "紐⑺몴媛� �뾾�뒿�땲�떎.\n":
            first_no_goal+=1
        if state == "o\n":
            first_sc_goal+=1
     first_num_goal = len(goalState) - first_no_goal          

def success_goal():
        while sc_goal <= num_goal :
            label =Label(root, text="none", image =goal_list[num_goal-1][int(sc_goal)])   
            label.pack(side = LEFT, padx = 0)
            break

def change_state():
     file = open("goalState.txt",'w')
     for state in checkVar:
          if state.get() == 1 :
               file.write("o\n")
          if state.get() == 0 :
               file.write("x\n")
          if state == '':
               file.write("紐⑺몴媛� �뾾�뒿�땲�떎.\n")
     file.close()

def check_click():
     file = open("goalState.txt",'r')
     goalState = file.readlines()
     a=0
     for state in goalState:
          a += 1
          if state == "o\n":
               checkBList[a-1].select()
          if state == "x\n":
               checkBList[a-1].deselect()
          if state == "紐⑺몴媛� �뾾�뒿�땲�떎.\n":
               file.close()
               break

def deleteGoalWin():
     if isNoGoal():
          goalEnoughLabel.configure(text = "�궘�젣�븷 紐⑺몴媛� �뾾�뒿�땲�떎.")
     else:     
          global newDeleteGoalWin
          newDeleteGoalWin = Toplevel(root)
          newDeleteGoalWin.title("紐⑺몴 �궘�젣�븯湲�")
          newDeleteGoalWin.geometry("480x360")
          newDeleteGoalWin.configure(bg = "white")
          label=Label(newDeleteGoalWin,fg = _from_rgb(bigTLColor), text="�궘�젣�븷 紐⑺몴瑜� �엯�젰�빐 二쇱꽭�슂.",font = ("留묒�� 怨좊뵓",20,"bold"),bg = 'white')
          label.place(x=60,y=50)
          global deleteTextbox
          deleteTextbox = Entry(newDeleteGoalWin, width=40, textvariable=str, highlightthickness=2)
          deleteTextbox.place(x=80,y=130)
          global warningLabel
          warningLabel=Label(newDeleteGoalWin, text="", width=40,bg = 'white',font = ("留묒�� 怨좊뵓",10))
          warningLabel.place(x=80,y=160)
          deleteButton = Button(newDeleteGoalWin, overrelief="solid", width=4,text="�궘�젣",command = deleteGoal,bg = _from_rgb(bigTLColor),fg = 'white')
          deleteButton.place(x=400,y=125)

def deleteGoal():
     file = open("goalsList.txt",'r')
     stateFile = open("goalState.txt",'r')
     goalName = file.readlines()
     goalState = stateFile.readlines()
     goalEnough = True
     findGoal = False
     for name in goalName:
          print("�엯�젰媛�: ",deleteTextbox.get()+"\n","name: ",name)
          if deleteTextbox.get() + "\n" == name:
               print(goalName.index(name))
               goalState.remove(goalState[goalName.index(name)])
               goalState.append("紐⑺몴媛� �뾾�뒿�땲�떎.\n")
               goalName.remove(name)
               goalName.append("紐⑺몴媛� �뾾�뒿�땲�떎.\n")
               findGoal = True
               break
     if not findGoal:
          warningLabel.configure(text = "�빐�떦 �씪�젙�씠 議댁옱�븯吏� �븡�뒿�땲�떎.")
          return
     file.close()
     stateFile.close()
     file = open("goalsList.txt",'w')
     stateFile = open("goalState.txt",'w')
     print("�궘�젣�슜�쑝濡� �뿴��� goalName")
     print(goalName)
     file.writelines(goalName)
     stateFile.writelines(goalState)
     file.close()
     stateFile.close()
     changeCheckbuttonText()
     change_img()
     newDeleteGoalWin.destroy()

def isNoGoal():
     file = open("goalsList.txt",'r')
     goalName = file.readlines()
     noGoal = True
     for name in goalName:
          if "紐⑺몴媛� �뾾�뒿�땲�떎." in name:
               pass
          else:
               noGoal = False
               break
     return noGoal
def infoWin():    
     newinfoWin = Toplevel(root)
     newinfoWin.title("�봽濡쒓렇�옩 �꽕紐�")
     newinfoWin.geometry("600x360")
     newinfoWin.configure(bg = 'white')
     info = '''
     而댄벂�꽣濡� �옉�뾽�쓣 �븷 �븣, �씠 �봽濡쒓렇�옩�쓣 �뿴�뼱�꽌 泥댄겕由ъ뒪�듃濡� �벝 �닔 �엳�뒿�땲�떎.
     �옄�떊�씠 紐⑺몴瑜� �븯�굹�뵫 �씠琉꾧��硫�, �쇊�렪�쓽 罹먮┃�꽣媛� 留덈씪�넠�쓣 �셿二쇳븷 �닔 �엳�뒿�땲�떎.
     �뵳�뵳�븳 硫붾え�옣 留먭퀬 洹��뿬�슫 罹먮┃�꽣媛� �엳�뒗 泥댄겕由ъ뒪�듃瑜� �궗�슜�빐 蹂댁꽭�슂!

     *�궗�슜�꽕紐�*
     1. 癒쇱�� �겙 紐⑺몴�쓽 �씠由꾩쓣 �꽕�젙�빐二쇱꽭�슂!
         :�닔�젙踰꾪듉�쓣 �늻瑜대㈃ �겙 紐⑺몴�쓽 �씠由꾩쓣 �꽕�젙�븷 �닔 �엳�뒿�땲�떎.

     2. �옉��� 紐⑺몴瑜� �꽕�젙�빐二쇱꽭�슂!
         :�븯�떒�쓽 �씪�젙 異붽�� 踰꾪듉�쓣 �늻瑜대㈃ �옄�떊�쓽 �씪�젙�쓣 異붽���븷 �닔 �엳�뒿�땲�떎.
         :�떒, 紐⑺몴�뒗 8媛� 源뚯��留� �꽕�젙�븷 �닔 �엳�뒿�땲�떎.

     3. 紐⑺몴瑜� �씠猷곕븣 留덈떎 �씪�젙 �씠由� �쇊�렪�쓽 鍮덉뭏�쓣 泥댄겕�빐二쇱꽭�슂!
          :泥댄겕踰꾪듉�쓣 �늻瑜쇰븣留덈떎 �쇊�렪�쓽 洹몃┝�씠 ���吏곸씪 寃껋엯�땲�떎!
          :泥댄겕�긽�깭�뿉�꽌 �븳踰� �뜑 �늻瑜� 寃쎌슦, 泥댄겕�뒗 �빐�젣�릺怨�, 罹먮┃�꽣�룄 �븳移� �뮘濡� 媛� 寃껋엯�땲�떎.

     4. �씪�젙�쓣 �궘�젣�빐二쇱꽭�슂!
          :�븯�떒�쓽 �씪�젙�궘�젣 踰꾪듉�쓣 �늻瑜닿퀬, �궘�젣�븯怨� �떢��� �씪�젙�쓽 �씠由꾩쓣 �젙�솗�엳 �쟻�뼱二쇱꽭�슂.
          :�씪�젙�쓣 �닔�젙�븯怨� �떢�쓣 �븣�뒗 �궘�젣�븯怨� �떎�떆 留뚮뱾�뼱二쇱꽭�슂.
     '''
     warningLabel=Label(newinfoWin, text=info, font = ("留묒�� 怨좊뵓",10),bg = 'white')
     warningLabel.pack()

def change_state():
     file_list_n = open("goalsList.txt",'r')
     goal_list_n = file_list_n.readlines()
     file_list_n.close()
     file_state = open("goalState.txt",'w')
     for state in checkVar:
          if goal_list_n[checkVar.index(state)] == '紐⑺몴媛� �뾾�뒿�땲�떎.\n':
               file_state.write("紐⑺몴媛� �뾾�뒿�땲�떎.\n")
          elif state.get() == 1 :
               file_state.write("o\n")
          elif state.get() == 0 :
               file_state.write("x\n")
     file_state.close()
     change_img()

def change_img():
     no_goal = 0
     sc_goal = 0
     num_goal = 0   
     fileOpen = open("goalState.txt", 'r')
     goalState = fileOpen.readlines()
     for state in goalState:
        if state == "紐⑺몴媛� �뾾�뒿�땲�떎.\n":
            no_goal+=1
        if state == "o\n":
            sc_goal+=1
     num_goal = len(goalState) - no_goal
     label_img.configure(image = goal_list[num_goal-1][sc_goal])
     fileOpen.close()

def changeBigGoal():
     file = open("bigGoalName.txt",'r')
     bigGoalLabel.configure(text = file.readline())
     file.close()
     
def createBigGoal():
     file = open("bigGoalName.txt",'w')
     file.write(bigGoalTextbox.get())
     file.close()
     changeBigGoal()
     newBigGoalWin.destroy()
     
def makeBigGoalWin():
     global newBigGoalWin
     newBigGoalWin= Toplevel(root)
     newBigGoalWin.title("�겙 紐⑺몴 �닔�젙�븯湲�")
     newBigGoalWin.geometry("480x360")
     newBigGoalWin.configure(bg = 'white')
     label=Label(newBigGoalWin,fg = _from_rgb(bigTLColor), text="�궡�슜 �닔�젙", width=10,font = ("留묒�� 怨좊뵓",20,"bold"),bg = 'white')
     label.place(x=160,y=50)
     global bigGoalTextbox
     bigGoalTextbox = Entry(newBigGoalWin, width=40, textvariable=str, highlightthickness=2)
     bigGoalTextbox.place(x=80,y=130)
     changBigGoalNameButton = Button(newBigGoalWin, overrelief="solid", width=4,text="�닔�젙", font = ("留묒�� 怨좊뵓",10),command = createBigGoal,bg = _from_rgb(bigTLColor),fg = 'white')
     changBigGoalNameButton.place(x=400,y=125)

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb 
#硫붿씤李� �꽕�젙
root = Tk()

root.title("紐⑺몴留덈씪�넠")
root.geometry("1080x720")
root.configure(background='white')
root.resizable(False, False)
bigTLColor = (64,66,103)
image1 = PhotoImage(file="0.PNG")
image2 = PhotoImage(file="11.PNG")
image3 = PhotoImage(file="25.PNG")
image4 = PhotoImage(file="32.PNG")
image5 = PhotoImage(file="40.PNG")
image6 = PhotoImage(file="50.PNG")
image7 = PhotoImage(file="75.PNG")
image8 = PhotoImage(file="90.PNG")
image9 = PhotoImage(file="100.PNG")
goal1=[image1, image9]
goal2=[image1, image6, image9]
goal3=[image1, image4, image7, image9]
goal4=[image1, image3, image6, image7, image9]
goal5=[image1, image2, image4, image5, image8, image9]
goal6=[image1, image2, image4, image5, image7, image8, image9]
goal7=[image1, image2, image4, image5, image6, image7, image8, image9]
goal8=[image1, image2, image3, image4, image5, image6, image7, image8, image9]
goal_list=[goal1, goal2, goal3, goal4, goal5, goal6, goal7, goal8]


check_goal_state()

fileForOpen = open("goalState.txt", 'r')
goalState = fileForOpen.readlines()
first_no_goal = 0
first_num_goal = 0
first_sc_goal = 0
for state in goalState:
     if state == "紐⑺몴媛� �뾾�뒿�땲�떎.\n":
          first_no_goal = first_no_goal + 1
     if state == "o\n":
          first_sc_goal+=1
first_num_goal = 8 - first_no_goal
photo = goal_list[first_num_goal-1][int(first_sc_goal)]
label_img =Label(root, text="none", image =photo)
label_img.pack(side = LEFT, padx = 0)
fileForOpen.close()

bigGoalLabel=Label(root, text="__", width=200, font = ("留묒�� 怨좊뵓",30,"bold"),bg = 'white',fg = _from_rgb((32, 30, 69)))
bigGoalLabel.pack()
reviseButton = Button(root, overrelief="solid", width=4,text="�닔�젙",fg = 'white',command = makeBigGoalWin,font = ("留묒�� 怨좊뵓",10),bg = _from_rgb(bigTLColor))
reviseButton.place(x=1020, y= 15)
     
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
v4 = StringVar()
v5 = StringVar()
v6 = StringVar()
v7 = StringVar()
v8 = StringVar()
cVar1 = IntVar()
cVar2 = IntVar()
cVar3 = IntVar()
cVar4 = IntVar()
cVar5 = IntVar()
cVar6 = IntVar()
cVar7 = IntVar()
cVar8 = IntVar()

cbFontSize = 13
checkB1 = Checkbutton(root, text = "1", textvariable=v1, variable = cVar1, command = change_state,font = ("留묒�� 怨좊뵓",cbFontSize),bg = 'white')
checkB2 = Checkbutton(root, text = "2", textvariable=v2, variable = cVar2, command = change_state,font = ("留묒�� 怨좊뵓",cbFontSize),bg = 'white')
checkB3 = Checkbutton(root, text = "3", textvariable=v3, variable = cVar3, command = change_state,font = ("留묒�� 怨좊뵓",cbFontSize),bg = 'white')
checkB4 = Checkbutton(root, text = "4", textvariable=v4, variable = cVar4, command = change_state,font = ("留묒�� 怨좊뵓",cbFontSize),bg = 'white')
checkB5 = Checkbutton(root, text = "5", textvariable=v5, variable = cVar5, command = change_state,font = ("留묒�� 怨좊뵓",cbFontSize),bg = 'white')
checkB6 = Checkbutton(root, text = "6", textvariable=v6, variable = cVar6, command = change_state,font = ("留묒�� 怨좊뵓",cbFontSize),bg = 'white')
checkB7 = Checkbutton(root, text = "7", textvariable=v7, variable = cVar7, command = change_state,font = ("留묒�� 怨좊뵓",cbFontSize),bg = 'white')
checkB8 = Checkbutton(root, text = "8", textvariable=v8, variable = cVar8, command = change_state,font = ("留묒�� 怨좊뵓",cbFontSize),bg = 'white')
checkBList = [checkB1,checkB2,checkB3,checkB4,checkB5,checkB6,checkB7,checkB8]
checkVar = [cVar1, cVar2, cVar3, cVar4, cVar5, cVar6, cVar7, cVar8]
varList = [v1,v2,v3,v4,v5,v6,v7,v8]

changeBigGoal()
changeCheckbuttonText()
check_click()


goalEnoughLabel=Label(root, text="", width=70,font = ("留묒�� 怨좊뵓",10),bg = 'white')
goalEnoughLabel.place(x = 480, y = 630)

infoImage = PhotoImage(file="info.png")
infoButton = Button(root, overrelief="solid", width=40,image = infoImage,command = infoWin,bg = 'white')
infoButton.place(x = 380 , y = 665)
#�씪�젙 異붽�� 踰꾪듉
addGoalButton = Button(root, overrelief="solid", width=10,text="紐⑺몴 異붽��",command = createNewGoalWin,font = ("留묒�� 怨좊뵓",10),bg = _from_rgb(bigTLColor),fg = 'white')
addGoalButton.place(x = 640 , y = 675)

#�씪�젙 �궘�젣 踰꾪듉
deleteGoalButton = Button(root, overrelief="solid", width=10,text="紐⑺몴 �궘�젣",command = deleteGoalWin,font = ("留묒�� 怨좊뵓",10),bg = _from_rgb(bigTLColor),fg = 'white')
deleteGoalButton.place(x = 750 , y = 675)
 
root.mainloop()

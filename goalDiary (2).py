from tkinter import *

def createNewGoalWin():
     if isGoalEnough():
          goalEnoughLabel.configure(text = "목표를 더 이상 추가할 수 없습니다. 목표는 8개까지 추가 가능합니다.")
     else:     
          global newGoalWin
          newGoalWin = Toplevel(root)
          newGoalWin.title("목표 추가하기")
          newGoalWin.geometry("480x360")
          newGoalWin.configure(bg = 'white')
          label=Label(newGoalWin,fg = _from_rgb(bigTLColor), text="추가할 목표를 입력해 주세요.",font = ("맑은 고딕",20,"bold"),bg = 'white')
          label.place(x=60,y=50)
          global textbox
          textbox = Entry(newGoalWin, width=40, textvariable=str, highlightthickness=2)
          textbox.place(x=80,y=130)
          button = Button(newGoalWin, overrelief="solid", width=4,text="추가",command = createNewGoal,bg = _from_rgb(bigTLColor),fg = 'white')
          button.place(x=400,y=125)

def createNewGoal():
     file = open("goalsList.txt",'r')
     stateFile = open("goalState.txt", 'r')
     goalName = file.readlines()
     goalState = stateFile.readlines()
     goalEnough = True
     for name in goalName:
          if "목표가 없습니다.\n" == name:
               goalEnough = False
               goalName[goalName.index(name)] = textbox.get()+"\n"
               print(goalName)
               break
     for state in goalState:
          if "목표가 없습니다.\n" == state:
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
     print("새로고침 열은 goalName")
     print(goalName)
     fileForOpen.close()
     for name in goalName:
          if "목표가 없습니다.\n" == name:
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
          if "목표가 없습니다." in name:
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
        if state == "목표가 없습니다.\n":
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
               file.write("목표가 없습니다.\n")
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
          if state == "목표가 없습니다.\n":
               file.close()
               break

def deleteGoalWin():
     if isNoGoal():
          goalEnoughLabel.configure(text = "삭제할 목표가 없습니다.")
     else:     
          global newDeleteGoalWin
          newDeleteGoalWin = Toplevel(root)
          newDeleteGoalWin.title("목표 삭제하기")
          newDeleteGoalWin.geometry("480x360")
          newDeleteGoalWin.configure(bg = "white")
          label=Label(newDeleteGoalWin,fg = _from_rgb(bigTLColor), text="삭제할 목표를 입력해 주세요.",font = ("맑은 고딕",20,"bold"),bg = 'white')
          label.place(x=60,y=50)
          global deleteTextbox
          deleteTextbox = Entry(newDeleteGoalWin, width=40, textvariable=str, highlightthickness=2)
          deleteTextbox.place(x=80,y=130)
          global warningLabel
          warningLabel=Label(newDeleteGoalWin, text="", width=40,bg = 'white',font = ("맑은 고딕",10))
          warningLabel.place(x=80,y=160)
          deleteButton = Button(newDeleteGoalWin, overrelief="solid", width=4,text="삭제",command = deleteGoal,bg = _from_rgb(bigTLColor),fg = 'white')
          deleteButton.place(x=400,y=125)

def deleteGoal():
     file = open("goalsList.txt",'r')
     stateFile = open("goalState.txt",'r')
     goalName = file.readlines()
     goalState = stateFile.readlines()
     goalEnough = True
     findGoal = False
     for name in goalName:
          print("입력값: ",deleteTextbox.get()+"\n","name: ",name)
          if deleteTextbox.get() + "\n" == name:
               print(goalName.index(name))
               goalState.remove(goalState[goalName.index(name)])
               goalState.append("목표가 없습니다.\n")
               goalName.remove(name)
               goalName.append("목표가 없습니다.\n")
               findGoal = True
               break
     if not findGoal:
          warningLabel.configure(text = "해당 일정이 존재하지 않습니다.")
          return
     file.close()
     stateFile.close()
     file = open("goalsList.txt",'w')
     stateFile = open("goalState.txt",'w')
     print("삭제용으로 열은 goalName")
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
          if "목표가 없습니다." in name:
               pass
          else:
               noGoal = False
               break
     return noGoal
def infoWin():    
     newinfoWin = Toplevel(root)
     newinfoWin.title("프로그램 설명")
     newinfoWin.geometry("600x360")
     newinfoWin.configure(bg = 'white')
     info = '''
     컴퓨터로 작업을 할 때, 이 프로그램을 열어서 체크리스트로 쓸 수 있습니다.
     자신이 목표를 하나씩 이뤄가면, 왼편의 캐릭터가 마라톤을 완주할 수 있습니다.
     딱딱한 메모장 말고 귀여운 캐릭터가 있는 체크리스트를 사용해 보세요!

     *사용설명*
     1. 먼저 큰 목표의 이름을 설정해주세요!
         :수정버튼을 누르면 큰 목표의 이름을 설정할 수 있습니다.

     2. 작은 목표를 설정해주세요!
         :하단의 일정 추가 버튼을 누르면 자신의 일정을 추가할 수 있습니다.
         :단, 목표는 8개 까지만 설정할 수 있습니다.

     3. 목표를 이룰때 마다 일정 이름 왼편의 빈칸을 체크해주세요!
          :체크버튼을 누를때마다 왼편의 그림이 움직일 것입니다!
          :체크상태에서 한번 더 누를 경우, 체크는 해제되고, 캐릭터도 한칸 뒤로 갈 것입니다.

     4. 일정을 삭제해주세요!
          :하단의 일정삭제 버튼을 누르고, 삭제하고 싶은 일정의 이름을 정확히 적어주세요.
          :일정을 수정하고 싶을 때는 삭제하고 다시 만들어주세요.
     '''
     warningLabel=Label(newinfoWin, text=info, font = ("맑은 고딕",10),bg = 'white')
     warningLabel.pack()

def change_state():
     file_list_n = open("goalsList.txt",'r')
     goal_list_n = file_list_n.readlines()
     file_list_n.close()
     file_state = open("goalState.txt",'w')
     for state in checkVar:
          if goal_list_n[checkVar.index(state)] == '목표가 없습니다.\n':
               file_state.write("목표가 없습니다.\n")
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
        if state == "목표가 없습니다.\n":
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
     newBigGoalWin.title("큰 목표 수정하기")
     newBigGoalWin.geometry("480x360")
     newBigGoalWin.configure(bg = 'white')
     label=Label(newBigGoalWin,fg = _from_rgb(bigTLColor), text="내용 수정", width=10,font = ("맑은 고딕",20,"bold"),bg = 'white')
     label.place(x=160,y=50)
     global bigGoalTextbox
     bigGoalTextbox = Entry(newBigGoalWin, width=40, textvariable=str, highlightthickness=2)
     bigGoalTextbox.place(x=80,y=130)
     changBigGoalNameButton = Button(newBigGoalWin, overrelief="solid", width=4,text="수정", font = ("맑은 고딕",10),command = createBigGoal,bg = _from_rgb(bigTLColor),fg = 'white')
     changBigGoalNameButton.place(x=400,y=125)

def _from_rgb(rgb):
    return "#%02x%02x%02x" % rgb 
#메인창 설정
root = Tk()

root.title("목표마라톤")
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
     if state == "목표가 없습니다.\n":
          first_no_goal = first_no_goal + 1
     if state == "o\n":
          first_sc_goal+=1
first_num_goal = 8 - first_no_goal
photo = goal_list[first_num_goal-1][int(first_sc_goal)]
label_img =Label(root, text="none", image =photo)
label_img.pack(side = LEFT, padx = 0)
fileForOpen.close()

bigGoalLabel=Label(root, text="__", width=200, font = ("맑은 고딕",30,"bold"),bg = 'white',fg = _from_rgb((32, 30, 69)))
bigGoalLabel.pack()
reviseButton = Button(root, overrelief="solid", width=4,text="수정",fg = 'white',command = makeBigGoalWin,font = ("맑은 고딕",10),bg = _from_rgb(bigTLColor))
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
checkB1 = Checkbutton(root, text = "1", textvariable=v1, variable = cVar1, command = change_state,font = ("맑은 고딕",cbFontSize),bg = 'white')
checkB2 = Checkbutton(root, text = "2", textvariable=v2, variable = cVar2, command = change_state,font = ("맑은 고딕",cbFontSize),bg = 'white')
checkB3 = Checkbutton(root, text = "3", textvariable=v3, variable = cVar3, command = change_state,font = ("맑은 고딕",cbFontSize),bg = 'white')
checkB4 = Checkbutton(root, text = "4", textvariable=v4, variable = cVar4, command = change_state,font = ("맑은 고딕",cbFontSize),bg = 'white')
checkB5 = Checkbutton(root, text = "5", textvariable=v5, variable = cVar5, command = change_state,font = ("맑은 고딕",cbFontSize),bg = 'white')
checkB6 = Checkbutton(root, text = "6", textvariable=v6, variable = cVar6, command = change_state,font = ("맑은 고딕",cbFontSize),bg = 'white')
checkB7 = Checkbutton(root, text = "7", textvariable=v7, variable = cVar7, command = change_state,font = ("맑은 고딕",cbFontSize),bg = 'white')
checkB8 = Checkbutton(root, text = "8", textvariable=v8, variable = cVar8, command = change_state,font = ("맑은 고딕",cbFontSize),bg = 'white')
checkBList = [checkB1,checkB2,checkB3,checkB4,checkB5,checkB6,checkB7,checkB8]
checkVar = [cVar1, cVar2, cVar3, cVar4, cVar5, cVar6, cVar7, cVar8]
varList = [v1,v2,v3,v4,v5,v6,v7,v8]

changeBigGoal()
changeCheckbuttonText()
check_click()


goalEnoughLabel=Label(root, text="", width=70,font = ("맑은 고딕",10),bg = 'white')
goalEnoughLabel.place(x = 480, y = 630)

infoImage = PhotoImage(file="info.png")
infoButton = Button(root, overrelief="solid", width=40,image = infoImage,command = infoWin,bg = 'white')
infoButton.place(x = 380 , y = 665)
#일정 추가 버튼
addGoalButton = Button(root, overrelief="solid", width=10,text="목표 추가",command = createNewGoalWin,font = ("맑은 고딕",10),bg = _from_rgb(bigTLColor),fg = 'white')
addGoalButton.place(x = 640 , y = 675)

#일정 삭제 버튼
deleteGoalButton = Button(root, overrelief="solid", width=10,text="목표 삭제",command = deleteGoalWin,font = ("맑은 고딕",10),bg = _from_rgb(bigTLColor),fg = 'white')
deleteGoalButton.place(x = 750 , y = 675)
 
root.mainloop()

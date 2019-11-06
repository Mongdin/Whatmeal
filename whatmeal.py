from random import randrange

cat = ["락궁","맘스터치","땅땅치킨"]






while(1):
    print('\n----------------------------------------------------\n말해보시오\n')
    ans = input("뭐뭐있는데 : 뭐있나보여줌\n뭐먹을까 : 메뉴골라줌 \n잘모르겠어 : 해보시지 \n추가할래 : 메뉴추가\n안먹을래 : 나가기\n----------------------------------------------------\n>>>")
    
    if ans == "뭐먹을까":
        a = randrange(0,len(cat))
        print("\n"+cat[a]+"먹어라"+"\n")



    elif ans == "뭐뭐있는데":
        for x in range(len(cat)):
            print('\n'+cat[x])

    elif ans == "추가할래":
          cat.append(input("뭐추가할래?"))
          
    elif ans == "잘모르겠어":
        what = []
        for x in range(100):
            a = randrange(0,len(cat))
            what.append(cat[a])
        print('\n')
        cnt = []
        for x in range(len(cat)):
            print('\n'+cat[x]+" : {}".format(what.count(cat[x]))+"표")
            cnt.append(what.count(cat[x]))
        
        print("\n"+str(max(cnt))+"표 받은 "+cat[cnt.index(int(max(cnt)))]+"먹어라")
        

    elif ans == "안먹을래":
        print("구래~")
        break

    else:
        print("뭐라는거야")

print("안녀엉~")
        

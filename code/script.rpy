
define nike = Character("千坂田妮可", color="#d25145", image = "nike")
define jieyi = Character("春日结衣", color="#c5ae27", image = "jieyi")
define yin = Character("春日影", color="#b39a0e")
define hua = Character("泉镜花", color="#6274c4")
define mizi = Character("四月一日弥子", color="#c657e4", image = "mizi")
define ni = Character("你", color="#3c80a2")

define zeyeju = Character("泽野雏菊", color="#c68331")
define tichuanchun = Character("笹川春", color="#c63180")

define buzhimingnvshi = Character("不知名女士", color="#000000")
define weizhiren = Character("???" , color="#000000")
define shafulin = Character("沙芙林" , color="#401dc0")
define xiuji = Character("秀吉", color="#d97121")
define kenan = Character("打了无效马赛克的小学生", color="#171134")
define mowang = Character("魔王", color="#000000")
define authorNames = ["陈依澄"]
# 动作
init python:
    import pygame
    import random
    def wiggleFuncX(trans, st, at):
        if st > 0.4:
            trans.xalign = 0.5
            return None
        elif st > 0.3:
            trans.xalign = 0.47 + (st-0.3)*0.3
            return 0
        elif st > 0.2:
            trans.xalign = 0.5 - (st-0.2)*0.3
            return 0
        elif st > 0.1:
            trans.xalign = 0.53 - (st-0.1)*0.3
            return 0
        else:
            trans.xalign = 0.5 + st*0.3
            return 0
    def wiggleFuncY(trans, st, at):
        if st > 0.4:
            trans.yalign = 1.0
            return None
        elif st > 0.2:
            trans.yalign = 2.0 - (st-0.2)*5
            return 0
        else:
            trans.yalign = 1.0 + st*5
            return 0

    def happyShake(trans, st, at):
        if st > 0.4:
            trans.yalign = 1.0
            return None
        elif st > 0.3:
            trans.yalign = 1.3 - (st-0.3)*3
            return 0
        elif st > 0.2:
            trans.yalign = 1.0 + (st-0.2)*3
            return 0
        elif st > 0.1:
            trans.yalign = 1.3 - (st-0.1)*3
            return 0
        else:
            trans.yalign = 1.0 + st*3
            return 0
    def crazy(trans, st, at):
        trans.xalign = 0.5 + random.random()*0.1
        trans.yalign = 1.0 - random.random()*2
        trans.zoom = 0.6+random.random()*2
        return 0.05
    def crazyBg(trans, st, at):
        trans.zoom = random.random()*0.1+1.0
        return 0.05
    def notcrazy(trans, st, at):
        if st > 0.1:
            return None
        trans.xalign = 0.5
        trans.yalign = 1.0
        trans.zoom = 1.0
        trans.rotation = 0.0
        return 0
    # def blockAllMouseInput(event,interact,**kwargs):
    #     print(event)
    #     if event == "begin":
    #         pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
    #     elif event == "slow_done":
    #         pygame.event.set_allowed(pygame.MOUSEBUTTONUP)
    # config.all_character_callbacks += [blockAllMouseInput]



# define renpy.config.all_character_callbacks = blockAllMouseInput
define firstStoryScore = 0
define thirdStoryScore = 0
label willEnd:
    scene black with fade
    "游戏结束，你获得[firstStoryScore]分"
    menu:
        "{color=#000}重新开始{/color}":
            jump start
label start:
    # TODO：发布版本代码
    # $ isEasterEgg = False
    # $ selectedStory = 0
    # python:
    #     import random
    #     random_number = random.random()
    #     probability_of_event = 0.1
    #     if random_number < probability_of_event:
    #         isEasterEgg = True
    #     else:
    #         selectedStory = random.randint(1,3)
    # if(isEasterEgg):
    #     jump easterEgg
    # elif(selectedStory == 1):
    #     $ firstStoryScore = 0
    #     jump firstStory
    # elif(selectedStory == 2):
    #     jump secondStory
    # else:
    #     $ thirdStoryScore = 0
    #     jump thirdStory


    menu:
        "{color=#000}black 剧本{/color}":
            $ thirdStoryScore = 0
            jump thirdStory
        "{color=#000}琥珀 剧本{/color}":
            $ firstStoryScore = 0
            jump firstStory
        "{color=#000}花言斋 剧本{/color}":
            jump secondStory
        "{color=#000}彩蛋{/color}":
            jump easterEgg
    return

label firstStory:
    scene black with fade
    menu:
        "{color=#000}观看角色介绍{/color}":
            jump .introduce
        "{color=#000}直接开始{/color}":
            jump .choiceA
    label .introduce:
        show nike normal with dissolve
        """
        千坂田妮可
        主修声乐，之前未接触过乐队
        天真活泼双钻头，是校长的侄女。
        """
        hide nike 
        show jieyi normal 
        with dissolve
        """
        春日结衣
        影的姐姐
        学校原有乐队成员，家境不好
        短发严肃，难以接近，对乐队话题有抵触
        """
        hide jieyi
        show yin normal
        with dissolve
        """
        春日影
        学校原有乐队成员，家境不好
        长发胆小，容易害羞也较为脆弱，一直怀念当时乐队但对于原因一直被蒙在鼓里
        个子矮
        """
        hide yin
        show hua normal 
        with dissolve
        """
        泉镜花
        名字出处是日本一位大作家，眼镜娘
        平时安静沉稳，喜欢文学；但弹贝斯时就是疯批美人，未组过乐队，与结衣是好朋友。
        """
        hide hua
        show mizi normal 
        with dissolve
        """
        四月一日弥子，个字高，黑长直
        校长大人，（很久以前）曾经乐队鼓手，大姐姐
        """
        hide mizi
        jump .choiceA
    label .choiceA:
        "一座历史悠久的艺术学院——角川艺术学院……需要在某次大型活动中以优异的表现拉赞助"
        "为此校长恳求经营专业的你出手拉起乐队"
        "看在小时候照顾你的份上，你勉为其难的答应了她，就这样开始了你的探索"
        "学院一直有组乐队的传统，但上一届的乐队《WHITE ALBUM》由于荒诞的白学原因解散了"
    jump firstOne

label firstOne:
    scene cafe
    "这是历史悠久的角川艺术学院旁的一处咖啡馆"
    "你却与这所学校的校长相对而坐"
    show mizi normal at center
    with dissolve
    mizi "
    所以你就帮帮忙吧，我可爱的弟弟
    "
    show mizi normal:
        function wiggleFuncX
    mizi "
    如果我们能在那场Live中出演，我们学校就有可能得到一大笔赞助的！
    "
    "面对这个装可爱的老女人你感到无奈，因为她是你姐姐的好朋友，而你又从小受她照顾"
    menu:
        "我说，阿姨，你怎么让一个根本没接触过的人去干这件事啊":
            jump choice
        "做不到，而且请不要恶意卖萌":
            jump choice
    label choice:
        show mizi normal:
            function wiggleFuncY
        mizi "好的，就这样说定了"
        "她自顾自地决定了"
        mizi "加油哦，我相信你可以做到的！给你一切需要的权利哦"
        hide mizi
        with dissolve
        menu:
            "拜托，这是现实世界，不要学番剧里那些倒霉蛋啊！":
                "就这样，你的乐队之旅正式开始"
    jump firstTwo
    
label firstTwo:
    scene waijin with fade
    """
    WHITE ALBUM，白色相簿，前一个乐队的名字多奇怪

    你感慨着，走在过道上
    """
    nike "NikeNikeNi!"
    """
    听到这熟悉的口头禅，你眼前一亮

    毕竟对你来说，那从小听到大的活泼的声音过于熟悉
    """
    show nike normal with dissolve
    nike "姑姑真是的，又莫名其妙地把事交给你做"
    nike "所以乐队是什么啊，是什么奇怪的组织吗？"
    menu:
        "举个例子，是四个颜色的女孩子聚在一起进行奇幻冒险的地方！":
            jump .choice1A
        "举个例子，是’爱生活，艳阳天”百合花盛开的命定之地！":
            jump .choice1B
    label .choice1A:
        show nike normal:
            function happyShake
        nike "好哎，是大冒险！"
        
        "妮可兴致勃勃，但又一下子有些犹豫"
        show nike kunhuo:
            function wiggleFuncX
        "我以前没接触过乐队，我不知道我能不能做好"
        menu:
            "怎么不行？你的声音简直是天籁！":
                jump .choice2A
            "没有关系，我会陪着你一起彩彩修车的！":
                jump .choice2B
    label .choice1B:
        show nike kunhuo:
            function wiggleFuncX
        nike "感觉不是很懂的样子"
        hide nike with dissolve
        "她拒绝了你的邀请，你找了另一个人做主唱"
        jump firstThree
    label .choice2A:
        show nike normal:
            function happyShake
        nike "嘿嘿，那看来主唱一定是我妮可了"
        $ firstStoryScore += 1
        hide nike with dissolve
        jump firstThree
    label .choice2B:
        show nike zhihui:
            function wiggleFuncX
        nike "我不明白我不明白我不明白，不要讲怪话！"
        hide nike with dissolve
        "攻略失败，你找了别人当主唱"
        jump firstThree

label firstThree:
    scene bianlidian
    with fade
    show jieyi normal
    with dissolve
    jieyi "可不要觉得我有妮可那样好说话！"
    "你在便利店找到了她，她穿着工作服脸色阴沉"
    jieyi "怎么，你也想像那个自以为是的人一样，上演“你怎么那么熟练啊”的戏码,然后又伤害其他人的梦想吗？"
    show jieyi normal:
        function wiggleFuncY
    jieyi xishuzuie """{size=+10}{color=#f00}他们的罪恶，我甚至不屑于细数{/color}{/size}
    \n此处谨慎选择
    """
    menu:
        "我才不会让乐队里有不可能的三角，真爱的力量才是无穷的啊！":
            jump .choice1A
        "就算我想打成员的主意，手段也不会那么低劣，何况我根本没兴趣":
            jump .choice1B
    label .choice1A:
        "她怔住了，旋即哈哈大笑"
        show jieyi daxiao:
            function wiggleFuncX
        jieyi "好久没有人让我发笑了"
        jieyi "能说服我的话，我就听你安排"
        menu:
            "结衣小姐，你也不想你妹妹为学费操劳吧，参加乐队的话能得到学校的补贴哦？":
                jump .choice2B
            "结衣小姐，你也不希望你妹妹得不到奖学金评优吧，我可以直接干预哦？":
                jump .choice2A
    label .choice1B:
        show jieyi lengxiao
        "她冷冷一笑"
        show jieyi lengxiao:
            function wiggleFuncX
        jieyi "算了吧，我还是没有兴趣"
        "拒绝加入，攻略失败"
        jump firstFive
    label .choice2A:
        show jieyi normal:
            function wiggleFuncX
        jieyi """
        的确对我有威慑力
        """
        show jieyi lengxiao
        jieyi"""
        但是，我拒绝！だが、断る，我可不想因为这点事约束妹妹的自由
        """
        """
        她冷冷说到

        角色攻略失败，你找了别的贝斯手
        """
        jump firstFive
    label .choice2B:
        show jieyi normal:
            function wiggleFuncY
        jieyi "额，也不是不行，那就陪你们跑一圈吧"
        jieyi "但你要是想整什么幺蛾子，或者打我妹的主意，后果自负"
        $ firstStoryScore += 1
        jump firstFour

label firstFour:
    scene room
    with fade
    """
    你还在做准备，却响起了敲门声

    在你的答复下，一个意料之外的人出现了
    """
    show yin normal with dissolve
    yin "贵安，我，我是春日结衣的妹妹，我听，听说了姐姐加入…"
    show yin normal:
        function happyShake
    yin "然后我也想加入！不过我，我想问个事"
    yin "就是上,上届..”WHITE ALBUM“的队长和前辈们"
    show yin ku:
        function wiggleFuncX
    yin "为什么就那样不辞而别啊！"
    menu:
        "也许只是他们间的感情纠纷，然后只能将乐队不了了之吧":
            jump .choice1A
        "也许是到各奔前程的时候，却又不想和影你说再见吧":
            jump .choice1B
    label .choice1A:
        show yin xiaozhengzhu:
            function wiggleFuncX
        yin "真的，就是这样吗？明明大家那么努力啊！怎么就…"
        "看着哭泣的少女，你不禁轻轻握住她的手"
        menu:
            "我能向你保证，绝不会再让你的眼泪为此而流":
                jump .choice2A
            "我能向你保证，绝不会再让新乐队重复旧乐队的乐章！":
                jump .choice2B
    label .choice1B:
        show yin ku:
            function wiggleFuncX
        yin "你在撒谎，和姐姐一样！"
        hide yin with dissolve
        "影哭着跑了出去，攻略失败"
        jump firstFive
    label .choice2A:
        show yin ku:
            function happyShake
        yin "啊，不要，不要这样"
        hide yin with dissolve
        "春日影冲出办公室，然后当晚你就被不知名的吉他英雄用吉他打进住院部"
        jump willEnd
    label .choice2B:
        yin "真，真的吗？那我相信你"
        show yin normal:
            function happyShake
        "她触电般抽回了手"
        show yin jidong:
            function wiggleFuncX
        yin "但请你，至少这一次，不要让大家不辞而别"
        hide yin with dissolve
        scene black with fade
        show jingao at truecenter
        "然后当晚你就收到了春日结衣“不要对我妹动手脚”的警告短信"
        $ firstStoryScore += 1
        jump firstFive

label firstFive:
    show classroom
    with fade
    """
    按照其他同学的指引，你推开了一间空教室的门

    里面只有一位戴着眼镜的少女安静地看着书，桌子上还有两本书

    一本是《源氏物语》，一本是《夜叉池》
    """
    show hua normal with dissolve
    hua "怎么，来这里搅乱我的安宁吗？"
    hua "我知道你的来意，但看见了”WHITE ALBUM” 的荒诞剧，我可没有兴趣"
    menu:
        "敲钟的承诺我将信守，不会再让洪波翻涌":
            jump .choice1B
        "怎么会再有人像那光华公子，随意换取薄幸名":
            jump .choice1A
    label .choice1A:
        show hua chaoxiao:
            function wiggleFuncX
        hua "呵呵，源氏的话，那还是不要相信的好"
        hide hua with dissolve
        "她拒绝了你的邀请，攻略失败，你找了其他贝斯手"
        jump firstSix
    label .choice1B:
        show hua weixiao:
            function wiggleFuncX
        hua "你愿坚守原则的话，龙姬也不会奈何良辰美景"
        hua "但假如我这样呢？"
        show classroom:
            function crazyBg
        show hua normal:
            function crazy
        hua "哈哈 ，wyyyyyyyyyyyyyyyyyyyyyyyyyyy!"
        "就突然间，她散开头发，拿起贝斯就是一阵吊诡的华丽电音"
        menu:
            "疯批美人最爱了，我真是high到不行啊！":
                show classroom:
                    function notcrazy
                show hua normal:
                    function notcrazy
                jump .choice2A
            "人类什么还是不做了，让我们一起疯狂吧，唉以呀咿呀……":
                show classroom:
                    function notcrazy
                show hua normal:
                    function notcrazy
                jump .choice2B
    label .choice2A:
        show hua haixiu:
            function wiggleFuncX
        hua "啊，你在讲什么？有没有病啊？"
        hua "不许再讲类似的话，否则我可要改主意了！"
        $ firstStoryScore += 1
        jump firstSix
    label .choice2B:
        hua "emm,我还没那么病重，你还是去宛平路看看吧"
        "攻略失败，你找了别的贝斯手"
        jump firstSix

label firstSix:
    show cafe with fade
    "周末，你在同一个咖啡馆将进展汇报给校长"
    show mizi normal with dissolve
    show mizi normal:
        function happyShake
    mizi "我就知道，我可爱的弟弟能做到一切！"
    mizi "不过，假如你累或者不愿意，就和姐姐讲好吗？"
    show mizi normal:
        function wiggleFuncX
    mizi "虽然我还是很想你继续带领乐队，因为大家都很认可你"
    menu:
        "大丈夫，能为姐姐分忧我很高兴！":
            jump .choice1A
        "我可以继续管理乐队，但也不是无条件的！":
            jump .choice1B
    label .choice1A:
        mizi "呵呵，小嘴真甜，可不要去拿去骗妮可哦！"
        hide mizi with dissolve
        "之后，你找了别的鼓手"
        jump firstSeven
    label .choice1B:
        show mizi jinya
        mizi "这可是你第一次对姐姐开的价不满足啊"
        show mizi normal:
            function wiggleFuncX
        mizi "那你还想要什么？不会是想打我的主意吧？"
        menu:
            "请校长大人以鼓手身份加入我们乐队吧！":
                jump .choice2A
    label .choice2A:
        pause(0.2)
        menu:
            "我就想听到那熟悉的鼓声，也不想让你的梦消散于黄昏":
                jump .choice3A
            "我们乐队就需要一位经验丰富的鼓手，何况你其实一直在练习吧！":
                jump .choice3B

    label .choice3A:
        show mizi jinya:
            function wiggleFuncX
        mizi "你说的是真的吗？不要骗我哦"
        show mizi haixiu:
            function happyShake
        mizi "那姐姐我就燃烧心火，再陪你们塔塔开一回！"
        mizi "不过，你要对你说过的话负责哦！"
        scene black
        with dissolve
        "呀咧呀咧，都要我负责什么啊？"
        $ firstStoryScore += 1
        jump firstSeven
    
    label .choice3B:
        hide mizi with dissolve
        "到这你还选这个选项，算了吧朋友，游戏结束"
        jump willEnd

label firstSeven: # 结局
    scene black with fade
    if firstStoryScore == 5:
        jump .goodEnd
    else:
        jump .normalEnd

    label .goodEnd:
        """
        经过几个月的训练，你们在接下来的音乐节演出中饱受好评，并一炮走红

        不过在几张专辑与年余的活跃后，你们还是出于工作和学业的原因解散了乐队
        """
        scene waijin with fade
        "妮可时常会拉你上号启动。"
        scene classroom with fade
        "
        而泉镜花却出人意料去研究古典乐了。
        "
        scene bianlidian with fade
        """
        影和结衣的学费被学校免除了，两个人对你与学校都很感激。

        但你还是会时常收到结衣的警告短信“可别欺负我妹”

        她不知道的是，每次影来找你，都会被班上女孩子疼爱地包围，你都凑不过去。
        """
        scene cafe with fade
        """
        不过有一点没有改变，

        就是每个周六，你总会在下午陪弥子喝咖啡，听她吐槽工作上的事。

        这是自你离开家乡来到这座城市后，

        弥子每周都一定要做的事，谁叫她照顾你习惯了呢？

        终
        """
        jump willEnd
    label .normalEnd:
        """
        经过几个月的训练，你们在接下来的音乐节演出中饱受好评，并一炮走红

        不过在几张专辑与年余的活跃后，你们还是出于工作和学业的原因解散了乐队
        """
        
        scene cafe with fade
        """
        不过有一点没有改变，

        就是每个周六，你总会在下午陪弥子喝咖啡，听她吐槽工作上的事。

        这是自你离开家乡来到这座城市后，

        弥子每周都一定要做的事，谁叫她照顾你习惯了呢？

        终
        """
        jump willEnd

label onSecondStoryWillEnd:
    menu:
        "{color=#000}重新开始{/color}":
            jump start
label secondStory:
    scene black with fade
    """
    秋风渐起，一年一度的全国剑道大赛又将开始了。

    为此你所在高中的剑道部的成员们正在热火朝天地进行特训。

    正当大家纷纷议论部内的王牌选手——泽野雏菊学姐会有什么样的训练计划时，

    她却指定你为她的陪练对象。

    虽然你们私下交情不错，但这能成为她当众指名你的理由吗？

    抱着这样的疑问，你与她进行了数次对练。终于，在一个日光和煦的下午......
    """
    jump secondStart
label secondStart:
    scene daochang at truecenter with fade
    show xuejie normal with dissolve
    "剑道训练馆内，你和泽野学姐手握竹剑对峙着"
    "经过一轮节奏明快的攻防，你再一次败下阵来。相互鞠躬后——"
    menu:
        "没问题，再来一次吧":
            jump secondAlpha1
        "学姐，还要训练哦，休息一下好不好啦":
            jump secondAlpha2

label secondAlpha1:
    show xuejie normal:
        function wiggleFuncY
    zeyeju "好的，那么拜托了"
    "又一轮激烈的对攻。泽野学姐最终还是打败了你"
    show xuejie biyan
    "但你也让她冒了一次冷汗，相互鞠躬后，学姐脱下头盔"
    show xuejie normal
    zeyeju "有点累了吧，要不要休息一下"
    menu:
        "再来一次，爷们要战斗！":
            jump secondBeta1
        "既然学姐这么说了，训练就暂停一下吧":
            jump secondBeta2
label secondAlpha2:
    show xuejie normal:
        function wiggleFuncY
    zeyeju "那么，今天就到此为止吧"
    """
    学姐放下装备，收拾好东西后便与你告别了
    """
    hide xuejie with dissolve
    scene black with fade
    """
    走在回家的路上时，你想起青梅竹马的邻家少女笹川春说过会来你家帮忙准备晚餐

    果然，推开屋门的一刹那，饭菜的香味扑面而来
    """
    scene fanzhuo with fade
    show qinmei with dissolve
    tichuanchun "你可算回来了！今天我做的饭菜怎么样？"
    menu:
        "看起来不错":
            jump .choice1
        "应该挺好吃的":
            jump .choice1
    label .choice1:
        show qinmei:
            function wiggleFuncY
        tichuanchun """
        感觉你有些疲惫，是因为剑道训练吗？
        
        在谈论什么热血啊羁绊啊之类的东西前，我觉得你更应该先照顾好自己的身体啊
        """
        menu:
            "有没有一种可能，其实我现在状态非常不错？":
                jump secondGamma11
            "春酱，你还是一如既往地体贴呢。一直以来真是谢谢你的照顾了":
                jump secondGamma12

label secondBeta1:
    show xuejie normal:
        function wiggleFuncX
    zeyeju "没想到你这么有干劲......好吧"
    "这一次，你的身体和反应速度渐渐跟上了学姐"
    "就在你以为要取得胜利之时，她的竹剑却先一步击中了你"
    menu:
        "就快达到了...那种境界......我就快领悟了！":
            jump secondOmega
        "......那今天就到此为止吧":
            jump secondAlpha2
label secondBeta2:
    zeyeju "今天也辛苦你了~"
    """
    泽野学姐放下竹剑，轻盈地向前小跑三两步推开训练馆的落地窗
    
    然后坐在门外台阶上晃荡着双腿，解开马尾辫任由秀发在风中飘扬
    
    她似乎若有所思地望着远处，你凑近一看，发现她正注视着院子里的一丛雏菊。
    """
    show xuejie normal:
        function wiggleFuncY
    zeyeju "对了，应该要好好犒劳一下如此努力的后辈呢"
    menu:
        "谢谢学姐！不过奶茶我只喝星芋啵啵的哦":
            jump secondThgema
        "学姐太客气了，这种小事不劳您费心":
            jump secondAlpha2

label secondGamma11:
    show qinmei:
        function wiggleFuncX
    tichuanchun "......我明白了"
    scene black with fade
    """
    之后的日子里，你照例担任陪练，直到全国大赛开始。最终泽野学姐拿下了冠军。

    什么，你想问后来的故事怎么样了？

    无事发生，不过是毫无高光的日常罢了。

    没错，无 事 发 生 哦——
    """
    jump secondEnd2
label secondGamma12:
    show qinmei:
        function wiggleFuncX
    tichuanchun "突、突然间说什么呢！快点吃饭啦......不过，你这样说我真的很开心~"
    scene black with fade
    """
    之后的日子里，你照例担任陪练，而春酱则仍会时不时“借用”你家的厨房
    """
    scene saichang with fade
    """
    全国大赛开始之际，春主动提出要陪同你前去观赛，于是你们肩并肩坐在观众席上看完了泽野学姐的所有比赛

    最终，学姐拿下了冠军。

    赛后，你向学姐祝贺，她却看着你身边的春
    """
    show xuejie normal at left
    show qinmei at right
    with dissolve
    zeyeju "你们俩关系真好呢，不会是情侣吧？"
    hide xuejie
    show qinmei at center
    with dissolve
    """
    春害羞地躲到你身后，你只能无奈地笑笑。

    和学姐道别后，春拉了拉你的衣角。你扭过头，发现她正努力藏住嘴角的微笑
    """
    show qinmei at center:
        function wiggleFuncX
    tichuanchun "那个......今晚，我再做些好吃的给你吧"
    jump secondEnd3

label secondTheta1:
    show qinmei:
        function wiggleFuncX
    tichuanchun "是嘛，你们都喜欢这样自说自话啊。别人不理解就显得自己追求的所谓理想更酷了吗？"
    tichuanchun "但我就是不明白啊！"
    "结果晚饭时间就在一片沉默之中度过了"
    call secondDabisai
    jump secondEnd4

label secondDabisai:
    scene saichang with fade
    """
    全国大赛如期而至，你前去观看了泽野学姐的比赛。她一路打败强敌，如愿斩获冠军。

    赛后，你站在场馆外，远远地看见她张开双臂向你小跑过来。你伸出手顺势抱住了她。
    """
    show xuejie normal with dissolve
    zeyeju "唉唉，我可是好不容易才从媒体和观众之中脱身出来啊。大家可真是盛情难却"
    "学姐握住了你的手"
    show xuejie lianhong:
        function wiggleFuncX
    zeyeju "还记得我之前在训练场和你的约定吗？其实嘛......"
    show xuejie lianhong:
        function wiggleFuncX
    zeyeju "我是想说，呃"
    show xuejie biyan:
        function happyShake
    zeyeju "其实我一直......"
    show xuejie lianhong:
        function happyShake
    zeyeju "对你......"
    "你不言语，只是温柔地注视着她"
    show xuejie biyan:
        function happyShake
    zeyeju "意思都这么明显了还要等我说完吗？"
    show xuejie normal:
        function wiggleFuncX
    "她忍不住笑出声来"
    show xuejie lianhong:
        function wiggleFuncY
    zeyeju ".....你这个坏蛋！"
    return
label secondTheta2:
    tichuanchun "知道就好啦，饿了吧？来来，快吃饭"
    "少女连忙拉着你入座了"
    call secondDabisai
    jump secondEnd5

label secondThgema:
    zeyeju "很遗憾，现在喝奶茶的话训练就前功尽弃了呢"
    "学姐笑出声来，右手轻叩身边的空位"
    show xuejie normal:
        function happyShake
    zeyeju "所以我准备了别的惊喜。来来，坐在我旁边吧"
    "你照做了。在你坐下的那一刻，她顺势扶住你的肩膀，在你反应过来之前轻巧地将你的头枕在了她的腿上。"
    show xuejie lianhong:
        function wiggleFuncY
    zeyeju "怎么样，偶尔这样这不错吧？不过我今天腿有点累了，没法给你躺真正的膝枕真是不好意思呢......"
    "学姐的声音越来越小了。你抬起头，发现她似乎在努力维持一副漫不经心的表情。为了打破无言的尴尬，还是说点什么好了"
    menu:
        "学姐，你在看什么？":
            jump .choice1
    label .choice1:
        show xuejie lianhong:
            function wiggleFuncX
        zeyeju "......哦哦！我在看......那丛菊花"
        zeyeju "你看，她在风中摇曳，说不定是在担心明天会不会更冷呢"
        menu:
            "但是，她会克服心中的恐惧去迎接寒风，无论结果如何":
                jump .choice2

    label .choice2:
        zeyeju "也是呢"
        "学姐低下头，目光深沉地看着你"
        show xuejie biyan:
            function wiggleFuncX
        zeyeju "其实我还有些话想告诉你，但果然还是等到全国大赛后再说吧！"
        show xuejie normal
        zeyeju "我们来做个约定，届时还请务必亲眼见证......我的决意哦"
        hide xuejie with dissolve
        scene black with fade
        """
        和学姐道别后，你想起青梅竹马的邻家少女笹川春说过会来你家帮忙准备晚餐
        
        于是加快了脚步。果然，推开屋门的一刹那，饭菜的香味扑面而来。
        """
        scene fanzhuo with fade
        show qinmei with dissolve
        tichuanchun "呀，你怎么这么晚才回来？发生什么事了吗？"
        menu:
            "学姐今日似乎非常有兴致":
                jump .choice3
    label .choice3:
        tichuanchun "是这样啊。唉，真是搞不明白你们这些人，明明比起训练，还是记得好好吃饭对身体更好嘛"
        menu:
            "没事，你也不必勉强自己去搞明白":
                jump secondTheta1
            "谢谢你一直作为朋友帮助这样任性的我":
                jump secondTheta2

label secondOmega:
    """
    为了求胜，这次你打算试试不一样的战术。
    
    你以街头搏斗般拼命的姿势狂舞挥打。
    """
    show xuejie normal:
        function happyShake
    """
    学姐显然有点吓到了，你精准地抓住了那措手不及的一瞬将她击败。

    你能感觉到，这些日子的训练让你产生了质变：
    """
    "泽野学姐，普通的剑道是有极限的......所以，我不做普通剑道部员啦！！！"

    zeyeju "你在说什么？总之今天先解散吧。"
    hide xuejie with dissolve
    scene feiqi with fade
    """
    和她分别后，你并没有回家，而是拐进了一条通往废弃厂房的小道。

    第二天，新闻栏目刊登了聚集在某厂房中的小混混被一名疑似高中生的青年尽数击倒的报道。

    你的心中毫无波澜，因为你知道，这只是你成为影之实力者的第一步。
    """
    jump secondEnd1

# 结局们
label secondEnd1:
    scene black with fade
    "达成结局“独孤求败”，获得2个印章"
    jump onSecondStoryWillEnd
label secondEnd2:
    scene black with fade
    "达成结局“我就喜欢孤寡”，获得1个印章"
    jump onSecondStoryWillEnd
label secondEnd3:
    scene black with fade
    "达成结局“我就喜欢青梅”，获得3个印章"
    jump onSecondStoryWillEnd
label secondEnd4:
    scene black with fade
    "达成结局“微微酸涩的青春”，获得4个印章"
    jump onSecondStoryWillEnd
label secondEnd5:
    scene black with fade
    """
    后来，每当你和雏菊并肩而坐，互相依偎的时候
    你总是会想起那个枕在她腿上，远远望着那丛盛放的菊，任凭秋风轻拂的下午
    """
    "达成结局“满溢甜蜜的青春”，获得5个印章"
    jump onSecondStoryWillEnd

label onThirdStoryWillEnd:
    scene black with fade
    "游戏结束，你获得[thirdStoryScore]分"
    menu:
        "{color=#000}重新开始{/color}":
            jump start
label thirdStory:
    scene black with fade
    weizhiren "异世界勇者，睁开眼睛，我是沙芙林"
    show akuyakaichang at truecenter with dissolve
    ni "这里是……?"
    shafulin "我是异世界女神，负责引导像你这样被大卡车创飞到异世界的勇者"
    ni "啊？哦"
    "(感觉她看起来更像社畜)"
    hide akuyakaichang
    show akuyachaofeng at top
    shafulin "想不想体验在异世界开后宫啊？被各种各样的戳你xp的帅哥美女们包围着"
    show akuyachaofeng at top:
        function wiggleFuncX
    shafulin "这当然是不可能的，想想就行了。这里是冒险类异世界，不是恋爱类的"
    "(她刚刚是不是说了什么不得了的话?) "
    hide akuyachaofeng
    show akuyaxiao at top
    shafulin "不用奇怪，我知道自己是纸片人。总之，开始冒险吧"
    jump thirdStoryFirst
label thirdStoryFirst:
    scene black with fade
    show zhaohuanzheng at truecenter
    shafulin "我打算给你召唤一个可爱的伙伴"
    hide zhaohuanzheng
    show zhaohuanzheng2 at truecenter
    "在光污染程度的特效闪过后，你看到有个拿剑的女性和一个有着双马尾(?)的粉白不明飞行物出现了"
    hide zhaohuanzheng2
    show zhaohuanzhengjianyin at truecenter
    buzhimingnvshi "你就是我的Master吗"
    shafulin "好了，让伙伴跟着你一起出发吧"
    ni "(嗯……她说了只有一个伙伴来着)"
    menu:
        "选择帅气的英灵":
            hide zhaohuanzhengjianyin
            jump .choice1
        "选择可爱(?)的不明生物":
            hide zhaohuanzhengjianyin
            jump .choice2
            
    label .choice1:
        show saber at truecenter
        weizhiren "喂!Saber，在这里"
        "一个橘色刺猬头少年打断了你，向金发英灵招手"
        show saber at truecenter:
            function wiggleFuncX
        "被称呼为Saber的女士意识到认错了人，向你们道了歉，离开了"
        jump thirdStorySecond
    label .choice2:
        show xiaoyuan at truecenter
        $ thirdStoryScore += 1
        "要和我签订契约成为魔法少女吗？"
        ni "(感到一阵恶寒)"
        show falao at truecenter
        shafulin "damiedayo～damieyo～damiedalou～吉祥物不要做多余的事情"
        jump thirdStorySecond

label thirdStorySecond:
    scene black with fade
    show sirenzukaichang at truecenter with dissolve 
    "一群人气势汹汹地向你跑来"
    shafulin "啊，你被主角团找麻烦了。不推荐恋战哦，不过打败他们会有隐藏奖励"
    hide sirenzukaichang
    show sirenzunanzhu at truecenter  
    ni "等等，为什么剧情之间一点联系都没有?"
    shafulin "因为我们是单元剧"
    ni "?"
    menu:
        "想办法牵制住他们然后逃跑吧":
            hide sirenzunanzhu
            jump .choice1
        "笑死，他们现在都是菜鸡，根本不怕":
            hide sirenzunanzhu
            jump .choice2
    label .choice1:
        $ thirdStoryScore += 1
        "你们花了点力气离开了。沙芙林告诉你，虽然他们很弱，但会有『机械降神』帮助他们"
        jump thirdStoryThird
    label .choice2:
        show rexuesirenzu at top with dissolve
        "你很轻松地打败了他们。但他们突然大喊着什么友谊啊，羁绊啊之类的话，满血复活，战力飙升，把你揍了一顿"
        jump thirdStoryThird
label thirdStoryThird:
    scene black with fade
    weizhiren "拯救世界的勇者呦……你怎么这么狼狈?跟人打架了？"
    show maoniang at truecenter with dissolve
    weizhiren "总之，我是公主，给你送东西的"
    ni "呃……你是男的吧"
    shafulin "不错啊，你竟然能看出来。他是我的同事，叫秀吉"
    hide maoniang
    show xiuji at truecenter:
        function wiggleFuncX
    xiuji "公主NPC出bug了嘛，只能我暂时代班喽。别介意，这个奖章免费送给你"
    menu:
        "是奖励关卡吗？":
            jump .choice1
        "是奖励关卡吧":
            jump .choice1
    label .choice1:
        $ thirdStoryScore += 1
        show shafulintan at truecenter with dissolve
        shafulin "没错，是保底关哦，有人全选了错误选项就不好了"
        jump thirdStoryFourth
label thirdStoryFourth:
    scene black with fade
    show xiuxi at truecenter with dissolve
    shafulin "魔王大殿的钥匙放在花盆下面了，你自己去拿吧，我休息一会儿"
    hide xiuxi with dissolve
    "刚靠近一看就不对劲的温室，一个一看就更不对劲的戴眼镜的小学生就冒了出来"
    show kenan at truecenter with dissolve
    kenan "啊咧咧，明明很久都没人照顾了，却还有两盆植物活着，这是怎么回事呢？"
    ni "(好熟悉，感觉这个小学生在的地方都会发生什么不好的事情)"
    shafulin "虽然是推理关，但你是从哪里冒出来的啊？根本不是这个世界的角色吧!"
    ni "唔姆，不管了，选一个吧"
    menu:
        "捕蝇草":
            hide kenan with dissolve
            jump .choice1
        "牵牛花":
            hide kenan with dissolve
            jump .choice2
    label .choice1:
        show yaoshi at truecenter with dissolve
        $ thirdStoryScore += 1
        "你拿到了大殿钥匙，准备离开时发现那个死神小学生已经不见了"
        "相比于此，为什么大殿钥匙会放在这么简陋的地方，才是你最感到疑惑的"
        jump thirdStoryFifth
    label .choice2:
        show chusheng at truecenter with dissolve
        "在你碰到牵牛花的那一刻，牵牛花化成了藤蔓向你袭来"
        "沙芙林先藤蔓一步，将你们两个传送走，成功避免了本子剧情"
        shafulin "你是baka吗？牵牛花这种，没办法通过捕食获得额外营养的植物，怎么可能会在花盆里活很久啊？！是陷阱，陷阱! "
        jump thirdStoryFifth

label thirdStoryFifth:
    scene black with fade
    "你们进入了魔王大殿。如同在等待着什么一样，魔王自王座起身"
    show wumu at truecenter with dissolve
    "来到你们面前。她有些扭捏，又或是害羞。你没有立刻攻击她"
    mowang "你，你们好!那个……虽然有些不好意思……我从勇者来到这个世界的第一刻就在关注了"
    mowang "后知后觉地意识到，我，我可能是一见钟情了，能给我个机会吗？"
    ni "?"
    menu:
        "不可以，这是冒险世界":
            jump .choice1
        "为什么不呢?让我们互相了解对方吧":
            jump .choice2
    label .choice1:
        show wumu yichang at truecenter with dissolve
        $ thirdStoryScore += 1
        "你们直接开打了。令人意外的是，你的攻击打到魔王身上的那一刻，她就迫不及待地躺到了地上"
        "女神阻止了打算补刀的你。魔王随后起身，摆了摆手，下班了"
        jump thirdStoryJieWei
    label .choice2:
        show wumu jingya at truecenter with dissolve
        mowang "真的假的？你是好奇选这个选项会发生什么吗？还是说…… "
        "她以为你是诚哥类的人，扇了你一巴掌，然后火速飞走了"
        jump thirdStoryJieWei
label thirdStoryJieWei:
    scene black with fade
    shafulin "结束了"
    shafulin "你要进行下一个游戏了吧？那么，再见。希望你还能继续喜欢着二次元的世界"
    jump onThirdStoryWillEnd
label willEasterEggEnd:
    scene black with fade
    menu:
        "{color=#000}重新开始{/color}":
            jump start
label easterEgg:
    $ thisAuthor = authorNames[-1]
    define author = Character("[thisAuthor]", color="#371da0")
    scene black
    show vscode at truecenter
    with dissolve 
    weizhiren """
    debugger;

    呃呃呃呃 这是一个什么神奇bug

    嗯？

    你是怎么进到debug模式来的，开了吗
    """
    menu:
        "这就默认我开了嘛":
            weizhiren """
            嘛估计就是程序出了一点BUG嘛，不要介意

            作为补偿，你想要去哪个游戏，我直接帮你跳转，就不用随机数了
            """
            menu:
                "第一个游戏":
                    $ thirdStoryScore = 0
                    jump firstStory
                "第二个游戏":
                    jump secondStory
                "第三个游戏":
                    $ thirdStoryScore = 0
                    jump thirdStory
        "事随机数后数组越界了罢":
            jump .choice1

    label .choice1:
        weizhiren """
        哦？我看看，好像是这样的

        我们这个游戏只有三个剧本，看来是game3把你传到这里来了，
        
        不过这个程序没崩溃也是奇怪，我当你是有缘人陪你聊聊罢
        """

        author """
        自我介绍一下，我叫[thisAuthor]，事这个游戏的程序员

        前面三个剧本分别是我们创作部文组的 ByBlack 琥珀 花言斋写的

        大部份图都是我们的图组大佬寰宇做的

        由于各种DDL我几乎就只挤出了一点时间学这个引擎，你能看出我用的是啥引擎做的吗
        """
        menu:
            "那当然是KRKR罢":
                author "啊 KRKR确实挺出名的，不过我用的是Renpy，要问为什么嘛"
                author "没啥为什么，单纯就觉得Renpy挺亲切的"
                author "ok闲聊时间到此为止我作为补偿，你想要去哪个游戏，我直接帮你跳转，就不用随机数了"
                menu:
                    "第一个游戏":
                        $ thirdStoryScore = 0
                        jump firstStory
                    "第二个游戏":
                        jump secondStory
                    "第三个游戏":
                        $ thirdStoryScore = 0
                        jump thirdStory
            "...Renpy?":
                author "哦？你很懂嘛，让我康康"
                jump .choice2
            "感觉不如( )( )":
                author "我知道你想说什么，我这就启动"
                scene yuanshen with fade
                "游戏结束 你获得了1个印章"
                jump willEasterEggEnd
            

    label .choice2:
        menu:
            "废话，我超懂的啦，我超会开发的啦":
                author "来来来 给你看个好康的"
                "你沉浸在开发的世界中无法自拔"
                "游戏结束 你获得了2个印章"
                jump willEasterEggEnd
            "我在想你在开发这个彩蛋剧本的时候是啥感觉":
                jump .choice3
    label .choice3:
        author "当然很奇怪啊，毕竟就像是对着空气输出嘛"
        author "你越来越有趣了，不过确实，数组越界程序不崩溃才是怪事，这个确实是一个彩蛋剧本"
        author "恭喜你触发了彩蛋，不过想要拿满印章还不够哦"
        author "你现在有两个选择"
        menu:
            "拿走4个印章离开":
                author "见好就收是不错的选择"
                "游戏结束 你获得了4个印章"
                jump willEasterEggEnd
            "选择任意的剧本并获得保底的2个印章":
                author "好啊，你选了一个我最难实现的逻辑"
                author "哎呀我也懒得设置变量了，把你旁边的工作人员喊过来，告诉他等会给你加盖两个章"
                menu:
                    "第一个游戏":
                        $ thirdStoryScore = 0
                        jump firstStory
                    "第二个游戏":
                        jump secondStory
                    "第三个游戏":
                        $ thirdStoryScore = 0
                        jump thirdStory
            "easterEggScore = 5":
                jump .choice4
    label .choice4:         
        author "你真的觉得这个可以修改分数嘛，太天...."
        scene black
        author "WOC怎么改成功了"
    menu:
        "characterVoice = false":
            author """
            太天真力，我又不是角色

            游戏结束，看你到了这里我就给你两个印章罢，再见力
            """
            "游戏结束 你获得了2个印章"
            jump willEasterEggEnd
        "authorVoice = false":
            author "唔唔唔,竟然把开发者禁言了，但是开发者的权限是无限大的，想要把我搞下去还是很难的"
            $ minling = ""
            screen entry_name():
                tag menu
                fixed:
                    input:
                        value VariableInputValue("minling")
                        size 35
                        length 20
                        allow None
                        color "#2F4F4F"
                        xpos 499
                        ypos 313
                        pixel_width 500
                        exclude " "                            
                button:   
                    action Return()
            call screen entry_name
            if(minling == "debugger;"):
                jump .choice5
            else:
                author "诶都给你机会自由输入代码了，也没见你能黑进去a，算了，我也懒得写你的流程分支了"
                author "这个剧本的逻辑已经一团糟了，给你三个印章结束罢"
                author "得到三个印章，游戏结束"
                jump willEasterEggEnd

    label .choice5:
        "系统已中断 请修改开发者姓名"
        $ nextName = ""
        screen changeName():
            tag menu
            fixed:
                input:
                    value VariableInputValue("nextName")
                    size 35
                    length 20
                    allow None
                    color "#2F4F4F"
                    xpos 499
                    ypos 313
                    pixel_width 500
                    exclude " "                            
            button:   
                action Return()
        call screen changeName
        "开发者姓名已修改成功，修改历史记录为..."
        python:
            authorNames.append(nextName)
            total = ""
            for value in authorNames:
                if value == nextName:
                    total += value
                else:
                    total += value + "->"
            say("",total)
        
        "游戏结束 你获得了5个印章"
        jump willEasterEggEnd




        

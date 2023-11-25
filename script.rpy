# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define nike = Character("千坂田妮可", color="#d25145", image = "nike")
define jieyi = Character("春日结衣", color="#c5ae27", image = "jieyi")
define yin = Character("春日影", color="#b39a0e")
define hua = Character("泉镜花", color="#6274c4")
define mizi = Character("四月一日弥子", color="#c657e4", image = "mizi")
define ni = Character("你", color="#3c80a2")
# 动作
init python:
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
# 游戏在此开始。

define firstStoryScore = 0

label willEnd:
    scene black with fade
    "游戏结束，你获得[firstStoryScore]分"
    menu:
        "{color=#000}重新开始{/color}":
            jump start
label start:
    $ firstStoryScore = 0
    jump firstStory
    return

label firstStory:
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
        天真活泼双钻头，是静的侄女。
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
        "一所历史悠久的（角川艺术学院）艺术学院需要在某次大型活动中以优异的表现拉赞助"
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
        show nike normal:
            function wiggleFuncX
        "我以前没接触过乐队，我不知道我能不能做好"
        menu:
            "怎么不行？你的声音简直是天籁！":
                jump .choice2A
            "没有关系，我会陪着你一起彩彩修车的！":
                jump .choice2B
    label .choice1B:
        show nike normal:
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
        show nike normal:
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
    jieyi "{size=+10}{color=#f00}他们的罪恶，我甚至不屑于细数{/color}{/size}"
    menu:
        "我才不会让乐队里有不可能的三角，真爱的力量才是无穷的啊！":
            jump .choice1A
        "就算我想打成员的主意，手段也不会那么低劣，何况我根本没兴趣":
            jump .choice1B
    label .choice1A:
        "她怔住了，旋即哈哈大笑"
        show jieyi normal:
            function wiggleFuncX
        jieyi "好久没有人让我发笑了"
        jieyi "能说服我的话，我就听你安排"
        menu:
            "结衣小姐，你也不希望你妹妹得不到奖学金评优吧，我可以直接干预哦？":
                jump .choice2A
            "结衣小姐，你也不想你妹妹为学费操劳吧，参加乐队的话能得到学校的补贴哦？":
                jump .choice2B
    label .choice1B:
        "她冷冷一笑"
        show jieyi normal:
            function wiggleFuncX
        jieyi "算了吧，我还是没有兴趣"
        "拒绝加入，攻略失败"
        jump firstFour
    label .choice2A:
        show jieyi normal:
            function wiggleFuncX
        jieyi """
        确实有我威慑力

        但是，我拒绝！だが、断る，我可不想因为这点事约束妹妹的自由
        """
        """
        她冷冷说到

        角色攻略失败，你找了别的贝斯手
        """
        jump firstFour
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
    show yin normal:
        function wiggleFuncX
    yin "为什么就那样不辞而别啊！"
    menu:
        "也许只是他们间的感情纠纷，然后只能将乐队不了了之吧":
            jump .choice1A
        "也许是到各奔前程的时候，却又不想和影你说再见吧":
            jump .choice1B
    label .choice1A:
        show yin normal:
            function wiggleFuncX
        yin "真的，就是这样吗？明明大家那么努力啊！怎么就…"
        "看着哭泣的少女，你不禁轻轻握住她的手"
        menu:
            "我能向你保证，绝不会再让你的眼泪为此而流":
                jump .choice2A
            "我能向你保证，绝不会再让新乐队重复旧乐队的乐章！":
                jump .choice2B
    label .choice1B:
        show yin normal:
            function wiggleFuncX
        yin "你在撒谎，和姐姐一样！"
        hide yin with dissolve
        "影哭着跑了出去，攻略失败"
        jump firstFive
    label .choice2A:
        show yin normal:
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
        show yin normal:
            function wiggleFuncX
        yin "但请你，至少这一次，不要让大家不辞而别"
        hide yin with dissolve
        scene black with fade
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
        "怎么会再有人像那光华公子，随意换取薄幸名":
            jump .choice1A
        "敲钟的承诺我将信守，不会再让洪波翻涌":
            jump .choice1B
    label .choice1A:
        show hua normal:
            function wiggleFuncX
        hua "呵呵，源氏的话，那还是不要相信的好"
        hide hua with dissolve
        "她拒绝了你的邀请，攻略失败，你找了其他贝斯手"
        jump firstSix
    label .choice1B:
        show hua normal:
            function wiggleFuncX
        hua "你愿坚守原则的话，龙姬也不会奈何良辰美景"
        hua "但假如我这样呢？"
        show classroom:
            function crazyBg
        show hua normal:
            function crazy
        hua "哈哈 ，wyyyyyyyyyyyyyyyyyyyyyyyyyyy!"
        "就突然间，她摘下眼镜，散开头发，拿起贝斯就是一阵吊诡的华丽电音"
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
        hua "啊，你在讲什么？有没有病啊？"
        show hua normal:
            function wiggleFuncX
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
        show mizi normal:
            function wiggleFuncX
        mizi "你说的是真的吗？不要骗我哦"
        show mizi normal:
            function happyShake
        mizi "那姐姐我就燃烧心火，再陪你们塔塔开一回！"
        mizi "不过，你要对你说过的话负责哦！"
        scene black
        show mizi normal
        with dissolve
        show mizi normal:
            function wiggleFuncX
        mizi "呀咧呀咧，都要我负责什么啊？"
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

        妮可时常会拉你上号启动。

        而泉镜花却出人意料去研究古典乐了。

        影和结衣的学费被学校免除了，两个人对你与学校都很感激。

        但你还是会时常收到结衣的警告短信“可别欺负我妹”

        她不知道的是，每次影来找你，都会被班上女孩子疼爱地包围，你都凑不过去。

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

        世事变换，但有一点未曾改变

        就是每个周六，你总会在下午陪弥子喝咖啡，听她吐槽工作上的事。

        这是自你离开家乡来到这座城市后，

        弥子每周都一定要做的事，谁叫她照顾你习惯了呢？
        
        """
        jump willEnd



define pengjingxiang = Character("PJ")
define kouliwen = Character("大司寇")
define jiangyan = Character("蒋老师")

label splashscreen:
    scene black
    with Pause(0.5)

    show text "本游戏剧情根据真实事件改编。" with dissolve
    with Pause(1.5)

    show text "所有登场人物年龄均未满十八岁\n如有雷同，纯属故意。" with dissolve
    with Pause(2)

#    show text "qi" with dissolve

    hide text with dissolve
    with Pause(1)

    return

label start:
##序章的虚序章

    scene black
    "从睡梦中惊醒，我汗流浃背地看着一旁空洞洞的位置。"

    pengjingxiang "原来是梦吗。"
    pengjingxiang "啊……"

    "我向后看了那个位置一眼，她还在认真地听课。"

    """
    她认真的眼神真的很好看,\n
    她身上的一切，都牵动着我的心。
    """

    "为了不影响她的学习，我主动向老师提出了换位置。\n尽管相隔但她依然存在于我内心的最深处。"

    "…………" with dissolve

    "(下课铃声)"
    "这么快就下课了吗？"
    "她这节课需不需要我给她讲题呢？"

    #这里zzy起身离开（去厕所）
    "正好有一会儿空闲时间，"
    "要不要找寇哥吐槽呢？"
    menu:
        "寇哥见识广，可以开导我。":
            jump end1
        "还是算了吧":
            jump chapter_0
    return

label end1:
    "还是找他聊聊吧。"
    pengjingxiang "寇哥。"
    kouliwen "嗯？"

    
    #这句我加的
    "不过，\n似乎有人说寇哥是出名的大嘴巴，他会不会给别人说呢？"

    "寇哥脑袋朝天，戴着校服帽，眼皮尽力地往上拉扯，手中的黑笔还在不断地滑动。"


    ###视角放大向寇哥
    "看起来不太靠谱，到底要不要找他倾诉呢？"
    menu:
        "寇哥看起来很靠谱":
            "我还是觉得寇哥看起来很靠谱，可以问问看。"
        "还是算了吧":
            jump chapter_0
    pengjingxiang "寇哥，我还是忘不了她，怎么办。"
    "寇哥听到我说话，脑袋往右边拧了一下，嘴巴里只蹦出一个字……"
    kouliwen "六。"
    pengjingxiang "大师，我悟了。"
    "……"
    "晚饭后。"
    jiangyan "彭靖翔，你出来一下。"
    "作为班长，蒋老师也是经常叫我出去。"
    pengjingxiang "但是这次似乎有一些不太一样。"
    "看这蒋老师强忍愤怒的眼神，我察觉到了一些异样。"
    "走出了教室，蒋老师正在教室外等着。"
    jiangyan "老实交代，你最近是不是馋人家身子？"
    "蒋老师是怎么知道的？！"
    "不会是寇哥泄露天机了吧？"
    pengjingxiang "没……没有吧。"
    jiangyan "你下贱的眼神被我观察一清二楚。"
    jiangyan "年轻人向往美好是一件很正常的事情，\n但你不要忘记你的初心是什么。"
    jiangyan "这个社会是弱肉强食的，\n你现在的本职工作的是学习，不要想那些有的没的。"
    jiangyan "等哪一天你步入社会你就体会到了。"
    jiangyan "高考的胜利就是给那些能够摒除干扰的人的。"
    jiangyan "而且你身为班级的领头羊，要起表率作用，同学们都追着你的脚步的。" with dissolve
    jiangyan """
    ………………。\n
    ………。
    """
    "蒋老师奚落了我半个小时，从此我一心一意学习，成为了玉林中学第二个理科状元……" with dissolve
    "可喜可贺，可喜可贺。"
    "…………\n才怪！"
    with pixellate
    "触发Bad Ending 1：“现在是幻想时间”"
    
    return

label chapter_0:
    "晚自习"
    
    return


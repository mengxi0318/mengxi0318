'''梦曦の主页'''
import streamlit as st
from PIL import Image
import time
page = st.sidebar.radio('梦曦の首页',["首页","我推的","我的图片处理工具","我的智慧词典","网址导航","音频","题目","我的留言区"])

def page1():
    st.header('欢迎来到我的网站')
    st.image("我的网络根据地/联想截图_20230830030110.png")                                                 
    st.balloons()
    st.write("dragon")

def page2():
    '''推的''' 
    tab1,tab2,tab3,tab4,tab5=st.tabs(["首页","咒术回战","新世纪福音战士","孤独摇滚","原神"])
    with tab1:
        st.header("欢迎来到我的首页")
        st.snow()
        st.write("-------------------------------------------------")
        st.write("进行一段很长的演讲，") 
        st.write("此处省略n个字")
    with tab2:
        st.write("五条悟")
        st.write("-------------------------------------------------")
        st.image("我的网络根据地/五条悟开篇.jpg")
        st.write(":red[术式反转 赫]") 
        st.image("我的网络根据地/术式反转赫1.jpg")
        st.image("我的网络根据地/术式反转赫2.jpg")
        st.image("我的网络根据地/术式反转赫3.jpg")
        st.image("我的网络根据地/术式反转赫4.jpg")
        st.image("我的网络根据地/术式反转赫5.jpg")
        st.image("我的网络根据地/术式反转赫6.jpg")
        st.image("我的网络根据地/术式反转赫7.jpg")
        st.image("我的网络根据地/术式反转赫8.jpg")
        st.image("我的网络根据地/术式反转赫9.jpg")
        st.image("我的网络根据地/术式反转赫10.jpg")
        st.image("我的网络根据地/术式反转赫11.jpg")
        st.image("我的网络根据地/术式反转赫12.jpg")
        '''st.image("我的网络根据地/术式反转赫13.jpg")'''
        st.image("我的网络根据地/术式反转赫14.jpg")
        st.image("我的网络根据地/术式反转赫15.jpg")
        st.image("我的网络根据地/术式反转赫16.jpg")
        st.image("我的网络根据地/术式反转赫17.jpg")
        st.image("我的网络根据地/术式反转赫18.jpg")
        st.image("我的网络根据地/术式反转赫19.jpg")
        st.image("我的网络根据地/术式反转赫20.jpg")
        st.image("我的网络根据地/术式反转赫21.jpg")
        st.image("我的网络根据地/术式反转赫22.jpg")
        st.image("我的网络根据地/术式反转赫23.jpg")
        st.image("我的网络根据地/术式反转赫24.jpg")
        st.image("我的网络根据地/术式反转赫25.jpg")
        st.image("我的网络根据地/术式反转赫26.jpg")
        st.image("我的网络根据地/术式反转赫27.jpg")
        st.image("我的网络根据地/术式反转赫28.jpg")
        st.image("我的网络根据地/术式反转赫29.jpg")
        st.image("我的网络根据地/术式反转赫30.jpg")
        st.image("我的网络根据地/术式反转赫31.jpg")
        st.image("我的网络根据地/术式反转赫32.jpg")
        st.image("我的网络根据地/术式反转赫33.jpg")
        st.image("我的网络根据地/术式反转赫34.jpg")
        st.image("我的网络根据地/术式反转赫35.jpg")
        st.image("我的网络根据地/术式反转赫36.jpg")
        st.image("我的网络根据地/术式反转赫37.jpg")
    with tab3:
        st.write("新世纪福音战士")
        video_file = open('我的网络根据地/EVA.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes) 
    with tab4:
        st.write("孤独摇滚")
        st.write("-------------------------------------------------")
        st.write(":pink[后藤一里(波奇酱)]")
        st.image("我的网络根据地/后藤一里1.jpg")
        st.image("我的网络根据地/后藤一里2.jpg")
        st.image("我的网络根据地/后藤一里3.jpg")
        st.image("我的网络根据地/后藤一里4.jpg")

    with tab5:
        st.write("原神")
        st.write("-------------------------------------------------")
        st.image("我的网络根据地/联想截图_20230929231429.png")
        st.image("我的网络根据地/联想截图_20231004142507.png")
        st.image("我的网络根据地/联想截图_20231004142507.png")
        st.image("我的网络根据地/联想截图_20231004142519.png")
        st.image("我的网络根据地/联想截图_20231004142529.png")
        st.image("我的网络根据地/联想截图_20231004142534.png")
        st.image("我的网络根据地/联想截图_20231004142551.png")
        st.image("我的网络根据地/联想截图_20231004142624.png")
        st.image("我的网络根据地/联想截图_20231004142641.png")
        st.image("我的网络根据地/联想截图_20231004142649.png")
        st.image("我的网络根据地/联想截图_20231004142649.png")
        st.image("我的网络根据地/联想截图_20231004142703.png")
        st.image("我的网络根据地/联想截图_20231004142719.png")
        st.image("我的网络根据地/联想截图_20231004142730.png")
        st.image("我的网络根据地/联想截图_20231004142751.png")
        st.image("我的网络根据地/联想截图_20231004142759.png")
        st.image("我的网络根据地/联想截图_20231004142814.png")
        st.image("我的网络根据地/联想截图_20231004142824.png")
        st.image("我的网络根据地/联想截图_20231004142831.png")
        st.image("我的网络根据地/联想截图_20231004142922.png")
        st.image("我的网络根据地/联想截图_20231004142957.png")
        st.image("我的网络根据地/联想截图_20231004143004.png")
        st.image("我的网络根据地/联想截图_20231004143013.png")
        st.image("我的网络根据地/联想截图_20231004143028.png")

def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height=img.size
    img_array= img.load()
    for x in range(width):
        for y in range(height):
            r =img_array[x,y][rc]
            g =img_array[x,y][gc]
            b =img_array[x,y][bc]
            img_array[x,y]=(r,g,b)
    return img

def page3():
    '''图片处理工具'''
    st.write(":sunglasses:图片处理小程序：sunglasses:")
    uploaded_file=st.file_uploader("上传图片",type=['png','jpeg','jpg'])
    if uploaded_file:
        file_name= uploaded_file.name
        file_type= uploaded_file.type
        file_size= uploaded_file.size
        img=Image.open(uploaded_file)
        st.image(img)
        tab1,tab2,tab3,tab4=st.tabs(["原图","改色1","改色2","改色3"])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
            
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i + 1)
        time.sleep(0.1)
def page4():
    '''智慧词典'''
    st.write('智慧词典')
    with open('我的网络根据地/words_space.txt','r',encoding='utf-8') as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
        with open('我的网络根据地/check_out_times.txt','r',encoding='utf-8')as f:
            times_list=f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i]=times_list[i].split('#')
    times_dict={}
    for i in times_list:
        times_dict[int(i[0])]=int(i[1])
    word=st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n=words_dict[word][0]
        if n in times_dict:
            times_dict[n]+=1
        else:
            times_dict[n]=1
        with open('我的网络根据地/check_out_times.txt','w',encoding='utf-8')as f:
            message =""
            for k,v in times_dict.items():
                message +=str(k)+'#'+str(v)+'\n'
            message=message[:-1]
            f.write(message)
            st.write("查询次数:",times_dict[n])
            if word == "python":
                st.balloons()
            if word == "dragon":
                st.header(":red[Happy Year of the Dragon!!!H]")
                st.header(":red[Happy Year of the Dragon!!!a]")
                st.header(":red[Happy Year of the Dragon!!!p]")
                st.header(":red[Happy Year of the Dragon!!!p]")
                st.header(":red[Happy Year of the Dragon!!!y]")
                st.header(":red[Happy Year of the Dragon!!! ]")
                st.header(":red[Happy Year of the Dragon!!!Y]")
                st.header(":red[Happy Year of the Dragon!!!e]")
                st.header(":red[Happy Year of the Dragon!!!a]")
                st.header(":red[Happy Year of the Dragon!!!r]")
                st.header(":red[Happy Year of the Dragon!!! ]")
                st.header(":red[Happy Year of the Dragon!!!o]")
                st.header(":red[Happy Year of the Dragon!!!f]")
                st.header(":red[Happy Year of the Dragon!!! ]")
                st.header(":red[Happy Year of the Dragon!!!t]")
                st.header(":red[Happy Year of the Dragon!!!h]")
                st.header(":red[Happy Year of the Dragon!!!e]")
                st.header(":red[Happy Year of the Dragon!!! ]")
                st.header(":red[Happy Year of the Dragon!!!D]")
                st.header(":red[Happy Year of the Dragon!!!r]")
                st.header(":red[Happy Year of the Dragon!!!a]")
                st.header(":red[Happy Year of the Dragon!!!g]")
                st.header(":red[Happy Year of the Dragon!!!o]")
                st.header(":red[Happy Year of the Dragon!!!n]")
            
def page5():
    '''网址导航'''
    tab1,tab2,tab3=st.tabs(["基础","进阶","超级"])
    with tab1:
        st.link_button('百度首页','https://www.baidu.com/')
        st.link_button('哔哩哔哩','https://www.bilibili.com/')
        st.link_button('原神','https://ys.mihoyo.com/')
        st.link_button('AmongUs','https://amonguscn.club/')
        st.link_button('图片大全','https://www.gettyimages.com/')
        st.link_button('设计资源','https://www.qijishow.com/')
    with tab2:
        st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
        go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['贴吧', 'bilibili','原神','AmongUs','图片大全','设计资源'])
        if go == '贴吧':
            st.link_button('帮我盖楼,跳转到'+go+"网站", 'https://www.baidu.com/')
        elif go == 'bilibili':
            st.link_button('帮我一键三连,跳转到'+go+"网站", 'https://www.bilibili.com/')
        elif go == '原神':
            st.link_button('支持米哈游,跳转到'+go+"网站", 'https://ys.mihoyo.com/')
        elif go == 'AmongUs':
            st.link_button('AmongUs模组资源网站,跳转到'+go+"网站", 'https://amonguscn.club/')
        elif go == '图片大全':
           st.link_button('全世界最大的图片资源网站,跳转到'+go+"网站", 'https://www.gettyimages.com/')
        elif go == '设计资源':
           st.link_button('设计资源网站,跳转到'+go+"网站", 'https://www.qijishow.com/')
    with tab3:
        st.balloons()
        st.header("你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？")
        st.header("你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？")
        st.header("你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？")
        st.header("你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？")
        st.header("你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？")
        st.header("你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？你在期待什么？")
def page6():
    '''音频'''  
    st.write("-------------------------------------------------")
    tab1,tab2,tab3=st.tabs(["ROG","音乐","经典名言"])
    with tab1:
        st.write("REPUBLIC OF GAMERS")
        video_file = open('我的网络根据地/合成 1.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        with open ("我的网络根据地/ROG开机音效.MP3","rb") as f:
            a = f.read()
        st.audio(a, format="audio/mp3 ",start_time=0)
    with tab2:
        st.write("for ya")
        with open ("我的网络根据地/for ya伴奏.MP3","rb") as f:
            b = f.read()
        st.audio(b, format="audio/mp3 ",start_time=0)
    with tab3:
        st.write("原神玩家的诞生")
        with open ("我的网络根据地/原神玩家的诞生.MP3","rb") as f:
            c = f.read()
        st.audio(c, format="audio/mp3 ",start_time=0)

def page7():
    '''题目'''
    st.header("下列哪个游戏不是   旗下的")
    genre = st.radio(
        "Which of the following games is not owned by miHoYo？",
        ('原神', '崩坏3', '崩坏·星穹铁道','APEX'))
    if genre == 'APEX':
        st.write('你回答对了')
        st.balloons()
    elif genre == '原神':
        st.write('你回答错了')
        st.image("我的网络根据地/联想截图_20230830023935.png")    
    elif genre == '崩坏3':
        st.write('你回答错了')
        st.image("我的网络根据地/联想截图_20230830023946.png")   
    elif genre == '崩坏·星穹铁道':
        st.write('你回答错了')
        st.image("我的网络根据地/联想截图_20230830023941.png")   
    st.write(":white[米哈游]")
        
def page8():
    '''留言区'''
    tab1,tab2=st.tabs(["留言区","签名区"])
    with tab1:
        st.write('我的留言区')
        with open('我的网络根据地/leave_messages.txt','r',encoding='utf-8')as f:
            messages_list=f.read().split('\n')
        for i in range(len(messages_list)):
            messages_list[i]=messages_list[i].split('#')
        for i in messages_list:
            if i[1]=='伊雷娜':
                with st.chat_message("🌞"):
                    st.write(i[1],':',i[2])
            elif i[1]=='绪山真寻':
                with st.chat_message('🍥'):
                    st.write(i[1],':',i[2])
            elif i[1]=='后藤一里':
                with st.chat_message('💯'):
                    st.write(i[1],':',i[2])
        name=st.selectbox('我是......',['伊雷娜','绪山真寻','后藤一里'])
        new_message=st.text_input('想要说的话......')
        if st.button('留言'):
            messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('我的网络根据地/leave_messages.txt','w',encoding='utf-8')as f:
            message =""
            for i in messages_list:
                message+=i[0]+'#'+i[1]+"#"+i[2]+'\n'
            message=message[:-1]
            f.write(message)
    with tab2:   
        st.write("请输入你的昵称")
        title = st.text_input('签名框1', ' ')
        st.write('本次游客的昵称为', title) 
        title = st.text_input('签名框2', ' ')
        st.write('本次游客的昵称为', title) 
        title = st.text_input('签名框3', ' ')
        st.write('本次游客的昵称为', title) 
        title = st.text_input('签名框4', ' ')
        st.write('本次游客的昵称为', title) 
        title = st.text_input('签名框5', ' ')
        st.write('本次游客的昵称为', title) 
        title = st.text_input('签名框6', ' ')
        st.write('本次游客的昵称为', title) 
        title = st.text_input('签名框7', ' ')
        st.write('本次游客的昵称为', title) 
        title = st.text_input('签名框8', ' ')
        st.write('本次游客的昵称为', title) 
        title = st.text_input('签名框9', ' ')
        st.write('本次游客的昵称为', title) 
        title = st.text_input('签名框10', ' ')
        st.write('本次游客的昵称为', title) 
        title = st.text_input('签名框11', ' ')
        st.write('本次游客的昵称为', title) 
        title = st.text_input('签名框12', ' ')
        st.write('本次游客的昵称为', title) 
    
if page == "首页":
    page1() 
if page == "我推的":
    page2()
elif page == "我的图片处理工具":
    page3()
elif page == "我的智慧词典":
    page4()
elif page == "网址导航":
    page5()
elif page == "音频":
    page6()  
elif page == "题目":
    page7()
elif page == "我的留言区":
    page8()

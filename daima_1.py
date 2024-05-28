from langchain.prompts import ChatPromptTemplate
from langchain_wenxin.chat_models import ChatWenxin


def generate_script(name, festival, creativity):

    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             f"""你非常擅长给别人写节日祝福语，根据需要发送祝福的对象和节日，写一段节日祝福语
             姓名：{name}，节日：{festival}，生成的节日祝福格式：
             文本开头要以姓名开头：内容中也要带有输入的姓名，这样收到祝福的人就不会觉得是群发的祝福了。
             祝福内容要真诚，有趣，吸引年轻人。此外，生成的内容要包含输入名字的藏头诗。
             格式参考如下：
             ###
             栋伟：栋材独树千秋茂， 伟业辉煌耀九州。 端午佳节粽飘香， 五福临门喜悠悠。 
             快乐满怀随粽在， 笑语欢歌绕心头。 幸福安康长相伴， 乐享佳节福无休。
             ###
          
        
        
             """)
        ]
    )


    model = ChatWenxin(model="ernie-speed-128k", temperature=creativity,baidu_api_key="Idvexi7giPhjajeswlwjz7uC"
                       ,baidu_secret_key="XVpmwFYDs4rXFdjgAvv9Hz7ewyhNCNlP")


    script_chain = script_template | model


    script = script_chain.invoke({"name": name, "festival": festival,
                               }).content

    return script


#print(generate_script("苹果", 1, 0.7))
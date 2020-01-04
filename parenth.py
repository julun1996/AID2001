# 判断一段文字中，括号匹配是否正确

# 创建栈

class Stack:
    def __init__(self):
        self.__list_value = []

    # 判断栈空
    def is_empty(self):
        return self.__list_value == []

    # 入栈
    def enstack(self, value):
        self.__list_value.append(value)

    # 出栈
    def destack(self):
        if self.is_empty():
            print("stack is empty!")
        else:
            return self.__list_value.pop(len(self.__list_value) - 1)

# 创建一个空栈
st = Stack()
parenths = "{[()]}"
left_parenth = "{[("
dict_parenth = {
        "}": "{",
        "]": "[",
        ")": "("
    }

# 判断文字当中，括号是否匹配正确
def match_parenth(text):
    i = 0
    text_len = len(text)

    while True:
        # 如果索引值没有超过总长度并且遍历的值不是括号---索引加1
        while i < text_len and text[i] not in parenths:
            i += 1
        else:
            if i >= text_len:
                return
            else:
                #如果遍历到左括号
                if text[i] in left_parenth:
                    # 入栈
                    st.enstack((text[i], i))
                    i+=1

                else:  # 找右括号
                    if st.is_empty() or dict_parenth[text[i]] != st.destack()[0]:
                        print("match is error", i)
                        break
                    else:
                        i+=1
def match(text):
    match_parenth(text)
    if not st.is_empty():
        print("match is error,", st.destack()[1])
    else:
        print("match is success!")


text = "(dkmfxxj[kncf]kkd(kc)kcmk})kskc"
match(text)

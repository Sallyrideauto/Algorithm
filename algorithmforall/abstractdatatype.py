# 스택
# 배열의 끝에서만 데이터를 접근할 수 있는 선형 자료구조
# 배열 인덱스 접근이 제한되며, 후입선출(LIFO; Last in First Out) 구조
# 시간 복잡도는 모두 O(1)

# append()와 pop() 메서드로 스택 구현
class Stack(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return not bool(self.items)

    def push(self, value):
        # 스택의 맨 끝(또는 맨 위)에 항목을 삽입
        self.items.append(value)

    def pop(self):
        # 스택의 맨 끝 항목을 반환하는 동시에 제거
        value = self.items.pop()
        if value is not None:
            return value
        else:
            print("Stack ie empty.")

    def size(self):
        # 스택의 크기를 확인
        return len(self.items)

    def peek(self):
        # 스택 맨 끝 항목을 조회
        if self.items:
            return self.items[-1]
        else:
            print("Stack is empty.")

    def __repr__(self):
        return repr(self.items)

if __name__ == "__main__":
    stack = Stack()
    print("스택이 비었나요? {0}".format(stack.isEmpty()))
    print("스택에 숫자 0~9를 추가합니다.")
    for i in range(10):
        stack.push(i)
    print("스택 크기 : {0}".format(stack.size()))
    print("peek: {0}".format(stack.peek()))
    print("pop: {0}".format(stack.pop()))
    print("peek: {0}".format(stack.peek()))
    print("스택이 비었나요? {0}".format(stack.isEmpty()))
    print(stack)
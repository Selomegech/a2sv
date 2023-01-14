class MyQueue {
public:
    stack<int> s1;
    stack<int> s2;
    MyQueue() {
        
    }
    
    void push(int x) {
        while(!s1.empty()) {  //1
            s2.push(s1.top());
            s1.pop();
        }
        s2.push(x);  //2
        while(!s2.empty()) {  //3
            s1.push(s2.top());
            s2.pop();
        }
    }
    
    int pop() {
        int curr = s1.top();
        s1.pop();
        return curr;
    }
    
    int peek() {
        return s1.top();
    }
    
    bool empty() {
        return s1.empty();
    }
};

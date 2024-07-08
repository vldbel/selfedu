class StackObj:
    """для описания объектов односвязного списка;"""

class Stack: 
    """для управления односвязным списком."""
    


st = Stack()
st.push(StackObj("obj1"))
st.push(StackObj("obj2"))
st.push(StackObj("obj3"))
st.pop()
res = st.get_data()    # ['obj1', 'obj2']

from helpers import createLL, Node, visualizeLL

def reverseLL(head):
    if not head or not head.next:
        return {"head": head, "visual": visualizeLL(head)}
    next = None
    trav = head
    prev = None
    while trav and trav.next:
        next = trav.next
        trav.next = prev
        prev = trav
        trav = next
    trav.next = prev
    # print(visualizeLL(trav))
    return {"head": trav, "visual": visualizeLL(trav)}


def reverseLLChecker():
    # print(reverseLL(LL1)['visual'])
    # print(reverseLL(emptyLL)['visual'])
    # print(reverseLL(oneElementLL)['visual'])
    assert reverseLL(LL1)['visual'] == '[6] -->[4] -->[3] -->[2] -->[1] --> None'
    assert reverseLL(emptyLL)['visual'] == 'None'
    assert reverseLL(oneElementLL)['visual'] == '[1] --> None'
    print('Reverse LL Tests Passed!')

if __name__ == "__main__":
    LL1 = createLL([1,2,3,4,6])["head"]
    emptyLL = createLL([])['head']
    oneElementLL = createLL([1])['head']
    reverseLLChecker()
   
   
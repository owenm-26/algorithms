class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None  

def createLL(values):

    prev = Node(0)
    head = prev
    for v in values:
        node = Node(v)
        prev.next = node
        prev = node
    visual = visualizeLL(head)
    return {"head": head.next, "visual": visual}

def visualizeLL(head):
    if not head:
        return 'None'
    trav = head
    visual = [f"[{trav.value}] -->"]
    while trav and trav.next:
        trav = trav.next
        visual.append(f"[{trav.value}] -->")
    return "".join(visual) + " None"
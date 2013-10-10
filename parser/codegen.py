def TraverseTree(tree):
    if tree['terminal']:
        return tree['state']
    children = []
    for elem in tree['children']:
        child = TraverseTree(elem)
        if child == None:
            return None
        children.append(child)
    return tree['rule'].apply(children)

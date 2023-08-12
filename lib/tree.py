class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    stack = []

    stack.append(self.root)

    while len(stack) > 0:
      node = stack.pop()

      if node["id"] == id:
        return node

      for child in node["children"]:
        stack.append(child)

    return None

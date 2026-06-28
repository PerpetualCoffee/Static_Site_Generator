class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError()

	def props_to_html(self):
		if self.props is None or not self.props:
			return ""
		result = ""
		for key, value in self.props.items():
			result += f' {key}="{value}"'
		return result

	def __repr__(self):
		return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
	def __init__(self, tag=None, value=None, props=None):
		super().__init__(tag, value, None, props)
	
	def to_html(self):
		if self.value is None:
			raise ValueError("LeafNode must have a value")
		elif self.tag is None:
			return self.value
		else: 
			return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

	def __repr__(self):
		return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag, None, children, props)

	def to_html(self):
		if not self.tag:
			raise ValueError("ParentNode must have a tag")
		elif not self.children:
			raise ValueError("ParentNode must have children")
		else:
			result = f"<{self.tag}{self.props_to_html()}>"
			for child in self.children:
				result += child.to_html()
			result += f"</{self.tag}>"
			return result
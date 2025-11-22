class SoupReplacer:
    def __init__(self, og_tag = None, alt_tag = None,name_xformer=None, attrs_xformer=None, xformer=None):
        self.og_tag = og_tag
        self.alt_tag = alt_tag
        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer
    

    def replace(self, tag):
        
        if self.og_tag is not None and self.alt_tag is not None:
            if tag.name == self.og_tag:
                tag.name = self.alt_tag

        
    
        if self.name_xformer:
            new_name = self.name_xformer(tag)
            if new_name is not None:
                tag.name = new_name

        if self.attrs_xformer:
            new_attrs = self.attrs_xformer(tag)
            if new_attrs is not None:
                tag.attrs = new_attrs
            
        if self.xformer:
            self.xformer(tag)
    
    

        
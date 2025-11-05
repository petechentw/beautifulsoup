class SoupReplacer:
    def __init__(self, og_tag = None, alt_tag = None,name_xformer=None, attrs_xformer=None, xformer=None):
        self.og_tag = og_tag
        self.alt_tag = alt_tag
        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer
    

    def replace(self, tag):
        
        if self.og_tag and self.alt_tag and tag.name == self.og_tag:
            tag.name = self.alt_tag
        
    
        if self.name_xformer:
            change_name = self.name_xformer(tag)
            if change_name:
                tag.name = change_name

        if self.attrs_xformer:
            change_attrs = self.attrs_xformer(tag)
            if change_attrs:
                tag.attrs = change_attrs
            
        if self.xformer:
            self.xformer(tag)
    
    

        
class PaginationHelper:
    
    def __init__(self, collection, items_per_page):
        self.collection, self.items_per_page = collection, items_per_page
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        div = len(self.collection)//self.items_per_page
        return div + 1 if len(self.collection)%self.items_per_page != 0 else div
    
    # returns the number of items on the given page. page_index is zero based
    def page_item_count(self, page_index):
        if page_index < 0 or page_index >= self.page_count():
            return -1
        elif page_index < len(self.collection)//self.items_per_page:
            return self.items_per_page
        else:
            return len(self.collection)%self.items_per_page
            
    
    # determines what page an item at the given index is on. Zero based indexes.
    def page_index(self, item_index):
        if item_index >= len(self.collection):
            return -1
        for i in range(self.page_count()):
            if i * self.items_per_page <= item_index < (i+1) * self.items_per_page:
                return i 
        return -1
        
            
    
    
helper = PaginationHelper(['a','b','c','d','e','f', 'j', 'h', 'g'], 4)
print(helper.page_index(5))


# Solution 2

class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self._item_count = len(collection)
        self.items_per_page = items_per_page

    def item_count(self):
        return self._item_count

    def page_count(self):
        return -(self._item_count // -self.items_per_page)

    def page_item_count(self, page_index):
        return min(self.items_per_page, self._item_count - page_index * self.items_per_page) \
            if 0 <= page_index < self.page_count() else -1

    def page_index(self, item_index):
        return item_index // self.items_per_page \
            if 0 <= item_index < self._item_count else -1
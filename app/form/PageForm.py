class PageForm:

    def __init__(self, page_num=1, page_size=10, sort_by=None, order='ASC', keyword=None, search_by=None):
        """
        :param page_num: 页码
        :param page_size: 页大小
        :param sort_by: 排序字段
        :param order: 升序或降序[ASC | DESC]
        :param keyword: 关键字
        :param search_by: 搜索字段
        """
        self.pageNum = page_num
        self.pageSize = page_size
        self.sortBy = sort_by
        self.order = order
        self.keyword = keyword
        self.searchBy = search_by

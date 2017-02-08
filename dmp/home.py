# encoding: utf-8
#!/usr/bin/python

class HomePage(object):

    def find_element(self,dr):
        dr.find_element_by_xpath()

    def select_customer(self,dr,customer):
        dr.find_element_by_xpath('//*[@id="show_curr_customer"]').click()
        if customer=='cpic':
            dr.find_element_by_xpath('//li[@idvalue="473"]').click()
        elif customer=='testtesttest':
            dr.find_element_by_xpath('//li[@idvalue="472"]').click()
        elif customer==u'太平洋保险':
            dr.find_element_by_xpath('//li[@idvalue="539"]').click()

    def menu_data_access(self,dr):
        span=dr.find_element_by_xpath('//*[span="数据接入"]')
        return span

    def menu_partner(self,dr):
        span=dr.find_element_by_xpath('//*[span="合作伙伴"]')
        return span

    def submenu_data_overview(self,dr):
        li=dr.find_element_by_xpath('//*[a="接入概览"]')
        return li
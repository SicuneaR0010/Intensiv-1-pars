import cianparser
from time import sleep
a=2
while a < 54:
    data = cianparser.CianParser(location="Московская Область").get_flats(deal_type="sale",
                                                              rooms=3,
                                                              with_saving_csv=True,
                                                              with_extra_data=True,
                                                              additional_settings={"start_page":1+a, "end_page":2+a})
    print("----------------------------------------------------")
    print("Waiting 180 sec")
    sleep(180)
    a+=2

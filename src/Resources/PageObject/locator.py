class Locator(object):

    test_url = "https://www.mall.cz/"
    article = "//div[@class='cms-carousel-b__slider-wrapper']//ul[@class='hooper-track']//li//article"
    carousel_Body = "//section//div[contains(@class,'hooper-list') and ul//li[contains(@data-testid,'cms-carousel-slide')]]"
    tab    = "//section[@tabindex]"
    Button ="//button[@data-testid='rounded-button']//div//span[@class='rounded-button__wrapper__slot' and text()='\n          Souhlasím\n        ']"
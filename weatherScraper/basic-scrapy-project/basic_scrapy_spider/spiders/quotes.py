import scrapy

class WeatherScraperSpider(scrapy.Spider):
    name = 'WeatherScraperSpider'
    start_urls = [
        'https://weather.com/weather/monthly/l/aa0cfbbf27654104df53cb7b9f2ed626e6d7a550c2ab39433644ee8a1e6fe481'
    ]

    def parse(self, response):
        # Select all date cells
        date_cells = response.css('.CalendarDateCell--dayCell--3wgxE')
        
        for index,cell in enumerate(date_cells):
            # Extract the date
            date = cell.css('.CalendarDateCell--date--K4fJ-::text').get()

            # Extract high temperature
            high_temp = cell.css('.CalendarDateCell--tempHigh--9CJX7 span::text').getall()
            high_temp_cleaned = [temp for temp in high_temp if temp.isdigit()]
            high_temp_integer = int(''.join(high_temp_cleaned)) if high_temp_cleaned else None

            # Extract low temperature
            low_temp = cell.css('.CalendarDateCell--tempLow--pvc0J span::text').getall()
            low_temp_cleaned = [temp for temp in low_temp if temp.isdigit()]
            low_temp_integer = int(''.join(low_temp_cleaned)) if low_temp_cleaned else None

            
            # Yield the results for each date
            yield {
                'date': date,
                'high_temp': high_temp_integer,
                'low_temp': low_temp_integer,
                
            }

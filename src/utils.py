import codecs
import csv

def write_to_csv(csv_file: str, jobs: list, page_num: int=0) -> None:
    with codecs.open(csv_file, 'a', encoding='utf-8') as file:
        writer = csv.writer(file, lineterminator='\n')

        if page_num == 0:
            writer.writerow(['Title', 'Company', 'Location', 'Apply'])

        for job in jobs:
            writer.writerow([
                job.find('h3', class_='base-search-card__title').text.strip(),
                job.find('h4', class_='base-search-card__subtitle').text.strip(),
                job.find('span', class_='job-search-card__location').text.strip(),
                job.find('a', class_='base-card__full-link').text.strip(),
            ])
        
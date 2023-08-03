from linkedin import linkedin_run

KEYWORDS = ['junior', 'developer']
LOCATION = ['göteborg']

def main() -> None:
    df = linkedin_run(KEYWORDS, LOCATION)
    print(df.Title)
    print(df.Link)


if __name__ == '__main__':
    main()

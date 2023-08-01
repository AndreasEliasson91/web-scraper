from linkedin import linkedin_run, KEYWORDS, LOCATION

KEYWORDS = ['junior', 'developer']
LOCATION = ['göteborg']

def main() -> None:
    linkedin_run(KEYWORDS, LOCATION)


if __name__ == '__main__':
    main()

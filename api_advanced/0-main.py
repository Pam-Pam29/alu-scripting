def main():
    if len(sys.argv) != 2:
        print("Usage: python 0-main.py <subreddit>")
        sys.exit(1)

    subreddit = sys.argv[1]
    try:
        num_subscribers = number_of_subscribers(subreddit)
        print("OK")
    except Exception as e:
        print("Not found")

if __name__ == "__main__":
    main()

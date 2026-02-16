from server.crawl_grid import CrawlGrid


if __name__ == "__main__":
    crawl_grid = CrawlGrid(["http://localhost:8000"])
    # crawl_grid.launch_grid(instances=3)
    crawl_grid.close_grid()
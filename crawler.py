# --- Crawling algorithm
# AddURL(URL_frontier, URL_seeds); 
# while !empty URL_frontier
#     url = Pop(URL_frontier); 
#     page = Fetch(url); 
#     Index(page);
#     url_list = extract_urls(page);
#     filtered_urls = Filter(url_list);
#     for u in filtered_urls:
#        AddURL(URL_frontier, u);

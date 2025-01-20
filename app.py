
from fastapi import FastAPI, HTTPException
from Tasks.helper import getDriver
from Tasks.task1 import detect_backlinks
from Tasks.task10 import detect_event_backlinks
from Tasks.task15 import compare_backlinks
from Tasks.task2 import rank_tracking
from Tasks.task3 import sentiment_analysis_mentions
from Tasks.task4 import evaluate_anchor_SERP
from Tasks.task5 import scrap_serp
from Tasks.task6 import analyze_backlink_relevance
from Tasks.task8 import analyze_sentiment_trends
from Tasks.task9 import track_gmb_visibility


app = FastAPI()
driver = getDriver()


@app.get("/")
def read_root():
    return {"message": "Offline SEO Microservice is running!"}

# task 1


@app.get("/analyze_backlinks")
def analyze_backlinks_endpoint(keyword: str, main_domain: str):
    try:
        return detect_backlinks(keyword, main_domain, driver)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# task 2


@app.get("/track_rank")
def track_rank_endpoint(keyword: str, main_domain: str):
    try:
        return rank_tracking(keyword, main_domain, driver)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# task 3


@app.get("/analyze_sentiments")
def analyze_sentiments_endpoint(keyword: str, main_domain: str):
    try:
        return sentiment_analysis_mentions(keyword, main_domain, driver)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# task 4


@app.get("/anchor_text")
def anchor_text_endpoint(keyword: str, main_domain: str):
    try:
        return evaluate_anchor_SERP(keyword, main_domain, driver)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# task 5


@app.get("/domain_authority")
def domain_authority_endpoint(keyword: str, main_domain: str):
    try:
        return scrap_serp(keyword, main_domain, driver)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# task 6


@app.get("/analyze_relevance")
def analyze_relevance_endpoint(keyword: str, main_domain: str):
    try:
        return analyze_backlink_relevance(keyword, main_domain, driver)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# task 8


@app.get("/review_sentiment")
def review_sentiment_endpoint(url: str):
    try:
        return analyze_sentiment_trends(url, driver)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# task 9


@app.get("/business_listing_visibility")
def business_listing_visibility_endpoint(keyword: str):
    try:
        return track_gmb_visibility(keyword, driver)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# task 10


@app.get("/event_backlinks")
def event_backlinks_endpoint(keyword: str, main_domain: str):
    try:
        return detect_event_backlinks(keyword, main_domain, driver)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# task 15


@app.get("/compare_backlinks")
def compare_backlinks_endpoint(brand_keyword: str, competitor_keyword: str, brand_domain: str, competitor_domain: str):
    try:
        return compare_backlinks(brand_keyword, competitor_keyword, brand_domain, competitor_domain, driver)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

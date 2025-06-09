from kfp import dsl
from scraper_component import scraper_op
from analyse_component import analyse_op
from enrich_component import enrich_op

@dsl.pipeline(
    name="Smart eCommerce Pipeline",
    description="Scrape → Analyze → Enrich product data"
)
def smart_pipeline():
    step1 = scraper_op()
    step2 = analyse_op().after(step1)
    step3 = enrich_op().after(step2)


from index import app
from flask import render_template, request
from config import BASE_URL


@app.route('/')
def index():
    page_url = BASE_URL + request.path
    page_title = 'Beyond Beethoven'
    interview_base_url = 'http://www.vpr.net/apps/beyond-beethoven/static/audio/VPR-Inside-'
    interview = [
        'Mendelssohn-Op-58',
        'Brahms-Op-38',
        'Mendelssohn-Op-45',
        'Brahms-Op-99']

    social = {
        'title': "Beyond Beethoven",
        'subtitle': "A production of VPR Classical and Burlington Ensemble",
        'img': "http://www.vpr.net/apps/beyond-beethoven/static/img/vpr_beyond_beethoven_logo_white.png",
        'description': "After recording Beethoven's cello sonata cycle, Benjamin Capps and David Kaplan return to record cello sonatas by two Beethoven successors.",
        'twitter_text': "Listen to Ben Capps + David Kaplan perform cello sonatos by 2 Beethoven successors.",
        'twitter_hashtag': "Brahms,Mendelssohn"
    }

    return render_template('content.html',
        page_title=page_title,
        social=social,
        interview=interview,
        interview_base_url=interview_base_url,
        page_url=page_url)

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import text2emotion as te
import spacy


class API:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
        self.nlp = spacy.load("en_core_web_sm")

    # Sentiment Analysis
    def sentiment_analysis(self, text):
        scores = self.analyzer.polarity_scores(text)
        
        if scores['compound'] >= 0.05:
            sentiment = "Positive"
        elif scores['compound'] <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"
        
        return {
            "sentiment": sentiment,
            "scores": scores
        }

    # Emotion Detection
    def emotion_detection(self, text):
        emotions = te.get_emotion(text)
        # Sabse high emotion pick karna
        main_emotion = max(emotions, key=emotions.get)
        return {
            "emotion": main_emotion,
            "scores": emotions
        }

    # Named Entity Recognition (NER)
    def named_entity_recognition(self, text):
        doc = self.nlp(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return {
            "entities": entities
        }
